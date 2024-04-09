import socket
import pyaudio

# Server configuration
HOST = '192.168.40.80'  # Server's IP address
PORT = 8081         # Same port as server

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to server")

# Receive and play audio
try:
    while True:
        data = client_socket.recv(CHUNK)
        stream.write(data)
        # print(data)
except KeyboardInterrupt:
    print("Client stopped by user.")

# Cleanup
stream.stop_stream()
stream.close()
audio.terminate()
client_socket.close()