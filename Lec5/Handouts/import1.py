import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://localhost:5432/travel' #os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("/Users/timballard/Projects/CS50W/Lec5/flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
