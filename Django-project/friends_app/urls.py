from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import add_friend, remove_friend


urlpatterns = [ 
    path('', views.friend_list, name='home'),  # 根路徑指向 friend_list
    path('friends/', views.friend_list, name='friend_list'),
    path('chat/', views.chat_room, name='chat_room'),
    path('accounts/login/', views.custom_login, name='login'),  # 自訂的登入視圖
    path('friends/<int:friend_id>/', views.friend_list, name='friend_detail'),  # 動態路由
    path('add_friend/', views.add_friend, name='add_friend'),  # 確認路由名稱為 'add_friend'
    path('get_chat_history', views.get_chat_history, name='get_chat_history'),
    path('send_message', views.send_message, name='send_message'),
    path('upload-avatar/', views.upload_avatar, name='upload_avatar'),  # 上傳圖片的頁面
    # 其他路由...
]
