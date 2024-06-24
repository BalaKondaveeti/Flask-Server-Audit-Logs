
# Audit Log Service - Flask Application

This repository contains a simple Flask server that runs on AWS EC2, designed to manage audit log events. The application allows users to post and retrieve events via a web interface and RESTful API.

## Features

- Web interface to post and get audit events
- RESTful API for posting and retrieving events
- Thread-safe storage for handling concurrent requests

## Prerequisites

- Python 3.x
- Flask
- AWS EC2 instance

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/BalaKondaveeti/Flask-Server-Audit-Logs.git
    cd audit-log-service
    ```

2. **Install required packages:**

    ```bash
    pip install Flask
    ```

## Running the Application

1. **Start the Flask server:**

    ```bash
    python application.py
    ```

2. **Access the application:**
   Open your browser and go to `http://<EC2_PUBLIC_IP>:5000`

## Deployment on AWS EC2

1. **Launch an EC2 instance:**
   - Choose an Amazon Machine Image (AMI) with Python installed (e.g., Amazon Linux 2).
   - Configure security group to allow inbound traffic on port 5000.

2. **Connect to your EC2 instance:**

    ```bash
    ssh -i <your-key-pair>.pem ec2-user@<EC2_PUBLIC_IP>
    ```

3. **Transfer the application files to the EC2 instance:**

    ```bash
    scp -i <your-key-pair>.pem -r ./* ec2-user@<EC2_PUBLIC_IP>:/home/ec2-user/
    ```

4. **Install Flask on the EC2 instance:**

    ```bash
    sudo yum install python3 -y
    pip3 install Flask
    ```

5. **Run the Flask application on the EC2 instance:**

    ```bash
    python3 application.py
    ```

## Application Endpoints

- **Home Page:**

  ```
  GET /
  ```

  Displays the web interface for posting and retrieving events.

- **Create Event:**

  ```
  POST /events
  ```

  - Request Body: `{ "data": "event data" }`
  - Response: `{ "status": "success", "event": "event data" }`

- **Get Events:**

  ```
  GET /events
  ```

  - Response: List of all posted events

## Code Overview

- `application.py`: Main application file containing the Flask server logic.
  - `@application.route('/')`: Serves the home page with the web interface.
  - `@application.route('/events', methods=['POST'])`: Handles POST requests to create events.
  - `@application.route('/events', methods=['GET'])`: Handles GET requests to retrieve all events.

## Acknowledgments

- Flask documentation: https://flask.palletsprojects.com/
- AWS EC2 documentation: https://docs.aws.amazon.com/ec2/

---

Feel free to reach out if you have any questions or need further assistance. Happy logging!
