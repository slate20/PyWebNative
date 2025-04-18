import webview
import os
from flask import Flask
from routes import bp as main_blueprint

# --- Flask App Setup ---
app = Flask(__name__)

# --- Register Blueprints ---
app.register_blueprint(main_blueprint)

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
