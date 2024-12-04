from django.contrib import admin
from django.urls import path, include
from friends_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from django.urls import path



urlpatterns = [
    path('', views.home, name='home'),  # 根路徑指向首頁
    path('friends/', views.friend_list, name='friend_list'),  # 好友列表頁面
    path('chat/', views.chat_room, name='chat_room'),  # 聊天頁面
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('header/', views.header, name='login'),
    path('admin/', admin.site.urls),  # 這行是必須的，讓 admin 能夠訪問
    path('add_friend/', views.add_friend, name='add_friend'),  # 確認路由名稱為 'add_friend'
    path('remove_friend/<int:friend_id>/', views.remove_friend, name='remove_friend'),
    path('test_app/', include('test_app.urls')),  # 包含 test_app 的路由
    path('teach_app/', include('teach_app.urls')),  # 包含 teach_app 的路由
    path('login_app/', include('login_app.urls')),  # 包含 login_app 的路由
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 設定靜態文件和媒體文件的路由
    