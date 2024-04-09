import socket
import pyaudio

# Server configuration
HOST = '192.168.40.80'  # The server's IP address (localhost for this example)
PORT = 8081         # Arbitrary port number

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server listening on port", PORT)

# Accept a connection
client_socket, address = server_socket.accept()
print("Connection from", address)

# Start streaming audio
try:
    while True:
        data = stream.read(CHUNK)
        client_socket.sendall(data)
except KeyboardInterrupt:
    print("Server stopped by user.")

# Cleanup
stream.stop_stream()
stream.close()
audio.terminate()
server_socket.close()