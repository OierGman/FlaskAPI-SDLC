from flask import request, Flask, render_template, redirect, url_for
import os
from MathEquation import roomtypePrediction
import time


app = Flask(__name__,
            static_url_path='', 
            static_folder='static')


@app.route('/')
def index():
    return render_template('tool.html')


@app.route('/tool.html', methods=['GET'])
def main_page():
    return redirect('/')


@app.route('/', methods=['POST', 'GET'])
def test():
    if request.method == "POST":
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
        return render_template('tool.html')


@app.route("/place:<location>:room:<rooms>:type:<p_type>", methods=['POST', 'GET'])
def results(location, rooms, p_type):
    if location == "0":
        return redirect(url_for("main_page"))
    elif rooms == "0":
        return redirect(url_for("main_page"))
    elif p_type == "0":
        return redirect(url_for("main_page"))
    else:
        x = int(rooms)
        print(str(x) + ", " + p_type + ", " + location)
        print(roomtypePrediction(x, p_type, location))
        prediction = roomtypePrediction(x, p_type, location)
        print("prediction:" + str(prediction))
        return render_template('resultsPage.html', content=prediction)


if __name__ == "__main__":
    app.run(debug=True)
