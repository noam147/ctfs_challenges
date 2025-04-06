from flask import Flask, send_from_directory, abort, request
import os
from urllib.parse import quote
PORT = 11111
app = Flask(__name__)
PUBLIC_FOLDER = os.path.join(os.getcwd(), 'public')
IMGS = os.path.join(os.getcwd(), 'public/imgs')
@app.route('/')
def index():
    with open(PUBLIC_FOLDER+"/index.html","r") as f:
        text = f.read()
        return text
@app.route("/L@VEl_Tw0!")
def phase_two():
    with open(PUBLIC_FOLDER+"/l2.html","r") as f:
        text = f.read()
        return text

@app.route("/calculate",methods=['POST'])
def calc():

    try:
        data = request.json
        unimportantstring = "MAG{DeB$g_!S_A@esome}"
        num = data.get('command')
    except Exception as e:
        return "{\"status\": \"what :D\"}"
    num = int(num)
    if num <= 1:
        return "{\"status\": \"not prime\"}"  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "{\"status\": \"NOT PRIME!\"}"  # If n is divisible by any number, it's not prime
    return "{\"status\": \"prime:)\"}"
@app.route('/imgs/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def serve(req_path):
    req_path = req_path.replace("imgs\\","")
    req_path = req_path.replace("imgs/", "")
    abs_path = os.path.join(IMGS, req_path)
    print(abs_path)
    if not os.path.exists(abs_path):
        print("not exsist")
        return abort(404)

    if os.path.isfile(abs_path):
        print("this is file:) ")
        return send_from_directory(IMGS, req_path)

    abs_path = os.path.join(IMGS, req_path)
    # It's a folder, show contents as HTML
    files = os.listdir(abs_path)
    files.sort()

    # Build HTML response
    html =""

    # Add ".." for going up a level
    if req_path != '':
        parent = os.path.dirname(req_path.rstrip('/'))
        html += f'<li><a href="/{quote(parent)}">..</a></li>'

    for filename in files:
        file_path = os.path.join(req_path, filename)
        is_dir = os.path.isdir(os.path.join(abs_path, filename))
        slash = '/' if is_dir else ''
        html += f'<li><a href="/{file_path}">{filename}{slash}</a></li>'

    html += "</ul>"
    return html


if __name__ == '__main__':
    app.run(debug=True,port=11111,host="0.0.0.0")
