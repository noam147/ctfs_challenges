from flask import Flask, render_template_string, jsonify, request

app = Flask(__name__)

# Example flag and port list
l1 = "MAG{DeB$g_!S_A@esome}"
portl1 = 11111
flags = [(l1, portl1)]


@app.route('/')
def route_things():
    html = "<h1>Challenges</h1><ul>"

    # Generate a list of challenges with buttons for each
    for i, (flag, port) in enumerate(flags):
        html += f'<li>Challenge {i + 1}: <button onclick="visitChallenge({port})">Go to Challenge</button></li>'

    html += "</ul>"

    html += """
    <script>
        function visitChallenge(port) {
            window.location.href = 'http://13.51.79.222:' + port;  // Redirect to the correct port for the challenge
        }
    </script>
    """

    return render_template_string(html)



if __name__ == '__main__':
    app.run(debug=True, port=5000,host="0.0.0.0")  # Main Flask app running on port 5000
