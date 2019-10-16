from flask import Flask, render_template, url_for, request
import sqlite3
from bot import solve

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('cb.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        nm = request.form["msg"]

        return render_template('cb.html',res = solve(nm))


if __name__ == '__main__':
    app.run(debug=True)
