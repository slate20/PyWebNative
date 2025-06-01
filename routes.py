import sys
import time
import json
from flask import Blueprint, render_template, request, jsonify
from logic import save_json_data, get_formatted_system_info, get_echo_response

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

# Routes for App demo
@bp.route('/get_system_info', methods=['GET'])
def get_system_info_route():
    """Handles request for system info, calls logic.get_formatted_system_info."""
    # Call the business logic function
    html_response = get_formatted_system_info()
    return html_response

@bp.route('/echo', methods=['POST'])
def echo_route():
    """Handles echo request, calls logic.get_echo_response."""
    message = request.form.get('echo-input', '') 
    # Call the business logic function
    html_response = get_echo_response(message)
    return html_response

@bp.route('/save_data', methods=['POST'])
def save_data_route():
    """Handles request to save data, calls logic.save_json_data."""
    data_to_save_text = request.form.get('data-input', '{}') 
    
    # Call the business logic function
    success, message = save_json_data(data_to_save_text)
    
    # Format the response based on the result from the logic function
    if success:
        html_response = f"<p style='color: green;'>{message}</p>"
    else:
        html_response = f"<p style='color: red;'>{message}</p>"
        
    return html_response