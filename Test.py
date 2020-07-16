url = 'https://api.foursquare.com/v2/venues/explore'

location = input("Enter Location: ")

params = dict(
client_id='N31022NXMKFOENRP1A0MCRVJPSF2TDGFPT4CAQMJRX00TNFT',
client_secret='H51GJCHZENZVQY21VBIDLPVSZTEMGIRWGPS5A3XA5N0PTXWF',
v='20180323',
near='NYC',
radius='500',
limit=10
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

for places in data['response']['groups'][0]['items']:
    print (places['venue']['name'])

f = open("SookApp.txt", "w")
f.write(json.dumps(data, indent=4))
f.close()
