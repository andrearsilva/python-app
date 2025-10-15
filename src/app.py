from flask import Flask, jsonify
import socket
# CORRECTED IMPORT: We now import the 'datetime' class from the 'datetime' module.
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# This line is now correct because we imported the datetime class directly.
now = datetime.now()

@app.route('/api/v1/details')
def details():
    """
    Returns the current time and the server's hostname.
    """
    return jsonify({    
        # Use datetime.now() directly here as well
        'timenow': datetime.now().strftime("%I:%M%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'test new changes 1'
    })

@app.route('/api/v1/healthz')
def healthz():
    """
    Simple health check endpoint.
    """
    return jsonify({'status': 'up'}), 200

# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0')