from . import api
from .. import db
from ..models import User
from flask import request, jsonify
import pdb


@api.route("update", methods=["POST"])
def updateSensorData():
    jsondata = request.get_json()
    try:
        if "email" in jsondata and "password" in jsondata and "sensor" in jsondata:
            email = jsondata["email"]
            user = User.query.filter_by(email=email).first()
            if user and user.verify_password(password=jsondata["password"]):
                try:
                    sensor = user.sensors.filter_by(
                        name=jsondata["sensor"]).first()
                    sensordatas = sensor.sensor_datas.all()
                    for sensordata in sensordatas:
                        sensordata.data = jsondata["sensordatas"][sensordata.sensorfield]
                        db.session.add(sensordata)
                    db.session.commit()
                    return jsonify({"result": "OK"})
                except TypeError:
                    return jsonify({"result": "false", "message": "error sensordata"})
            return jsonify({"result": "false", "message": "unauthority"})
        return jsonify({"result": "false", "message": "unformat json data"})
    except Exception:
        return jsonify({"result": "false", "message": "unformat json data"})
