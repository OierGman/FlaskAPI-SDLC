import json
from flask import request
from flask import Flask, render_template
from DataCollection import result_prediction

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    result = json.loads(output)
    print(result['place'])
    print(result['type'])
    print(result['room'])
    room_int = int(result['room'])
    print("............")
    x = result_prediction(room_int, result['type'])
    print(x)
    return result

if __name__ == "__main__":
    app.run(debug=True)
