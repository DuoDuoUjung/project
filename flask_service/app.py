from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    data = request.get_json()
    code = data.get('code', '')
    print(f"Received code on server: {code}")
    
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

# 路由配置，直接渲染模板
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

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500)