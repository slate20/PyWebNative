import os
import json
import sys
import time
from user_methods import UserMethods

class BaseAPI:
    """
    Python backend API that can be called from JavaScript
    All methods in this class can be called from JavaScript
    """
    
    def __init__(self):
        self.window = None  # Will be set by webview
    
    def init(self, window):
        """Initialize the API with the window object"""
        self.window = window
        return True
    
    def get_system_info(self):
        """Example method that returns system information"""
        info = {
            'python_version': sys.version,
            'platform': sys.platform,
            'time': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return info
    
    def echo(self, message):
        """Echo a message back to JavaScript"""
        return message
    
    def save_data(self, data):
        """Example method to save data to a file"""
        try:
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return {'success': True}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
class API(BaseAPI, UserMethods):
    pass
