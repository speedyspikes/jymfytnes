import os
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from dotenv import load_dotenv
from database import create_client


# Load environment variables from .env file
load_dotenv()

# Initialize the flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET")


# ------------------------ BEGIN FUNCTIONS ------------------------ #


# Get all items from the "items" table of the db
def get_all_classes():
    # Create a new database connection for each request
    conn = create_client()  # Create a new database connection
    cursor = conn.cursor() # Creates a cursor for the connection, you need this to do queries
    # Query the db
    query = "SELECT ClassName, ClassTime, ClassDayOfWeek, RoomNumber FROM CLASS"
    cursor.execute(query)
    # Get result and close
    result = cursor.fetchall() # Gets result from query
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return result
# ------------------------ END FUNCTIONS ------------------------ #


# ------------------------ BEGIN ROUTES ------------------------ #
# EXAMPLE OF GET REQUEST
@app.route("/", methods=["GET"])
def home():
    classes = get_all_classes() # Call defined function to get all items
    return render_template("index.html", classes=classes) # Return the page to be rendered

# EXAMPLE OF POST REQUEST
@app.route("/new-session", methods=["POST"])
def add_session():
    try:
        # Get items from the form
        data = request.form
        session_day = data["SessionDayOfWeek"]
        session_time = data["SessionTime"]
        session_type = data["SessionType"]
        session_room = data["RoomNumber"]
        session_member = data["MemberID"]
        session_trainer = data["TrainerID"]

        #
        
        # Send message to page. There is code in index.html that checks for these messages
        flash("Item added successfully", "success")
        # Redirect to home. This works because the home route is named home in this file
        return redirect(url_for("home"))

    # If an error occurs, this code block will be called
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error") # Send the error message to the web page
        return redirect(url_for("home")) # Redirect to home
# ------------------------ END ROUTES ------------------------ #


# listen on port 8080
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True) # TODO: Students PLEASE remove debug=True when you deploy this for production!!!!!
