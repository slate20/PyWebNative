import webview
import os
import sys
import json
from api import API

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    print(f"Resource path: {os.path.join(base_path, relative_path)}")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    # Create API instance
    api = API()
    
    # Set up the window
    window = webview.create_window(
        title='PyWebview App',
        url=get_resource_path('frontend/index.html'),  # Use main index.html file
        js_api=api,
        width=800,
        height=600,
        resizable=True,
        min_size=(400, 300)
    )
    
    # Start the webview application
    webview.start(debug=True)
