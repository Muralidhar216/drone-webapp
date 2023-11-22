
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
socket.on('parameters', function(data) {
    console.log('Received altitude update:', data.data);
    document.querySelector("#altitude1").innerHTML="Altitude : "+data.data;
});

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
    event.preventDefault();  // Prevent the form from submitting and page reload

    const yaw = document.getElementById('yaw').value;
    console.log(yaw);
    fetch('/yaw', {
        method: 'POST',
        body: JSON.stringify({ yaw: yaw }),
        headers: {
            'Content-Type': 'application/json', // Set the Content-Type header
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