from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from other_app.models import Course  # 如果這個模型存在於其他 app 中，可以保留
import random
import string

# 自定義 CustomUser 模型
class CustomUser(AbstractUser):

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    completed_topics = models.ManyToManyField('PythonTopic', blank=True)  # 自定義 `completed_topics` 欄位

# Friend 模型
class Friend(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='friends_profile')
    friends = models.ManyToManyField(CustomUser, related_name='friend_list')

    def __str__(self):
        return self.user.username

# ChatMessage 模型
class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} -> {}: {}...'.format(self.sender, self.receiver, self.text[:20])

# PythonTopic 模型
class PythonTopic(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Topic 模型
class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')

    def __str__(self):
        return self.user.username
