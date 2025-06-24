
from flask import Flask, render_template,request
import subprocess
import sys
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run/<project>')
def run_project(project):
    scripts = {
        'coffee': 'projects/coffee_machine/coffee.py',
        'pong': 'projects/pong_game/pong.py',
        'workout': 'projects/workout_tracker/workout.py',
        'weather': 'projects/weather/weather.py'
    }
    if project in scripts:
        subprocess.Popen([sys.executable, scripts[project]])
        return f"Started {project.capitalize()}!"
    return "Project not found."

@app.route('/blog')
def run_blog():
    os.system("python projects/blog/app.py")
    return "Blog app started!"
@app.route('/coffee_web', methods=["GET", "POST"])
def coffee_web():
    menu = {
        "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
        "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
    }
    resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
    message = ""

    if request.method == "POST":
        choice = request.form.get("drink")
        quarters = float(request.form.get("quarters", 0)) * 0.25
        dimes = float(request.form.get("dimes", 0)) * 0.10
        nickels = float(request.form.get("nickels", 0)) * 0.05
        pennies = float(request.form.get("pennies", 0)) * 0.01
        payment = quarters + dimes + nickels + pennies

        drink = menu.get(choice)
        if drink:
            cost = drink["cost"]
            if payment < cost:
                message = f"Not enough money. ${payment:.2f} refunded."
            else:
                change = round(payment - cost, 2)
                message = f"Enjoy your {choice} ☕. Change: ${change}"

    return render_template("coffee_web.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)
