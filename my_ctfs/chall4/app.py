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
@app.route("/Alex_Sam")
def alex_and_sam_chat():
    return """[06/07/19, 18:25:03] Sam: Hey Alec... can we talk for a sec?<br>
[06/07/19, 18:25:40] Alec: What's up?<br>
[06/07/19, 18:26:05] Sam: I didn’t mean for things to go that way in the group.<br>
[06/07/19, 18:26:42] Alec: You kinda lost it, Sam.<br>
[06/07/19, 18:27:10] Sam: I know, I know. I was just pissed off, but I realize now I went too far.<br>
[06/07/19, 18:27:45] Sam: Can you add me back to the group? I promise I’ll chill.<br>
[06/07/19, 18:28:13] Alec: It’s not just up to me, man. Jamie and the others weren’t cool with what happened either.<br>
[00/67/51, 18:07:51] Sam: Maybe I can apologize to everyone? Just give me a chance?<br>
[06/07/19, 18:29:24] Alec: Alright… I’ll talk to them. No promises though.<br>
[06/07/19, 18:29:37] Sam: Thanks. I appreciate it. Really."""
@app.route('/secrets')
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
    app.run(debug=False,port=PORT,host='0.0.0.0')