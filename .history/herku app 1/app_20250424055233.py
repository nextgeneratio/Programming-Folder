from flask import Flask, render_template, request, jsonify
import logic

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

if __name__ == '__main__':
    app.run(debug=True)