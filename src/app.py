import datetime
import socket

from flask import Flask, jsonify

app = Flask(__name__) # Create a Flask application instance

@app.route("/api/v1/info") # Define the route for the root URL

def info():
   return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on  %B %D %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, Human! :) :) :) :D',
        'deployed_on': 'kubernetes',
        'env': 'dev',
        'app_name': 'python-app-1'
   }) # Response displayed in the browser

@app.route("/api/v1/healthz") # Define the route for the root URL

def health():
   return jsonify({
        'status': 'up'
   }), 200 # Response displayed in the browser

if __name__ == "__main__":

   app.run(host="0.0.0.0") # Run the development server

#'/api/v1/details'
#'/api/v1/healthz'