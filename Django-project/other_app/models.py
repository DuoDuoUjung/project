from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  # 使用 settings 來引用 AUTH_USER_MODEL
import random
import string

class Course(models.Model):
    students = models.ManyToManyField(settings.AUTH_USER_MODEL)  # 應該指向 `AUTH_USER_MODEL`，而不是直接 `User`

    def __str__(self):
        return self.title

# 創建一些預設的課程語言，最多人學的六個程式語言
def create_default_courses():
    courses = [
        {"name": "Python", "description": "Learn Python, a powerful general-purpose programming language."},
        {"name": "Java", "description": "Master Java, the foundation of Android development."},
        {"name": "C++", "description": "Learn C++, a language for game development and system software."},
        {"name": "JavaScript", "description": "Explore JavaScript, the language of the web."},
        {"name": "Ruby", "description": "Learn Ruby, a dynamic language for web applications."},
        {"name": "PHP", "description": "Master PHP, the server-side scripting language for web development."},
    ]
    
    for course_data in courses:
        Course.objects.get_or_create(name=course_data['name'], defaults={'description': course_data['description']})




