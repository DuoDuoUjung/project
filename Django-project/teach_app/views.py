import requests
from django.shortcuts import render
from django.http import JsonResponse

def teach_view(request):
    return render(request, 'teach.html')

def proxy_to_flask(request):
    flask_url = "http://127.0.0.1:5500/run-python"  # Flask 的路徑
    response = requests.post(flask_url, json=request.POST)  # 發送 Django 請求到 Flask
    return JsonResponse(response.json())  # 返回 Flask 的結果

