from flask import Flask, render_template, request, jsonify
import threading
import pygame_canvas

app = Flask(__name__)
current_tool = 'brush'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_tool', methods=['POST'])
def set_tool():
    global current_tool
    data = request.get_json()
    current_tool = data['tool']
    pygame_canvas.update_tool(current_tool)
    return jsonify(success=True)

def run_flask():
    app.run(debug=False, port=5000)

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    pygame_canvas.run()
