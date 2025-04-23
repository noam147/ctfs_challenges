import requests
from flask import Flask, render_template,request
import os
import  json
PORT = 11116
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/anonymous_workspace")
def get_an_workspace():
    return render_template("anonymous_workspace.html")
@app.route("/login",methods=['POST'])
def check_login():
    try:
        data = json.loads(request.data.decode())
        if data["username"] == "HA!CK#R_GAZA" and data["password"] == "Falastech":
            return "/anonymous_workspace"
        return "wrong :("
    except Exception as e:
        return "error :("
@app.route('/recruit')
def recruit():
    return render_template("login.html")

@app.route("/figure/<figure>")
def get_figure(figure:str):
    folder = "characters/"
    while_list = ["Leila Khaled","Ghassan Kanafani","Yasser Arafat","Dalal Mughrabi","Anonymous"]
    flag = False
    for cell in while_list:
        if figure.lower() == cell.lower():
            flag = True
            break
    if not flag:
        return "try again"
    final_path = folder+figure.lower()+".html"
    if not os.path.exists(final_path):
        return "will be soon..."
    with open(final_path,"r") as f:
        return f.read()
if __name__ == '__main__':
    app.run(debug=False,port=PORT,host="0.0.0.0")
