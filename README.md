# README BASIC WEB SERVICE

## Basic Web Service

This project consists in the implementation of a basic web service which receives a number in its numeric form and writes it in full form. This solution uses Python's flask lib.

### Requirements

1. python >= 2.7
2. Flask >= 1.0.2

### How to use - Without docker
1. Open a terminal and enter BasicWebService/source/ and run: 
```console
python server.py
```
2. Open a web browser and type http://localhost:5000/<INTEGER-NUMBER>
3. If the number is in the range -99999 - 99999, the server will return a JSON with the number written in full form, otherwise, a JSON with an error message will be returned.

### How to use - Using docker
1. Open a terminal and enter:
```console
docker pull lukter/basic-web-service:flask_alpine
```
2. Run a container
```console
sudo docker run -p5000:5000 lukter/basic-web-service:flask_alpine
```
3. Open a web browser and type http://localhost:5000/<INTEGER-NUMBER>

4. If the number is in the range -99999 - 99999, the server will return a JSON with the number written in full form, otherwise, a JSON with an error message will be returned.

## Notes

### Server
1. Server's IP is the localhost IP
2. The port used is defined 5000. It has been used a four-digit numbers to avoid conflicts.
3. Server can receive any kind of string, but only translates from -99999 - 99999.
