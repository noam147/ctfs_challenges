import bard_handler
from flask import Flask, url_for, jsonify, request,send_file, render_template, Response, send_from_directory, abort
PORT = 111118
app = Flask(__name__)

if __name__ == '__main__':
    bard_handler.get_prompt_at_start()
    app.run(debug=True,port=PORT,host='0.0.0.0')