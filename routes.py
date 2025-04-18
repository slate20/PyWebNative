import sys
import time
import json
from flask import Blueprint, render_template, request, jsonify

# Create a Blueprint instance
# The first argument 'main' is the name of the blueprint.
# The second argument __name__ helps Flask locate the blueprint's resources.
# 'template_folder' tells Flask where to find templates for this blueprint.
bp = Blueprint('main', __name__, template_folder='templates')

@bp.route('/')
def index():
    """Serves the main HTML page."""
    # render_template will automatically look in the 'templates' folder
    # associated with this blueprint (or the app's default if not found here)
    return render_template('index.html')

@bp.route('/get_system_info', methods=['GET'])
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

@bp.route('/echo', methods=['POST'])
def echo_route():
    """Flask route equivalent of BaseAPI.echo, returns HTML fragment."""
    message = request.form.get('echo-input', '')
    return f"<p>Server received: <code>{message}</code></p>"

@bp.route('/save_data', methods=['POST'])
def save_data_route():
    """Flask route equivalent of BaseAPI.save_data, returns HTML fragment."""
    data_to_save_text = request.form.get('data-input', '{}')
    try:
        data_obj = json.loads(data_to_save_text)
        # Consider saving data to a more robust location or subfolder
        with open('data.json', 'w') as f:
            json.dump(data_obj, f, indent=2)
        return "<p style='color: green;'>Data saved successfully!</p>"
    except json.JSONDecodeError:
        return "<p style='color: red;'>Error: Invalid JSON format.</p>"
    except Exception as e:
        return f"<p style='color: red;'>Error saving data: {e}</p>"

# You can add more routes here related to the main functionality