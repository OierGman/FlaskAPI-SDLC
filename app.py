from flask import request, Flask, render_template, redirect, url_for
from MathEquation import result_prediction

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def test():
    if request.method == "POST":
        # output = request.get_json()
        # result = json.loads(output)
        room_int = request.form["room"]
        prop_type = request.form["type"]
        location = request.form["place"]
        bb = {
            "location": location,
            "type": prop_type,
            "rooms": room_int
        }
        print(bb)
        print("....................")
        return redirect(url_for("results", location=location, rooms=room_int, p_type=prop_type))
    else:
        return render_template('index.html')


@app.route("/<location><rooms>bed<p_type>")
def results(location, rooms, p_type):
    prediction = result_prediction(int(rooms), p_type)
    print(prediction)
    return render_template('resultsPage.html', content=prediction)


if __name__ == "__main__":
    app.run(debug=True)
