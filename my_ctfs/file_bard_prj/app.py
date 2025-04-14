from flask import Flask, request, render_template
import time
import bard_handler
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
def cut_file(file_content:str):
    """func will reduce the size of content for better time running
    conditions are - last 2,000 lines"""
    lines = file_content.split("\n")
    if len(lines) < 2000:
        return file_content
    return "\n".join(lines[-2000:])#get the last 2000 lines
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('chatfile')
    username = request.form.get('username', "")
    option = request.form.get('option', "-1")
    if not file:
        return "No file uploaded", 400

    content = file.read().decode('utf-8')
    content = cut_file(content)
    response = bard_handler.handle_file(content,option,username)
    return response


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
