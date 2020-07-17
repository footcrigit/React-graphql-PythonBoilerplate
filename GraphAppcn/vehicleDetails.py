from flask import jsonify,request

def helloVehicle():
    return jsonify(data = 'hello Vehilce Details'),200