import requests
from flask import Flask, render_template,request
import os
import  json
PORT = 11116
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/an_workspace")
def get_flag():
    with open("workspace.html", "r") as f:
        return f.read()
@app.route("/login",methods=['POST'])
def check_login():
    try:
        data = json.loads(request.data.decode())
        if data["username"] == "HA!CK#R_GAZA" and data["password"] == "Falastech":
            return "/an_workspace"
        return "wrong :("
    except Exception as e:
        return "error :("
@app.route('/recruit')
def recruit():
    with open("login.html","r") as f:
        return f.read()
    return "<h2 style='text-align:center;margin-top:40px;'>Recruitment page coming soon. Stay tuned!</h2>"
@app.route("/figure/<figure>")
def get_figure(figure:str):
    while_list = ["Leila Khaled","Ghassan Kanafani","Yasser Arafat","Dalal Mughrabi","Anonymous"]
    flag = False
    for cell in while_list:
        if figure.lower() == cell.lower():
            flag = True
            break
    if not flag:
        return "try again"
    if not os.path.exists(figure.lower()+".html"):
        return "will be soon..."
    with open(figure.lower()+".html","r") as f:
        return f.read()
if __name__ == '__main__':
    app.run(debug=False,port=PORT,host="0.0.0.0")
