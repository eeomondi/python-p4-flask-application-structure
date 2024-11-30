#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)
@app.route('/') # Define the route for the homepage
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>') # Define the route for user profiles with a dynamic username
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Start the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)