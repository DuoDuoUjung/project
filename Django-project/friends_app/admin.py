# friends_app/admin.py

from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Friend
from .models import User
import random
import string

# 獲取自定義的 User 模型（CustomUser）
CustomUser = get_user_model()

# 生成6位數ID
def generate_custom_id():
    return ''.join([random.choice(string.digits) for _ in range(6)])

# 擴展 UserAdmin，增加自定義的 ID 欄位
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'custom_id')

    # 自定義欄位，生成6位數 ID
    def custom_id(self, obj):
        if not hasattr(obj, '_custom_id'):
            obj._custom_id = generate_custom_id()
        return obj._custom_id

    custom_id.short_description = 'Custom ID'


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'avatar']  # 顯示 avatar 欄位
# 取消註冊預設的 UserAdmin，並重新註冊 CustomUserAdmin
# 使用 admin.site.is_registered 檢查 User 是否已註冊，避免未註冊時報錯
if admin.site.is_registered(CustomUser):
    admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)

# 註冊 Friend 模型到 Django 後台
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('user',)  # 顯示哪些欄位
    filter_horizontal = ('friends',)  # 讓你能通過管理後台編輯好友列表


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'avatar')  # 顯示名稱和頭像
