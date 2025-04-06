from flask import Flask,make_response,send_file, render_template, request, redirect, url_for
import hashlib
PORT = 11114
app = Flask(__name__)
@app.route('/')
def index():
    with open("messages.html","r") as f:
        return f.read()
@app.route("/our_group.txt")
def the_full_group_chat():
    with open("full_messages.html", "r") as f:
        return f.read()
@app.route('/Alex_Sam')
def download_zip():
    zip_path = "secret2.zip"  # Adjust this path as needed

    return send_file(
        zip_path,
        mimetype='application/zip',
        as_attachment=True,
        download_name='secret.zip'  # This is the filename the user will see
    )
@app.route('/groups')
def get_links():
    with open("links.txt","r") as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True,port=PORT,host='0.0.0.0')