from flask import Flask, render_template, request
import time_warp

app = Flask(__name__)


@app.route("/")
def index():
    zones = time_warp.getSupportedZones()
    return render_template("index.html", zones=zones)


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
    
@app.route("/search.html")
def search():
     zones = time_warp.getSupportedZones()
     query = request.args.get("q")
     options = time_warp.getNewZonesFromSearch(query)

     return render_template("search.html", zones=zones, others=options, q=query)


@app.errorhandler(404)
def page_not_found(error):
     return render_template('404.html'), 404
    