import csv
from faker import Faker
import requests

from flask import (
    Blueprint, render_template, request, abort
)

bp = Blueprint('firstpart', __name__, url_prefix='/firstpart')

fake = Faker()


@bp.route('/requirements/')
def requirements():
    """
    This function returned content of requirement.txt file
    """
    with open("requirements.txt", "r") as file:
        text = file.read().split("\n")
        return render_template('firstpart/requirements.html', text=text)


@bp.route('/generate-users/')
def user_generator():
    """
    This function returned generated users depend on get parameters(100 default)
    """
    try:
        count = int(request.args.get("count", 100))
    except ValueError:
        return abort(404, f"Write only integer value")
    return render_template('firstpart/generator.html', users=[(fake.name() + " " + fake.email()) for _ in range(count)])


@bp.route('/mean/')
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
    return render_template('firstpart/mean.html', mean_height=mean_height, mean_weight=mean_weight)


@bp.route('/space/')
def number_of_astronaut():
    """
    This function return number of astronaut in space
    """
    read = requests.get('http://api.open-notify.org/astros.json')
    return render_template("firstpart/astronaut.html", astronaut=read.json()["number"])
