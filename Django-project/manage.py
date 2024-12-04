#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
import threading


def start_flask():
    """啟動 Flask 應用"""
    flask_path = os.path.abspath(os.path.join(os.getcwd(), "../flask_service/app.py"))  # 確保路徑正確
    try:
        # 使用獨立子進程運行 Flask，並確保輸出同步顯示到主進程
        subprocess.Popen(
            ["python", flask_path],
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        print("Flask application started successfully.")
    except FileNotFoundError:
        print(f"Flask application not found at {flask_path}. Please check the path.")
    except Exception as e:
        print(f"Failed to start Flask application: {e}")


def main():
    """主進入點，啟動 Django 並並行啟動 Flask"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django-project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # 使用 threading 啟動 Flask 子進程
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    # 啟動 Django 主進程
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
