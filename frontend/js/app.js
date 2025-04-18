// Main application JavaScript file
document.addEventListener('DOMContentLoaded', () => {
    // Wait for pywebview API to be available before initializing
    waitForPywebviewApi();
});

// Function to wait for the pywebview API to be available
function waitForPywebviewApi() {
    if (window.pywebview && window.pywebview.api) {
        // API is available, initialize the app
        initApp();
    } else {
        // API not available yet, wait and try again
        console.log('Waiting for pywebview API to be available...');
        setTimeout(waitForPywebviewApi, 100);
    }
}

async function initApp() {
    try {
        // Load system information when the app starts
        await loadSystemInfo();
        
        // Set up event listeners
        setupEventListeners();
    } catch (error) {
        console.error('Error initializing app:', error);
    }
}

async function loadSystemInfo() {
    try {
        const systemInfoElement = document.getElementById('system-info');
        // Call the Python backend method
        const info = await window.pywebview.api.get_system_info();
        // Format and display the information
        systemInfoElement.textContent = JSON.stringify(info, null, 2);
    } catch (error) {
        console.error('Error loading system info:', error);
        document.getElementById('system-info').textContent = 'Error loading system information';
    }
}

function setupEventListeners() {
    // Refresh system info button
    document.getElementById('refresh-info').addEventListener('click', loadSystemInfo);
    
    // Echo button
    document.getElementById('echo-button').addEventListener('click', async () => {
        const input = document.getElementById('echo-input').value;
        const resultElement = document.getElementById('echo-result');
        
        try {
            // Call the Python backend method
            const result = await window.pywebview.api.echo(input);
            resultElement.textContent = `Echo response: ${result}`;
            resultElement.style.color = '#2ecc71';
        } catch (error) {
            console.error('Echo error:', error);
            resultElement.textContent = `Error: ${error.message || 'Unknown error'}`;
            resultElement.style.color = '#e74c3c';
        }
    });
    
    // Save data button
    document.getElementById('save-button').addEventListener('click', async () => {
        const dataInput = document.getElementById('data-input').value;
        const resultElement = document.getElementById('save-result');
        
        try {
            // Parse the JSON input
            const data = JSON.parse(dataInput);
            
            // Call the Python backend method
            const result = await window.pywebview.api.save_data(data);
            
            if (result.success) {
                resultElement.textContent = 'Data saved successfully!';
                resultElement.style.color = '#2ecc71';
            } else {
                resultElement.textContent = `Error saving data: ${result.error}`;
                resultElement.style.color = '#e74c3c';
            }
        } catch (error) {
            console.error('Save data error:', error);
            resultElement.textContent = `Error: ${error.message || 'Unknown error'}`;
            resultElement.style.color = '#e74c3c';
        }
    });
}

// Helper function to create a notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.classList.add('fade-out');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 500);
    }, 3000);
}
