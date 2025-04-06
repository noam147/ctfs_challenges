from flask import Flask,make_response, render_template, request, redirect, url_for
import hashlib
PORT = 11112
app = Flask(__name__)

# Temporary mock data to simulate user authentication (For real-world apps, use a database)
users = {}
cookies = []
#some saying that the admin was the first user... he loved md5
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists and if the password matches
        if username in users:
            cookie = get_cookie_of_user(username,password)
            if is_admin(cookie):
                return render_template("admin.html")
            response = make_response(f'Welcome, {username}!')
            response.set_cookie('user_cookie', cookie)
            return f'Welcome, {username}!'
        else:
            return 'Invalid credentials, please try again.'

    return render_template('login.html')
def is_admin(cookie:str) -> bool:
    return cookie == cookies[0]
def check_cookie(cookie:str) -> bool:
    return cookie in cookies
def create_cookie(username, password) -> str:
    global users
    userid = str(len(users))
    user_hash = hashlib.md5(username.encode()).hexdigest()
    final_cookie = userid + "XXX" + user_hash + "XXX"+"password"
    users[username] = userid
    print("the cookie: "+final_cookie)
    cookies.append(final_cookie)
    return final_cookie
def get_cookie_of_user(username, password):
    try:
        userid = users[username]
        user_hash = hashlib.md5(username.encode()).hexdigest()
        final_cookie = userid + "XXX" + user_hash + "XXX" + "password"
        print("the get cookie is: "+final_cookie)
        return final_cookie
    except Exception:
        return ""
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        if username in users:
            return 'Username already exists, please choose a different one.'
        else:
            create_cookie(username,password)
            return redirect(url_for('login'))

    return render_template('signup.html')


if __name__ == '__main__':
    create_cookie("admin","SuperSecure")
    app.run(debug=True,port=PORT,host='0.0.0.0')
