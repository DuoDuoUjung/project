from django.urls import path
from django.http import HttpResponse
import requests

# 定義代理到 Flask 的視圖
def flask_proxy(request, path):
    try:
        # 將請求代理到 Flask
        flask_url = f"http://127.0.0.1:5500/{path}"  # Flask 運行的服務
        if request.method == "GET":
            response = requests.get(flask_url)
        elif request.method == "POST":
            response = requests.post(flask_url, json=request.body)
        else:
            return HttpResponse("Unsupported method", status=405)

        # 返回 Flask 的回應
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers.get('Content-Type', 'text/plain'))
    except Exception as e:
        return HttpResponse(f"Error connecting to Flask: {e}", status=500)

# 配置 URL 路由
urlpatterns = [
    path('flask_service/<path:path>', flask_proxy),  # 所有 Flask 的路由以 flask_service 開頭
]
