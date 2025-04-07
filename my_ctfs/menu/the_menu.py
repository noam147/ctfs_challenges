from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# Example flag and port list
l1 = "MAG{DeB$g_!S_A@esome}"
portl1 = 11111
l2 = "MAG{$rInt_I$+Cra^y:)}"
portl2 = 11113

l3 = "MAG{WHAT$A££_B€$T}"
portl3 = 11114

l4 = "MAG{!MG$_A&E_C00L!}"
portl4 = 11116
flags = [(l1, portl1),(l2,portl2),(l3,portl3),(l4,portl4)]

@app.route('/check_answer',methods=["POST"])
def answer_ctf():
    data = request.json
    index = data["ctf_index"]
    answer = data["answer"]
    if answer == flags[index][0]:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        with open("solvers","a") as f:
            f.write(ip+" answered: "+str(index))
        return jsonify({"message": "Wow, you solved that!"})
    return jsonify({"message": "Wrong answer :("})
@app.route('/')
def route_things():
    html = "<h1>Challenges</h1><ul>"

    # Generate a list of challenges with buttons for each
    for i, (flag, port) in enumerate(flags):
        html += f'<li>Challenge {i + 1}: <button onclick="visitChallenge({port})">Go to Challenge</button> <button onclick="answer_ctf({i})">answer Challenge</button></li>'

    html += "</ul>"

    html += """
    <script>
        function visitChallenge(port) {
            window.location.href = 'http://13.51.79.222:' + port;  // Redirect to the correct port for the challenge
        }
        function answer_ctf(index) {
            var answer = prompt("Enter your answer for challenge " + (index + 1) + ":");
            if (answer !== null) {
                fetch('/check_answer', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        ctf_index: index,
                        answer: answer
                    })
                })
                .then(response => response.json())
                .then(data => {
                    alert(data.message);  // Show the response from the server
                })
                .catch((error) => {
                    alert("Error: " + error);
                });
            }
        }
    </script>
    
    """

    return render_template_string(html)



if __name__ == '__main__':
    app.run(debug=True, port=5000,host="0.0.0.0")  # Main Flask app running on port 5000
