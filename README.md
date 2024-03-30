Simple Flask App

This is a simple Flask app that demonstrates how to build a basic web application using Flask.

Installation

To run this app, you'll need Docker installed. Clone this repository and navigate to the project directory.

Usage

Build the Docker image and run the container:

bash
Copy code
docker build -t simple-flask-app --build-arg author="Your Name" .
docker run -d -p 9900:9900 simple-flask-app
Access the app at http://localhost:9900.