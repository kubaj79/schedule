#-*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
#import impxlsx_py as im
from dane import *
import datetime

app=Flask(__name__)

dane=apteka()
komputerowa=komputerowa()
aula2=aula2()
aula3=aula3()
aula4a=aula4a()
aula4b=aula4b()
sala45=sala45()
sala46=sala46()
sala213=sala213()
sala214=sala214()
leg=legeda()
data=datetime.datetime.now().strftime("%Y,%m,%d")

@app.route('/')
def index():
    return render_template('home.html',dane = dane,komputerowa=komputerowa,aula2=aula2,aula3=aula3,aula4a=aula4a,aula4b=aula4b,sala45=sala45,sala46=sala46,sala213=sala213,sala214=sala214,leg=leg,data=data)

if __name__== '__main__':
    app.run(debug=True)
