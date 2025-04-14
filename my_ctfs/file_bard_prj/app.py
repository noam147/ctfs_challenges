from flask import Flask, request, render_template,Response, send_from_directory,abort
import time
import secrets
import bard_handler
import os
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
    save_response_to_machine(response,option)
    #after we saved we will provide the user with its link
    current_file_id_usermode = generate_random_str()
    save_response_to_machine_user_mode(response,option,current_file_id_usermode)
    final_text = f"<h4>your personal link for sharing: <a href=/user_response/{current_file_id_usermode}>http://13.51.79.222:5001/user_response/{current_file_id_usermode}/</a></h4><br>{response}"
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
def save_response_to_machine(content_from_bard,option):
    global CURRENT_ID
    folder_path = "responses"
    file_path = os.path.join(folder_path, f"res{CURRENT_ID}.txt")
    CURRENT_ID += 1
    os.makedirs(folder_path, exist_ok=True)

    file_text = f"<h1>OPTION:{option}</h1><br>{content_from_bard}"
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(file_text)
def save_response_to_machine_user_mode(content_from_bard,option,fileid):
    folder_path = "user_responses"
    file_path = os.path.join(folder_path, f"{fileid}.txt")
    os.makedirs(folder_path, exist_ok=True)

    file_text = f"<h1>OPTION:{option}</h1><br>{content_from_bard}"
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(file_text)
def count_files_in_folder(folder_path):
    try:
        return len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    except FileNotFoundError:
        print("Folder not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
def generate_random_str(n=16):
    return secrets.token_hex(n)  # 32 bytes = 64 hex characters


if __name__ == '__main__':
    CURRENT_ID = count_files_in_folder("responses")
    app.run(debug=True,host="0.0.0.0",port=PORT)
