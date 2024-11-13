from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    data = request.get_json()
    code = data.get('code', '')
    print(f"Received code on server: {code}")  # 確認伺服器接收到的代碼
    
    try:
        # 執行 Python 代碼並捕獲輸出
        result = subprocess.run(['python3', '-c', code], capture_output=True, text=True, timeout=5)
        output = result.stdout if result.returncode == 0 else result.stderr
        print(f"Execution output: {output}")  # 檢查執行結果
    except subprocess.TimeoutExpired:
        output = "Error: Code execution timed out."
    except Exception as e:
        output = f"Error: {str(e)}"
    
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True, port=5500)