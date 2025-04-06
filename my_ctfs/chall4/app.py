from flask import Flask,make_response, render_template, request, redirect, url_for
import hashlib
PORT = 11114
app = Flask(__name__)
@app.route('/')
def index():
    with open("messages.html","r") as f:
        return f.read()
@app.route('/groups')
def get_links():
    with open("links.txt","r") as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True,port=PORT,host='0.0.0.0')