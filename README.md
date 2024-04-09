# V-CASP : Video Call App using Scoket Programming

> **Name**:Harsh Singh Rawat, Geetansh Jangid, Kartikey Teotia<br>
  **Reg**: ECE/21127/787, ECE/21124/784, ECE/21129/789

We present an Video Calling App for one vs one connected over the same network using socket programming and simple web client using flask and python.

## Usage and Installation
- Clone this repository, then create a virtual environment using `venv` or `conda` and then to install the dependencies type `pip install -r requirements.txt` in the terminal where the cloned repository resides after activating the virtual environment.
- Find the IPv4 address using `ipconfig` in linux system and `ifconfig` in Windows. 
- Place this IP in both server_video.py and server_audio.py of your PC and the Place the same IP in the client_audio.py and client_video.py of the second machine. 
- Do the same for the second machine connected to the same network.  
- Run both server (audio/video) on both machines using `python3 server_video.py` and `python3 server_audio.py` in different Terminals.
- Run the Clients Simultaneously by running `python3 app.py`
- open Web page and start video call.
