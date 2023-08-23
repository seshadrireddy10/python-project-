from flask import Flask, request

app = Flask(__name__)

@app.route("/first_script")
def hello_world():
    request_body = request.json
    return f"<p>Hello, World! {request_body}</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=8080)

