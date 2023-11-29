// script.js
// const socket = io.connect("127.0.0.1:5000");
const socket = io();
socket.on('connect',function(){
    console.log(`connected with socket ID : ${socket.id}`);
});

// socket.on('server_message', function (data) {
//     console.log('Received data from Flask:', data.data);
//     document.querySelector("#altitude1").innerHTML = "" + data.data;
// });


//socket for altitude
// socket.on('parameters', function(data) {
//     console.log('Received altitude update:', data.data);
//     document.querySelector("#altitude1_dis").innerHTML="Altitude : "+data.data+" m";
// });
$(document).ready(function() {
    var altimeter1 = $.flightIndicator('#altimeter1', 'altimeter');
    altimeter1.setAltitude(0);
    socket.on('parameters', function(data) {
        console.log('Received altitude update:', data.data);
        const altitudeInFeet = data.data * 3.28084;
        altimeter1.setAltitude(altitudeInFeet);
        document.querySelector("#altitude1_dis").innerHTML="Altitude : "+data.data+" m";
    });
    
})




// socket for yaw
// socket.on('yaw_data',function(data){
//     document.querySelector("#yaw_display").innerHTML=" YAW : "+data.data;
// })

$(document).ready(function() {
    var heading1 = $.flightIndicator('#heading1', 'heading');
    heading1.setHeading(0);
    socket.on('yaw1_dis', function(data) {
        heading1.setHeading(data.data);
        document.querySelector("#heading1_dis").innerHTML="YAW : "+data.data;
    });
    
})



function connect() {
    fetch('/drone_connect', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function takeOff(event) {
    event.preventDefault();
    const altitude = document.getElementById('altitude').value;
    console.log(altitude);
    fetch('/takeoff', {
        method: 'POST',
        body: JSON.stringify({ altitude: altitude }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function land() {
    fetch('/land', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function RTL() {
    fetch('/RTL', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function yaw(event) {
    event.preventDefault();
    const yaw = document.getElementById('yaw').value;
    console.log(yaw);
    fetch('/yaw', {
        method: 'POST',
        body: JSON.stringify({ yaw: yaw }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}