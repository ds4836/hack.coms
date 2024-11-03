from flask import Flask, redirect, render_template, request, url_for
from src.main import main
from src.color_selection import rgb_to_hex

app = Flask(__name__)

@app.route('/')
def display_colors():
    selection = request.args.get('option')
    color_list = main(selection)
    hex_colors = [rgb_to_hex(color) for color in color_list]

    return render_template('colors.html', colors=hex_colors, selection=selection)

@app.route('/new_colors')
def new_colors():
    selection = request.args.get('option')
    if selection:
        return redirect(url_for('display_colors',option=selection))
    else:
        return redirect(url_for('display_colors',selection=None))

if __name__ == '__main__':
    app.run(debug=True, port=4999)