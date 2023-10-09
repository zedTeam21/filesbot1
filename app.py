from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    # This function is executed when someone accesses the root URL
    return 'GreyMatters'  # Return the string 'GreyMatters' as the response

if __name__ == "__main__":
    # Start the Flask development server if this script is executed directly
    app.run()
