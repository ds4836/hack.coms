from flask import Flask, redirect, render_template, url_for
from src.main import main
from src.color_selection import rgb_to_hex

app = Flask(__name__)

@app.route('/')
def display_colors():
    color_list = main()
    hex_colors = [rgb_to_hex(color) for color in color_list]

    return render_template('colors.html', colors=hex_colors)

@app.route('/new_colors')
def new_colors():
    return redirect(url_for('display_colors'))

if __name__ == '__main__':
    app.run(debug=True)