import requests
from faker import Faker
from flask import Flask, request, render_template
import csv

app = Flask(__name__)
fake = Faker()


@app.route('/requirements/')
def requirements():
    """
    This function returned content of requirement.txt file
    """
    with open("requirements.txt", "r") as file:
        text = file.read().split("\n")
        return render_template('requirements.html', text=text)


@app.route('/generate-users/')
def user_generator():
    """
    This function returned generated users depend on get parameters(100 default)
    """
    try:
        count = int(request.args.get("count", 100))
    except ValueError:
        return render_template("error.html")
    return render_template('generator.html', users=[(fake.name() + " " + fake.email()) for _ in range(count)])


@app.route('/mean/')
def height_weight():
    """
    This function returned mean of value height(cm) and weight(kg). The value taken from hw.csv file in inch and pounds resp.
    """
    height = []
    weight = []
    with open("hw.csv", "r", newline="") as csvfile:
        read = csv.DictReader(csvfile)
        for row in read:
            height.append(float(row["Height(Inches)"]))
            weight.append(float(row["Weight(Pounds)"]))
    mean_height = sum(height) / len(height) * 2.54
    mean_weight = sum(weight) / len(weight) * 2.20462
    return render_template('mean.html', mean_height=mean_height, mean_weight=mean_weight)


@app.route('/space/')
def number_of_astronaut():
    """
    This function return number of astronaut in space
    """
    read = requests.get('http://api.open-notify.org/astros.json')
    return render_template("astronaut.html", astronaut=read.json()["number"])
