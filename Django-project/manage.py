#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess


def start_flask():
    """啟動 Flask 應用"""
    flask_path = os.path.join(os.getcwd(), "../flask_service/app.py")  # 修改為正確路徑
    try:
        subprocess.Popen(["python", flask_path], stdout=sys.stdout, stderr=sys.stderr)
        print("Flask application started successfully.")
    except Exception as e:
        print(f"Failed to start Flask application: {e}")


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django-project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # 啟動 Flask 子進程
    start_flask()

    # 啟動 Django
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
