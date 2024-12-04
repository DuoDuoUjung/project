import requests
from django.shortcuts import render
from django.http import JsonResponse

def ans_view(request):
    return render(request, 'ans.html')

def test_view(request):
    return render(request, 'test.html')

def execute_code(request):
    """與 Flask 應用交互執行代碼"""
    if request.method == 'POST':
        code = request.POST.get('code', '')
        flask_url = "http://127.0.0.1:5500/run-python"  # Flask 提供的端點
        try:
            response = requests.post(flask_url, json={"code": code})
            if response.status_code == 200:
                result = response.json()
                return JsonResponse({'output': result.get('output', 'No output received.')})
            else:
                return JsonResponse({'error': 'Flask service returned an error.'}, status=500)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'test_app/execute.html')  # 渲染 Django 的模板
