import json
import os
import sys
import time

"""
Business Logic functions for demonstration.

Replace with your own business logic functions.
"""

def get_formatted_system_info():
    try:
        info = {
            'python_version': sys.version.split()[0],
            'platform': sys.platform,
            'time': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        html_fragment = f"Python Version: {info['python_version']}\n"
        html_fragment += f"Platform: {info['platform']}\n"
        html_fragment += f"Current Time: {info['time']}"
        return html_fragment
    except Exception as e:
        # In case fetching info fails unexpectedly
        return f"Error getting system info: {e}"

def get_echo_response(message):
    # Basic sanitization could be added here if needed
    safe_message = message # Placeholder for potential future sanitization
    return f"<p>Server received: <code>{safe_message}</code></p>"

def save_json_data(data_string, filename="data.json"):
    try:
        # Attempt to parse the text as JSON before saving
        data_obj = json.loads(data_string)
        # Consider saving data to a more robust location or subfolder
        # For example, create a 'data' subdirectory if it doesn't exist:
        # data_dir = 'data'
        # os.makedirs(data_dir, exist_ok=True)
        # filepath = os.path.join(data_dir, filename)
        filepath = filename # Keep original behavior for now

        with open(filepath, 'w') as f:
            json.dump(data_obj, f, indent=2) # Save parsed object, pretty print
        return True, "Data saved successfully!"
    except json.JSONDecodeError:
        return False, "Error: Invalid JSON format."
    except Exception as e:
        # Log the error for debugging?
        # print(f"Error saving data: {e}")
        return False, f"Error saving data: {e}"

# Add other core logic functions here later, e.g.:
# def load_json_data(filename="data.json"):
#     ...
# def clear_json_data(filename="data.json"):
#     ...