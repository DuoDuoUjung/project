from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # 啟用跨域支持

@app.route('/')
def index():
    return "Flask App Running"

@app.route('/run-python', methods=['POST'])
def run_python():
    data = request.get_json()
    code = data.get('code', '').strip()
    print(f"Received code on server: {code}")

    if not code:
        return jsonify({'output': 'Error: No code provided.'})

    if 'import os' in code or 'import shutil' in code:
        return jsonify({'output': 'Error: Unsafe code detected.'})

    try:
        result = subprocess.run(
            ['python', '-c', code],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            output = result.stdout.strip() if result.stdout else "No output produced."
        else:
            output = result.stderr.strip()
        print(f"Execution output: {output}")
    except subprocess.TimeoutExpired:
        output = "Error: Code execution timed out."
    except Exception as e:
        output = f"Error: {str(e)}"

    return jsonify({'output': output})


@app.route('/TryPython.html')
def trypython():
    return render_template('TryPython.html')

@app.route('/TryHtml.html')
def tryhtml():
    return render_template('TryHtml.html')

@app.route('/header.html')
def header():
    return render_template('header.html')

@app.route('/teach.html')
def teach():
    return render_template('teach.html')

@app.route('/ans.html')
def ans():
    return render_template('ans.html')


if __name__ == '__main__':
    app.run(debug=True, port=5500)