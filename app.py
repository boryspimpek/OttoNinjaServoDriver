from flask import Flask, render_template, jsonify
import threading
from servo import (
    return_to_neutral, left_swing, right_swing,
    left_walk_forward, right_walk_forward, walk, LL, LF, RL, RF, left_walk_back, right_walk_back, moonwalk, steps
)

app = Flask(__name__)

walk_thread = None
walk_stop_flag = threading.Event()

# Obsługa strony głównej
@app.route('/')
def index():
    return render_template('index.html')

# Moonwalk: jedno kliknięcie
@app.route('/startmoonwalk')
def startmoonwalk():
    threading.Thread(target=moonwalk).start()
    return jsonify({'status': 'startedmoonwalk'})

# Dance: jedno kliknięcie
@app.route('/startsteps')
def startsteps():
    threading.Thread(target=steps).start()
    return jsonify({'status': 'startedsteps'})

# Walk left
@app.route('/walkleftForward')
def leftwalkForward():
    threading.Thread(target=left_walk_forward).start()
    return jsonify({'status': 'leftwalking'})

# Walk right
@app.route('/walkrightForward')
def rightwalkForward():
    threading.Thread(target=right_walk_forward).start()
    return jsonify({'status': 'rightwalking'})

# Walk left back
@app.route('/walkleftBack')
def leftwalkBack():
    threading.Thread(target=left_walk_back).start()
    return jsonify({'status': 'leftwalkingback'})

# Walk right back
@app.route('/walkrightBack')
def rightwalkBack():
    threading.Thread(target=right_walk_back).start()
    return jsonify({'status': 'rightwalkingback'})

# Swing left
@app.route('/leftswing/start')
def leftswing_start():
    threading.Thread(target=left_swing).start()
    return jsonify({'status': 'leftswinging'})

# Swing right
@app.route('/rightswing/start')
def rightswing_start():
    threading.Thread(target=right_swing).start()
    return jsonify({'status': 'rightswinging'})

@app.route('/startwalk')
def startwalk():
    global walk_thread, walk_stop_flag
    if walk_thread is None or not walk_thread.is_alive():
        walk_stop_flag.clear()
        walk_thread = threading.Thread(target=walk, args=(walk_stop_flag,))
        walk_thread.start()
        return jsonify({'status': 'walk started'})
    else:
        return jsonify({'status': 'walk already running'})

@app.route('/stopwalk')
def stopwalk():
    walk_stop_flag.set()
    return_to_neutral()
    return jsonify({'status': 'walk stopped'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
