# PyWebNative - Flask + HTMX Template

This template provides a starting point for building native-like desktop applications using Python, powered by a Flask backend and a dynamic frontend using HTMX, all packaged within a PyWebview window.

It allows you to leverage Python for backend logic while using standard web technologies (HTML, CSS) enhanced with HTMX for creating interactive UIs with minimal JavaScript.

## Features

*   **Native Window:** Uses `pywebview` to create a lightweight native OS window.
*   **Python Backend:** Employs `Flask` for handling requests, routing, and server-side logic.
*   **Dynamic Frontend:** Uses `HTMX` to enable modern browser features (AJAX, CSS Transitions, WebSockets) directly from HTML, reducing the need for custom JavaScript.
*   **Standard Web Tech:** Build your UI with HTML, CSS, and Flask's Jinja2 templating.
*   **Cross-Platform:** Compatible with Windows, macOS, and Linux.

## Project Structure

```
/
├── .venv/               # Virtual environment directory
├── static/              # Static files (CSS, JS, images)
│   ├── css/style.css
│   └── js/              # (Optional JS if needed)
├── templates/           # HTML templates (Jinja2)
│   └── index.html
├── app.py               # Main application entry point (Initializes Flask & PyWebview)
├── routes.py            # Flask Blueprint containing application routes/view functions
├── requirements.txt     # Python dependencies
├── user_methods.py      # (Optional) For non-route Python helper functions/classes
└── README.md            # This file
```

## Getting Started

### Prerequisites

*   Python 3.7+
*   `pip` and `venv` (usually included with Python)

### Setup

1.  **Clone the repository (or use this template):**
    ```bash
    # git clone ... (if applicable)
    cd PyWebNative # Navigate to the project directory
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # On Windows
    .\.venv\Scripts\activate
    # On macOS/Linux
    # source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

```bash
python app.py
```

This will start the Flask development server and open the `pywebview` window, loading the application.

## Development Guide

### Adding New Features

1.  **Define a Route:** Add a new function decorated with `@bp.route('/your-new-route', methods=['GET', 'POST'])` in `routes.py`.
    *   This function will handle requests to `/your-new-route`.
    *   It should typically return an HTML fragment or redirect.

2.  **Update the Frontend:** In `templates/index.html` (or other templates):
    *   Add HTML elements.
    *   Use HTMX attributes (e.g., `hx-get`, `hx-post`, `hx-target`, `hx-swap`) on elements (like buttons or forms) to trigger requests to your new route.
    *   Specify a target element where the HTML response from your route should be placed.

3.  **Add Static Files:** Place CSS, JavaScript (if absolutely necessary), or images in the `static/` directory and reference them in your templates using `{{ url_for('static', filename='path/to/your/file') }}`.

### Example Workflow (Adding a 'Clear Data' Button)

1.  **routes.py:**
    ```python
    import os
    # ... other imports ...

    @bp.route('/clear_data', methods=['POST'])
    def clear_data_route():
        try:
            if os.path.exists('data.json'):
                os.remove('data.json')
                return "<p style='color: orange;'>Data cleared.</p>"
            else:
                return "<p style='color: grey;'>No data file to clear.</p>"
        except Exception as e:
            return f"<p style='color: red;'>Error clearing data: {e}</p>"
    ```

2.  **templates/index.html** (Inside the 'Save Data Test' section):
    ```html
    <section class="card">
        <h2>Save Data Test</h2>
        <div class="form-group" hx-swap="innerHTML">
            <textarea id="data-input" name="data-input" placeholder="Enter JSON data to save..."></textarea>
            <!-- Existing Save Button -->
            <button hx-post="/save_data" hx-include="[name='data-input']" hx-target="#save-result" hx-indicator="#save-result">Save Data</button>
            <!-- New Clear Button -->
            <button hx-post="/clear_data" hx-target="#save-result" hx-indicator="#save-result">Clear Saved Data</button>
        </div>
        <div id="save-result" class="result"></div>
    </section>
    ```

## Further Information

*   **PyWebview:** [https://pywebview.flowrl.com/](https://pywebview.flowrl.com/)
*   **Flask:** [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
*   **HTMX:** [https://htmx.org/](https://htmx.org/)
*   **Jinja2 (Templating):** [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/)
