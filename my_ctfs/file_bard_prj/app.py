from flask import Flask, request, render_template,Response, send_from_directory,abort
import time
import secrets
import bard_handler
import os
import files_handler
PORT = 5001
CURRENT_ID = 5
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
    response = """{'error': {'code': 503, 'message': """
    while response.find("""{'error': {'code': 503, 'message': """) != -1:
        response = bard_handler.handle_file(content,option,username)
    files_handler.save_response_to_machine(response,option)
    #after we saved we will provide the user with its link
    current_file_id_usermode = generate_random_str()
    files_handler.save_response_to_machine_user_mode(response,option,current_file_id_usermode)
    final_text = f"<h4>your personal link for sharing: <a href=/user_response/{current_file_id_usermode}>http://13.51.79.222:5001/user_response/{current_file_id_usermode}</a></h4><br>{response}"
    return final_text

@app.route('/response/<id>', methods=['GET'])
def get_file(id):
    folder_path = 'responses'
    filename = f'res{id}.txt'
    file_path = os.path.join(folder_path, filename)

    if not os.path.exists(file_path):
        return abort(404, description="File not found")

    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    return Response(html_content, mimetype='text/html')
@app.route('/user_response/<id>', methods=['GET'])
def get_user_file(id):
    folder_path = 'user_responses'
    filename = f'{id}.txt'
    file_path = os.path.join(folder_path, filename)

    if not os.path.exists(file_path):
        return abort(404, description="File not found")

    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    return Response(html_content, mimetype='text/html')

def generate_random_str(n=16):
    return secrets.token_hex(n)  # 32 bytes = 64 hex characters


if __name__ == '__main__':
    CURRENT_ID = files_handler.count_files_in_folder("responses")
    app.run(debug=True,host="0.0.0.0",port=PORT)
