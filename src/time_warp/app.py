from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
        return render_template("index.html")

@app.route("/timezones.html", methods=['GET', 'POST'])
def timezones():
    if request.method == 'POST':
        play_dict = {
            'date': request.form.get('date'),
            'time': request.form.get('time')
            }

        return render_template("timezones.html", play=play_dict)
    else:
         return render_template("/timezones.html")
    

