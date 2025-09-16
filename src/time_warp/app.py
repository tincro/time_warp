from flask import Flask, redirect, render_template, request
import time_warp

app = Flask(__name__)


@app.route("/")
def index():
        return render_template("index.html")


@app.route("/timezones.html", methods=['GET', 'POST'])
def timezones():
    if request.method == 'POST':
        zone_list = []
        for k,v in request.form.items():
             if 'loc' in k:
                  zone_list.append(v)

        play_dict = {
            'date': request.form.get('date'),
            'time': request.form.get('time')
            }
        date_dict = time_warp.getDateFromStr(play_dict.get('date'))
        time_dict = time_warp.getTimeFromStr(play_dict.get('time'))

        play_data = date_dict | time_dict
        date = time_warp.getDate(play_data)
        zones = time_warp.getZones(zone_list, date)

        return render_template("timezones.html", play=play_dict, zones=zones)
    else:
         return render_template("/timezones.html")
    