import csv
import plotly.express as px
import numpy as np

def plot(coffee):
  with open("Coffee.csv") as f:
    f = csv.DictReader(f)
    fig = px.scatter(f, x="Coffee in ml", y="sleep in hours")
    fig.show()

def convert(coffee):
  coffees=[]
  sleep=[]
  with open("Coffee.csv") as f:
    f = csv.DictReader(f)
    for row in f:
      coffees.append(float(row["sleep in hours"]))
      sleep.append(float(row["Coffee in ml"]))
  return{"x":coffees, "y":sleep}

def corelation(converted):
  corelation = np.corrcoef(converted["x"],converted["y"])
  print("corelation between hours of sleep and amount of coffee dranked:-\n-->",corelation[0,1])

coffee = "Coffee.csv"
converted = convert(coffee)
plot(coffee)
corelation(converted)