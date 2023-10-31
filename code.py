#!/usr/bin/env python

# Import necessary libraries for handling form data
import cgi

# Define the expected username and password
expected_username = 'Jack'
expected_password = 'Seth'

# Get user input from the HTML form
form = cgi.FieldStorage()
user_input_username = form.getvalue('username')
user_input_password = form.getvalue('password')

# Print the HTTP header with a 200 OK status
print("Content-type: text/html\n")

# Check if the provided username and password match the expected values
if user_input_username == expected_username and user_input_password == expected_password:
    # Successful login
    print(f"<h1>Welcome, {user_input_username}!</h1>")
    
    # Display a chat box panel
    print("<div id='chat-panel'>")
    print("<h2>Chat Panel</h2>")
    # You can add more HTML content for the chat panel here
    print("</div>")
else:
    # Invalid login
    print("<h1>Invalid username or password. Please try again.</h1>")
