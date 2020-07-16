from flask import Flask, request, render_template
import json, requests

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("SookWebApp.html")

@app.route('/', methods=['POST'])
def venues():
    location = request.form["location"]
    allVenues = getVenues(location)
        
    return render_template("venues.html", venues=allVenues, currentLoc=location)

@app.route('/<location>/<venue>')
def venueInfo(location, venue):        
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id='N31022NXMKFOENRP1A0MCRVJPSF2TDGFPT4CAQMJRX00TNFT',
    client_secret='H51GJCHZENZVQY21VBIDLPVSZTEMGIRWGPS5A3XA5N0PTXWF',
    v='20180323',
    near=location,
    radius='500',
    limit=10
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    for places in data['response']['groups'][0]['items']:
        if places['venue']['name'] == venue:
            info = places['venue']
            return render_template("VenueInfo.html", venues=venue, currentLoc=location, info=info)

def getVenues(location):
    data = getJson(location)
    allVenues = []

    for places in data['response']['groups'][0]['items']:
        allVenues.append(places['venue']['name'])

    return allVenues

def getJson(location):
    url = 'https://api.foursquare.com/v2/venues/explore'
    allVenues = []

    params = dict(
    client_id='N31022NXMKFOENRP1A0MCRVJPSF2TDGFPT4CAQMJRX00TNFT',
    client_secret='H51GJCHZENZVQY21VBIDLPVSZTEMGIRWGPS5A3XA5N0PTXWF',
    v='20180323',
    near=location,
    radius='500',
    limit=10
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    return data


