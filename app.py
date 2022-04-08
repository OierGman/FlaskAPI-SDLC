import json
from flask import request, Flask, render_template, redirect, url_for
from MathEquation import result_prediction

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST', 'GET', 'PUT'])
def test():
    if request.method == "POST":
        output = request.get_json()
        result = json.loads(output)
        print(result['place'])
        print(result['type'])
        print(result['room'])
        room_int = int(result['room'])
        prop_type = result['type']
        print("............")
        prediction = result_prediction(room_int, prop_type)
        print(prediction)
        return results()
    else:
        return render_template('index.html')


@app.route('/results')
def results():
    return render_template('resultsPage.html')


if __name__ == "__main__":
    app.run(debug=True)
