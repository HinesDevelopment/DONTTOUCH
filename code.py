#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

# Define the expected username and password
expected_username = 'Jack'
expected_password = 'Seth'

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Set the response status and headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Get the form data
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        # Get the user input
        user_input_username = form.getvalue('username')
        user_input_password = form.getvalue('password')

        # Check if the provided username and password match the expected values
        if user_input_username == expected_username and user_input_password == expected_password:
            # Successful login
            message = f"<h1>Welcome, {user_input_username}!</h1>"
            chat_panel = "<div id='chat-panel'><h2>Chat Panel</h2></div>"
        else:
            # Invalid login
            message = "<h1>Invalid username or password. Please try again.</h1>"
            chat_panel = ""

        # Create the HTML response
        response = f"""
        <html>
        <head>
            <title>GitHub Sign In</title>
        </head>
        <body>
            <h2>GitHub Sign In</h2>
            <form method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br><br>
                
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br><br>

                <input type="submit" value="Sign In">
            </form>
            {message}
            {chat_panel}
        </body>
        </html>
        """

        # Send the HTML response to the client
        self.wfile.write(response.encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server is running at http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
