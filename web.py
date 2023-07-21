# app.py
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import subprocess

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app, async_mode='threading')

process = None  # Global variable to store the subprocess

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    global process

    print('Client disconnected')

    # If the process is running, terminate it
    if process is not None and process.poll() is None:
        process.terminate()
        process.wait()
        print('Virtual Voice Assistant stopped due to client disconnection')

@socketio.on('run_script')
def run_script():
    global process

    try:
        if process is not None and process.poll() is None:
            emit('script_output', {'output': 'Virtual Voice Assistant is already running.'})
            return

        # Execute the main.py script using subprocess
        process = subprocess.Popen(['python', '-u', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Function to read output and emit it to the client
        def emit_output():
            for line in iter(process.stdout.readline, ''):
                socketio.emit('script_output', {'output': line.strip()})
            process.stdout.close()

        # Start the background task to read output and emit it to the client
        socketio.start_background_task(emit_output)

        process.wait()
        emit('script_output', {'output': 'Task Completed.'})
        emit('script_complete')  # Emit event to inform client about script completion
    except Exception as e:
        emit('script_output', {'output': f'Error: {str(e)}'})

@socketio.on('stop_script')
def stop_script():
    global process

    try:
        if process is not None and process.poll() is None:
            process.terminate()
            process.wait()  # Wait for the process to finish
            emit('script_output', {'output': 'Virtual Voice Assistance Stopped.'})
        else:
            emit('script_output', {'output': 'Virtual Voice Assistance is not running.'})
    except Exception as e:
        emit('script_output', {'output': f'Error: {str(e)}'})



if __name__ == '__main__':
    socketio.run(app, debug=True)
