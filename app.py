import webview
import os
import sys
import json
import time 
from flask import Flask, render_template, request, jsonify 
from user_methods import UserMethods 

# --- Flask App Setup ---
app = Flask(__name__) 

# --- API Logic (moved from api.py) ---

class API(UserMethods): 
    pass

# Example API methods converted to Flask routes
@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/get_system_info', methods=['GET'])
def get_system_info_route():
    """Flask route equivalent of BaseAPI.get_system_info, returns HTML fragment."""
    info = {
        'python_version': sys.version.split()[0], 
        'platform': sys.platform,
        'time': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    html_fragment = f"Python Version: {info['python_version']}\n"
    html_fragment += f"Platform: {info['platform']}\n"
    html_fragment += f"Current Time: {info['time']}"
    return html_fragment 

@app.route('/echo', methods=['POST'])
def echo_route():
    """Flask route equivalent of BaseAPI.echo, returns HTML fragment."""
    message = request.form.get('echo-input', '') 
    return f"<p>Server received: <code>{message}</code></p>" 

@app.route('/save_data', methods=['POST'])
def save_data_route():
    """Flask route equivalent of BaseAPI.save_data, returns HTML fragment."""
    data_to_save_text = request.form.get('data-input', '{}') 
    try:
        data_obj = json.loads(data_to_save_text)
        with open('data.json', 'w') as f:
            json.dump(data_obj, f, indent=2) 
        return "<p style='color: green;'>Data saved successfully!</p>"
    except json.JSONDecodeError:
        return "<p style='color: red;'>Error: Invalid JSON format.</p>"
    except Exception as e:
        return f"<p style='color: red;'>Error saving data: {e}</p>"

if __name__ == '__main__':
    window = webview.create_window(
        title='Flask + PyWebview App',
        url=app,  
        width=800,
        height=600,
        resizable=True,
        min_size=(400, 300)
    )

    webview.start(debug=True)
