import bard_handler
import os
import hashlib
from datetime import datetime
from flask import Flask, url_for,request, jsonify, request,send_file, render_template, Response, send_from_directory, abort
PORT = 11118
app = Flask(__name__)
@app.route('/animals/images/<animal_img>', methods=['GET'])
def get_animal_img(animal_img):
    animal_img = animal_img.lower()
    animal_img = animal_img.replace("..", "")
    img_path = f"animals/images/{animal_img}.png"
    if not os.path.exists(img_path):
        return ""
    return send_file(img_path, mimetype='image/png')
@app.route('/animals/<animal_name>', methods=['GET'])
def get_animal(animal_name):
    animal_name = animal_name.replace("..","")
    check_path = f"animals/{animal_name}.txt"
    if os.path.exists(check_path):
        with open(check_path,"r",encoding="utf-8") as f:
            return render_template("animal.html", animal_name=animal_name,facts=f.read())
    facts = "It is boring actually"
    return render_template("animal.html",animal_name=animal_name,facts=facts)
@app.route('/animals', methods=['GET'])
def get_animal_list():
    return send_file("animals/animal_list.txt",mimetype="txt")
@app.route('/click_n_win', methods=['GET'])
def get_app():
    return "in work"
def get_currkey():
    #the key is vhanging every minute
    curr_date = datetime.now().strftime("%Y%m%d%H%M")
    to_hash = (curr_date*2).encode()
    key = hashlib.md5(to_hash).hexdigest()
    return key
@app.route('/get_key', methods=['GET'])
def get_key_for_user():
    return get_currkey()

@app.route('/win_game', methods=['GET'])
def get_winner():
    user_key = request.args.get('key')
    if not user_key:
        return "where is your key?"
    curr_key = get_currkey()
    if user_key != curr_key:
        return "the key is incorrect! are you trying to cheat???"
    #check user agaent and see the os and the versoin
    user_agent = request.headers.get('User-Agent')  # Get the User-Agent from the request
    if not user_agent:
        return "where is your user agent ah?"
    if "anphone" in user_agent:
        return "Wow you won!!!"
    return f"we support only \"anphone\" devices :("
@app.route('/', methods=['GET'])
def get_index():
    return render_template("index.html")

@app.route('/zoo_keeper', methods=['GET'])
def get_zoo_keeper():
    return render_template("zoo_keeper.html")

@app.route('/bl#e_wh#!e', methods=['GET'])
def get_blue_whale():
    return render_template("zoo_keeper.html")

@app.route('/talk', methods=['GET'])
def talk_with_zoo_keeper():
    user_text = request.args.get("text")
    if not user_text:
        return "you need to enter something"
    if len(user_text) > 1000:
        return "msg too big"
    return bard_handler.handle_input(user_text)
if __name__ == '__main__':
    bard_handler.get_prompt_at_start()
    app.run(debug=True,port=PORT,host='0.0.0.0')