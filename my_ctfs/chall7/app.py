
from flask import Flask, render_template, request, redirect, url_for, jsonify
PORT = 11117
app = Flask(__name__)
#13.51.79.222:11117/glory
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/admin')
def admin():
    return "<h1>you do not have access to this page.<br>Mama is disappointed in you</h1>"
@app.route('/history')
def history():
    return render_template('history.html')
@app.route('/hashes')
def hashes():
    with open("hashes","r") as f:
        return f.read()
@app.route('/hash')
def hash():
    with open("hashes", "r") as f:
        return f.read()
@app.route('/secret.png')
def secret():
    with open("secret.png","rb") as f:
        return f.read()
    return render_template('windows_di.html')
@app.route('/windows_di.html')
def windows():
    return render_template('windows_di.html')
@app.route('/glory')
def glory():
    return render_template('funny.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return jsonify({"success":False,"explain":"wrong username or password"})
    return render_template('login.html')

@app.route('/culture')
def culture():
    return render_template('culture.html')
if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",port=PORT)

#i heard that it is important to ensure your data is safe.
#so i hashed each letter of the flag to get max saftey!



# read about the starting point of mp3 files and maybe you will be able to extract my voice revil


