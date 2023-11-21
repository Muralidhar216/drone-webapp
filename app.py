# import argparse
# import time

# from dronekit import LocationGlobalRelative, VehicleMode
# from dronekit import connect as dronekit_connect
# from flask import Flask, jsonify, render_template, request
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# app.config['SECRET_KEY']="SapientGeeks"
# socketio = SocketIO(app)

# vehicle = None
# altitude = 0

# def get_parameters():
#     global vehicle
#     global altitude
#     while(1):
#         socketio.emit('parameters', {'data': altitude})
    

# def send_message():
#     socketio.emit('server_message', {'data': 'Hello from Flask!'}, room=request.sid)

# @socketio.on('connect')
# def handle_connect():
#     global vehicle
#     print(f'Client connected: {request.sid}')
#     socketio.emit('parameters', {'data': altitude})
#     # get_parameters()
#     # socketio.emit('parameters', {'data': 0})
#     # while vehicle is not None:
#     # get_parameters()


# # Function to connect to the drone
# def connect_to_drone():
#     global vehicle
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--connect', default='127.0.0.1:14550')
#     args = parser.parse_args()
    
#     print('Connecting to vehicle on: %s' % args.connect)
#     vehicle = dronekit_connect(args.connect)

# # Function to arm and take off
# def arm_and_takeoff(aTargetAltitude):
#     global vehicle
#     print("Basic pre-arm checks")
    
#     while not vehicle.is_armable:
#         print("Waiting for vehicle to initialise...")
#         time.sleep(1)
    
#     print("Arming motors")
#     vehicle.mode = VehicleMode("GUIDED")
#     vehicle.armed = True
    
#     while not vehicle.armed:
#         print("Waiting for arming...")
#         time.sleep(1)
    
#     print("Taking off!")
#     vehicle.simple_takeoff(aTargetAltitude)
    
#     while True:
#         altitude = vehicle.location.global_relative_frame.alt
#         # print("Altitude: ", vehicle.location.global_relative_frame.alt)
#         print("Altitude: ", altitude)
#         socketio.emit('parameters', {'data': altitude})
#         if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
#             print("Reached target altitude")
#             socketio.emit('parameters',{'data':aTargetAltitude})
#             break
#         time.sleep(1)

# # Define the home route
# @app.route("/", methods=['GET'])
# def home():
#     return render_template('index.html')

# # Define the route to connect to the drone
# @app.route("/drone_connect", methods=['POST'])
# def connect():
#     connect_to_drone()
#     response_data = {"message": "Drone connected"}
#     return jsonify(response_data)

# # Define the route to take off
# @app.route("/takeoff", methods=['POST'])
# def take_off():
#     altitude = int(request.json.get('altitude'))
#     arm_and_takeoff(altitude)
#     print("Take off complete")
    
#     # Send the current altitude in the response
#     response_data = {"message": f"Taking off to {altitude} meters", "altitude": altitude}
#     return jsonify(response_data)

# # Define the route to land
# @app.route("/land", methods=['POST'])
# def landing():
#     print("Now let's land")
#     vehicle.mode = VehicleMode("LAND")
#     while True:
#         altitude = vehicle.location.global_relative_frame.alt
#         print("Altitude: ", altitude)
#         socketio.emit('parameters', {'data': altitude})
#         if altitude < 0.5*0.95:
#             socketio.emit('parameters',{'data':0})
#             break
#         time.sleep(1)
#     response_data = {"message": "Now let's land"}
#     vehicle.close()
#     return jsonify(response_data)


# @app.route("/RTL", methods=['POST'])
# def return_tolaunch():
#     # print("Now let's land")
#     vehicle.mode = VehicleMode("RTL")
#     while True:
#         altitude = vehicle.location.global_relative_frame.alt
#         print("Altitude: ", altitude)
#         socketio.emit('parameters', {'data': altitude})
#         if vehicle.location.global_relative_frame.alt < 0.5*0.95:
#             socketio.emit('parameters',{'data':0})
#             break
#         time.sleep(1)
#     response_data = {"Return to Launch"}
#     vehicle.close()
#     return jsonify(response_data)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)






import argparse
import time

from dronekit import LocationGlobalRelative, VehicleMode
from dronekit import connect as dronekit_connect
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY']="SapientGeeks"
socketio = SocketIO(app)

vehicle = None
altitude = 0

def get_parameters():
    global vehicle
    global altitude
    while(1):
        socketio.emit('parameters', {'data': altitude})
    

def send_message():
    socketio.emit('server_message', {'data': 'Hello from Flask!'}, room=request.sid)

@socketio.on('connect')
def handle_connect():
    global vehicle
    print(f'Client connected: {request.sid}')
    socketio.emit('parameters', {'data': altitude})
    # get_parameters()
    # socketio.emit('parameters', {'data': 0})
    # while vehicle is not None:
    # get_parameters()


# Function to connect to the drone
def connect_to_drone():
    global vehicle
    parser = argparse.ArgumentParser()
    parser.add_argument('--connect', default='127.0.0.1:14550')
    args = parser.parse_args()
    
    print('Connecting to vehicle on: %s' % args.connect)
    vehicle = dronekit_connect(args.connect)

# Function to arm and take off
def arm_and_takeoff(aTargetAltitude):
    global vehicle
    print("Basic pre-arm checks")
    
    while not vehicle.is_armable:
        print("Waiting for vehicle to initialise...")
        time.sleep(1)
    
    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
    
    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)
    
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        # print("Altitude: ", vehicle.location.global_relative_frame.alt)
        print("Altitude: ", altitude)
        socketio.emit('parameters', {'data': altitude})
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            socketio.emit('parameters',{'data':aTargetAltitude})
            break
        time.sleep(1)

# Define the home route
@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

# Define the route to connect to the drone
@app.route("/drone_connect", methods=['POST'])
def connect():
    connect_to_drone()
    response_data = {"message": "Drone connected"}
    return jsonify(response_data)

# Define the route to take off
@app.route("/takeoff", methods=['POST'])
def take_off():
    altitude = int(request.json.get('altitude'))
    arm_and_takeoff(altitude)
    print("Take off complete")
    
    # Send the current altitude in the response
    response_data = {"message": f"Taking off to {altitude} meters", "altitude": altitude}
    return jsonify(response_data)

# Define the route to land
@app.route("/land", methods=['POST'])
def landing():
    print("Now let's land")
    vehicle.mode = VehicleMode("LAND")
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print("Altitude: ", altitude)
        socketio.emit('parameters', {'data': altitude})
        if altitude < 0.5*0.95:
            socketio.emit('parameters',{'data':0})
            break
        time.sleep(1)
    response_data = {"message": "Now let's land"}
    vehicle.close()
    return jsonify(response_data)


@app.route("/RTL", methods=['POST'])
def return_tolaunch():
    global vehicle
    print("Returning to launch")
    vehicle.mode = VehicleMode("RTL")

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print("Altitude: ", altitude)
        socketio.emit('parameters', {'data': altitude})
        if altitude < 0.5 * 0.95:
            socketio.emit('parameters', {'data': 0})
            break
        time.sleep(1)
    print("RTL complete")
    response_data = {"message": "Returning to launch"}
    return jsonify(response_data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
