from flask import Flask, render_template, url_for, request
import sqlite3
from bot import solve
import math

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('cb.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        nm = request.form["msg"]
        E = int(nm)
        #decrypt
        d = 13
        n = 143
        

        C = pow(E,d,n)
        C = E
        input = ""
        while(C>0):
        	rem = C%100
        	c = chr(rem)
        	input+= c
        	C = C//100
        
        input = input[::-1]
        output = solve(input)
        
        return render_template('cb.html',res = output)


if __name__ == '__main__':
    app.run(debug=True)
