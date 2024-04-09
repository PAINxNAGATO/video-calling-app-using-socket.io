from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect-to-server', methods=['POST'])
def connect_to_server():
    print('Connect to server')
    subprocess.Popen(['python', 'client1.py'])
    subprocess.Popen(['python', 'client1_1.py'])
    return 'Connecting to server...'

if __name__ == '__main__':
    app.run(debug=True)
