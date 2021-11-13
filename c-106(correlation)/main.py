
import csv
import plotly.express as px
import numpy as np

def graph(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getData(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return{"x" : marks_in_percentage, "y": days_present}

def finding_Correlation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(" Correlation is : ",correlation[0,1])

def main():
    data_path  = "./Student Marks vs Days Present.csv"

    datasource = getData(data_path)
    finding_Correlation(datasource)
    graph(data_path)

main()
