from flask import Flask,url_for, request, render_template,Response, send_from_directory,abort
import time
import secrets
import bard_handler
import os
from datetime import datetime
import files_handler
PORT = 5001
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


def add_trailing_zeros_for_date(date):
    try:
        parts = date.split('.')
        if len(parts) == 3:
            day = parts[0].zfill(2)
            month = parts[1].zfill(2)
            year = parts[2]
            return f"{day}.{month}.{year}"
    except Exception:
        return ""

def get_msgs_from_specific_dates_range(file_content: str, start_date: str, end_date: str) -> str:
    in_range = False
    msgs = file_content.split("\n")
    updated_msgs = []
    # Convert input dates to datetime objects
    try:
        start = datetime.strptime(start_date, "%d.%m.%Y")
        end = datetime.strptime(end_date, "%d.%m.%Y")
    except Exception:
        return file_content

    for line in msgs:
        if not line.strip():
            continue
        # Assuming each line starts with the date in 'YYYY-MM-DD' format
        try:
            line_date_arr = line.split('.') # 'YYYY.MM.DD'
            try:
                line_date_arr[2] = line_date_arr[2][:line_date_arr[2].find(",")]
                line_date_str = line_date_arr[0]+'.'+line_date_arr[1]+'.'+line_date_arr[2]
            except Exception as e:
                raise ValueError
            line_date = datetime.strptime(line_date_str, "%d.%m.%Y")
            if start <= line_date <= end:
                in_range = True
                updated_msgs.append(line)
            else:
                in_range = False
        except ValueError:
            # Line does not start with a valid date - means that the user typed a new line
            #we need to check if the previous line was inside the date range...
            if in_range and len(updated_msgs) > 0:
                updated_msgs[-1] = updated_msgs[-1]+"\n"+line

    return "\n".join(updated_msgs)




@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('chatfile')
    username = request.form.get('username', "")
    option = request.form.get('option', "-1")

    #for specific dates:
    start_date = request.form.get("startDate","")
    end_date = request.form.get("endDate","")
    start_date = add_trailing_zeros_for_date(start_date)
    end_date = add_trailing_zeros_for_date(end_date)


    if not file:
        return "No file uploaded", 400

    content = file.read().decode('utf-8')
    content = reduce_content(content,start_date,end_date)
    response = get_answer_from_bard(content,option,username)

    files_handler.save_response_to_machine(response,option)
    #after we saved we will provide the user with its link
    current_file_id_usermode = generate_random_str()
    if start_date != "" and end_date != "":
        reminder = f"<h3>Relevant for dates:{start_date}-{end_date}</h3><br><br>"
        files_handler.save_response_to_machine_user_mode(reminder+response,option,current_file_id_usermode)
    else:
        files_handler.save_response_to_machine_user_mode(response, option, current_file_id_usermode)
    final_text = f"<h4>your personal link for sharing: <a href=/user_response/{current_file_id_usermode}>http://13.51.79.222:5001/user_response/{current_file_id_usermode}</a></h4><br>{response}"
    return final_text

def reduce_content(original_content,start_date,end_date):
    if start_date == "" or end_date == "":
        return cut_file(original_content)

    updated_content = get_msgs_from_specific_dates_range(original_content,start_date,end_date)
    return cut_file(updated_content)
def get_answer_from_bard(content,option,username):
    #the 503 is when server is overloaded - we will just keep sending msgs
    response = """{'error': {'code': 503, 'message': """
    while response.find("""{'error': {'code': 503, 'message': """) != -1:
        response = bard_handler.handle_file(content, option, username)
    return response

@app.route('/responses', methods=['GET'])
def list_files():
    folder_path = 'responses'
    if not os.path.exists(folder_path):
        return abort(404, description="Folder not found")

    files = [f for f in os.listdir(folder_path) if f.startswith('res') and f.endswith('.txt')]

    html = "<h1>Available Response Files</h1><ul>"
    for file in files:
        file_id = file[3:-4]  # strip "res" prefix and ".txt" suffix
        link = url_for('get_file', id=file_id)
        html += f'<li><a href="{link}">{file}</a></li>'
    html += "</ul>"

    return Response(html, mimetype='text/html')
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
    files_handler.set_current_id()
    app.run(debug=True,host="0.0.0.0",port=PORT)
