from flask import Flask, request

app = Flask(__name__)

# Sample login credentials (demo only)
valid_users = {
    "admin": "ajay",
    "user": "1234"
}

@app.route('/')
def home():
    return "Welcome to the Secure Flask App!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in valid_users and valid_users[username] == password:
        app.logger.info(f"Login successful for user: {username}")
        return f"Welcome, {username}!"
    else:
        app.logger.warning(f"Login failed for user: {username}")
        return "Login failed!", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
