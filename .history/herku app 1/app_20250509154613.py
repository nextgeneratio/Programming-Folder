from flask import Flask, render_template, request, jsonify, redirect, url_for
import logic
import os
from logic import reset_game_state

app = Flask(__name__)

# Initialize the game matrix
mat = logic.start_game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global mat
    direction = request.json.get('direction')
    if direction == 'up':
        mat, _ = logic.move_up(mat)
    elif direction == 'down':
        mat, _ = logic.move_down(mat)
    elif direction == 'left':
        mat, _ = logic.move_left(mat)
    elif direction == 'right':
        mat, _ = logic.move_right(mat)

    status = logic.get_current_state(mat)
    if status == 'GAME NOT OVER':
        logic.add_new_2(mat)

    return jsonify({'matrix': mat, 'status': status})

@app.route('/restart')
def restart_game():
    reset_game_state()
    return redirect(url_for('index'))  # Redirect to the starting page

while True:
    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
        app.run(host="0.0.0.0", port=port)