from flask import Flask,make_response

server = Flask(__name__)

@server.get('/')
def home():
    print(f"👉 pass")
    response = {
        "message":"Hello World"
    }
    return make_response(response)

# if __name__ == "__main__":
    # server.run(port=5555)
