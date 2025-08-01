from flask import Flask, render_template, jsonify
import threading
from servo import return_to_neutral, left_swing, right_swing, stop_swing, left_walk, right_walk, LL, LF, RL, RF

app = Flask(__name__)

# Obsługa strony głównej
@app.route('/')
def index():
    return render_template('index.html')

# Moonwalk: jedno kliknięcie
@app.route('/moonwalk')
def moonwalk():
    threading.Thread(target=moonwalk).start()
    return jsonify({'status': 'started moonwalk'})

# Dance: jedno kliknięcie
@app.route('/dance')
def dance():
    threading.Thread(target=dance).start()
    return jsonify({'status': 'started dance'})

# Walk left
@app.route('/walkleft')
def leftwalk():
    threading.Thread(target=left_walk).start()
    return jsonify({'status': 'leftwalking'})

# Walk right
@app.route('/walkright')
def rightwalk():
    threading.Thread(target=right_walk).start()
    return jsonify({'status': 'rightwalking'})

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

# Stop swing
@app.route('/stopswing')
def stop():
    stop_swing()
    return jsonify({'status': 'stopswing'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
