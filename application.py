from flask import Flask, request, jsonify, render_template_string
from threading import Lock
import json

application = Flask(__name__)

# Thread-safe storage for events
events = []
events_lock = Lock()

@application.route('/')
def home():
    # HTML form with separate JavaScript functions for POST and GET
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Audit Log Service</title>
        <script>
            async function postEvent() {
                // Get the value from input
                const eventData = document.getElementById("eventData").value;

                // POST request
                const response = await fetch('/events', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ "data": eventData })
                });
                const data = await response.json();

                // Display POST response
                document.getElementById("postResult").textContent = JSON.stringify(data);
            }

            async function getEvents() {
                // GET request
                const response = await fetch('/events', {
                    method: 'GET'
                });
                const data = await response.json();

                // Display GET response
                document.getElementById("getResult").textContent = JSON.stringify(data);
            }
        </script>
    </head>
    <body>
        <h1>Welcome to the Audit Log Service!</h1>
        <input type="text" id="eventData" placeholder="Enter event data" />
        <button onclick="postEvent()">Post Event</button>
        <button onclick="getEvents()">Get Audit of All Events</button>
        <h2>POST Response:</h2>
        <pre id="postResult"></pre>
        <h2>GET Response:</h2>
        <pre id="getResult"></pre>
    </body>
    </html>
    '''
    return render_template_string(html_content)

@application.route('/events', methods=['POST'])
def create_event():
    event = request.json["data"]
    with events_lock:
        events.append(event)
    return jsonify({"status": "success", "event": event}), 201

@application.route('/events', methods=['GET'])
def get_events():
    with events_lock:
        return jsonify(events), 200
    
@application.route('/favicon.ico')
def favicon():
    return '', 204  # No content to return

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)
