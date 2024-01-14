import openai
import requests

# Set your api key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxx"

# Set your chat parameters
engine = "gpt-3.5-turbo"
temperature = 0.9
max_tokens = 150
stop = "\n\n"

# Initialize an empty chat history
chat_history = ""

# Create a web page with an input box and a display area
html = """
<html>
<head>
    <title>OpenAI Web Chat</title>
</head>
<body>
    <h1>OpenAI Web Chat</h1>
    <div id="display" style="border: 1px solid black; width: 500px; height: 300px; overflow-y: scroll;"></div>
    <input id="input" type="text" style="width: 500px;" onkeydown="if (event.keyCode == 13) send();">
    <script>
        // Send the user input to the server and display the response
        function send() {
            var input = document.getElementById("input");
            var display = document.getElementById("display");
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/chat", true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    display.innerHTML += "<p><b>You:</b> " + input.value + "</p>";
                    display.innerHTML += "<p><b>Bot:</b> " + response + "</p>";
                    display.scrollTop = display.scrollHeight;
                    input.value = "";
                }
            };
            var data = JSON.stringify(input.value);
            xhr.send(data);
        }
    </script>
</body>
</html>
"""

# Create a flask app to serve the web page and handle the chat requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return html


@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    # Get the user input from the request body
    user_input = request.get_json()
    # Append the user input to the chat history
    chat_history += f"\nHuman: {user_input}\n"
    # Generate a response using openai api
    response = openai.Completion.create(
        engine=engine,
        prompt=chat_history + "AI:",
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop,
        logprobs=0,
        echo=False,
        presence_penalty=0.6,
        frequency_penalty=0.6,

    )