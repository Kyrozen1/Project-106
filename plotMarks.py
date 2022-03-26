import csv
import plotly.express as px
import numpy as np

def plot(mark):
  with open("Marks.csv") as f:
    f = csv.DictReader(f)
    fig = px.scatter(f, x="Marks In Percentage", y="Days Present")
    fig.show()

def convert(mark):
  marks=[]
  dayPresent=[]
  with open("Marks.csv") as f:
    f = csv.DictReader(f)
    for row in f:
      marks.append(float(row["Marks In Percentage"]))
      dayPresent.append(float(row["Days Present"]))
  return{"x":marks, "y":dayPresent}

def corelation(converted):
  corelation = np.corrcoef(converted["x"],converted["y"])
  print("corelation between marks and day present:-\n-->",corelation[0,1])

mark = "Marks.csv"
converted = convert(mark)
plot(mark)
corelation(converted)