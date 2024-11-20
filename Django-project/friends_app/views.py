from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Friend, PythonTopic, ChatMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ChatMessage

import json
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

@login_required
def friend_list(request):
    # 查詢當前使用者的好友資料
    if hasattr(request.user, 'friends_profile'):
        friends = request.user.friends_profile.friends.exclude(username=request.user.username)
    else:
        friends = []  # 如果沒有找到 `friends_profile` 屬性，則返回空列表

    # 取得 `friend_id` 來選擇特定好友的資料
    friend_id = request.GET.get('friend_id')
    if friend_id:
        selected_friend = get_object_or_404(User, id=friend_id)
        streak_days = 30  # 假設為 30 天
        progress_percent = calculate_progress(selected_friend)
    else:
        selected_friend = None
        streak_days = 0
        progress_percent = 0

    # 查詢所有 Python 課程主題
    python_topics = PythonTopic.objects.all()

    context = {
        'friends': friends,
        'user': request.user,
        'selected_friend': selected_friend, 
        'streak_days': streak_days,
        'progress_percent': progress_percent,
        'python_topics': python_topics,
    }
    return render(request, 'friends_app/friend_list.html', context)

# 計算好友的學習進度
def calculate_progress(friend):
    total_topics = PythonTopic.objects.count()
    completed_topics = friend.completed_topics.count() if hasattr(friend, 'completed_topics') else 0
    return (completed_topics / total_topics) * 100 if total_topics > 0 else 0

@login_required
def chat_room(request):
    if request.method == 'POST':
        message_text = request.POST.get('message')
        receiver_username = request.POST.get('receiver')
        try:
            receiver = User.objects.get(username=receiver_username)
            message = ChatMessage(sender=request.user, receiver=receiver, text=message_text)
            message.save()
        except User.DoesNotExist:
            messages.error(request, "接收者不存在")

    # 獲取與當前用戶相關的聊天消息
    messages_qs = ChatMessage.objects.filter(sender=request.user) | ChatMessage.objects.filter(receiver=request.user)
    messages_qs = messages_qs.order_by('timestamp')
    users = User.objects.exclude(id=request.user.id)

    return render(request, 'friends_app/chat.html', {'messages': messages_qs, 'users': users})

@login_required
def add_friend(request):
    if request.method == 'POST':
        friend_identifier = request.POST.get('friend_identifier')
        search_type = request.POST.get('search_type')

        try:
            # 根據 search_type 確定查找條件
            if search_type == 'username':
                friend = User.objects.get(username=friend_identifier)
            elif search_type == 'id':
                friend = User.objects.get(id=friend_identifier)
            else:
                messages.error(request, "無效的搜尋類型")
                return redirect('friend_list')

            current_user = request.user
            friend_profile, created = Friend.objects.get_or_create(user=current_user)

            # 確認好友是否已存在
            if friend in friend_profile.friends.all():
                messages.error(request, "已經有該好友")
            else:
                friend_profile.friends.add(friend)
                messages.success(request, "好友已成功添加！")
                
            return redirect('friend_list')

        except User.DoesNotExist:
            messages.error(request, "找不到該使用者")
            return redirect('friend_list')

@login_required
def remove_friend(request, friend_id):
    if request.method == 'POST':
        current_user = request.user
        friend_profile = get_object_or_404(Friend, user=current_user)

        try:
            friend_to_remove = User.objects.get(id=friend_id)
            friend_profile.friends.remove(friend_to_remove)
            messages.success(request, "好友已成功移除！")
        except User.DoesNotExist:
            messages.error(request, "找不到該使用者")

    return redirect('friend_list')

def home(request):
    return render(request, 'index.html')


# 假設從數據庫獲取聊天歷史
def get_chat_history(request):
    username = request.GET.get("username")
    # 假設從數據庫獲取對話記錄
    messages = [
        {"sender": "me", "content": "我很認真啊！！！"},
        {"sender": username, "content": "該認真學習了吧"},
        {"sender": "me", "content": "太關心我了吧"},
    ]
    return JsonResponse({"messages": messages})

# 處理消息發送
@csrf_exempt
def send_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")
        # 保存消息到數據庫（此處省略）
        return JsonResponse({"status": "success", "message": message})
    return JsonResponse({"status": "error"}, status=400)


def get_chat_messages(request, username):
    # 假設資料庫中有 ChatMessage 模型
    # 這裡會從資料庫獲取對話內容，根據接收者和發送者篩選
    messages = ChatMessage.objects.filter(
        recipient__username=username
    ).order_by('timestamp')
    
    # 格式化返回的消息
    messages_data = [
        {
            'content': message.content,
            'sent_by': 'me' if message.sender == request.user else 'other',
            'avatar': message.sender.avatar.url if message.sender.avatar else '/static/images/default-avatar.png'
        }
        for message in messages
    ]
    
    return JsonResponse({'messages': messages_data})


def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content')
        recipient_username = data.get('recipient')
        
        recipient = User.objects.get(username=recipient_username)
        message = ChatMessage(sender=request.user, recipient=recipient, content=content)
        message.save()
        
        return JsonResponse({'status': 'success', 'avatar': request.user.avatar.url if request.user.avatar else '/static/images/default-avatar.png'})
    
def header(request):
    return render(request, 'header.html')