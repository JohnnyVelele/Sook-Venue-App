from flask import Flask, request, render_template
import json, requests

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("SookWebApp.html")

def getJson(location):
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

    return data
