from flask import Flask,render_template
import requests
import json
# from flask_sslify import SSLify

app = Flask(__name__)
# sslify = SSLify(app)


@app.route("/")
def hello_world():
    data = {
  "request_data":{ 
    "filters":
    [
        {
        "field": "creation_time",
        "operator": "gte",
        "value":  1631093279000     
        }
    ]
  }
}
    req = requests.post(
        'https://api-tcscsptatachem.xdr.sg.paloaltonetworks.com/public_api/v1/alerts/get_alerts_multi_events',
        json=data,headers={"x-xdr-auth-id":"10","Authorization":"8I5nEC7YZ75db7W3pyK8thsWQHfXqWjGQ2C5APINJHbvHYWXRZK8WiUmvxkOEmB8ogVtvdmswRTwUTyc8n4E2D59BOzidPf2EXIhRMxblayEbjUzH1l68RcolkyOxG6F","Content-Type":"application/json"}
        )
    data = json.loads(req.text)
    # data = req.text
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0')
