import subprocess
import webbrowser
import time

# Djangoサーバーをバックグラウンドで起動
subprocess.Popen(['python', 'manage.py', 'runserver'])

# サーバーが起動するのを待つ
time.sleep(1)  # 1秒待つ

# 指定されたURLをデフォルトのブラウザで開く
webbrowser.open('http://127.0.0.1:8000/myapp/hakodate_restaurant/')