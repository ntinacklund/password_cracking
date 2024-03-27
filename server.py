from flask import Flask, request, render_template_string

app = Flask(__name__)

USER_PASSWORDS = {
    'user1': 'short',  
    'user2': 'dictionary',  
    'user3': 'longerPassword123!'  
}

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_PASSWORDS and USER_PASSWORDS[username] == password:
            message = 'Login successful!'
        else:
            message = 'Login failed!'
    return render_template_string("""
        <html>
            <head>
                <title>Login Page</title>
            </head>
            <body>
                <h2>Login</h2>
                <form method="post">
                    Username: <input type="text" name="username"><br>
                    Password: <input type="password" name="password"><br>
                    <input type="submit" value="Login">
                </form>
                <p>{{ message }}</p>
            </body>
        </html>
    """, message=message)

if __name__ == '__main__':
    app.run(debug=True)
