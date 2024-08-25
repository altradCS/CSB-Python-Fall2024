import pandas as pd
import urllib.request
import csv
import datetime
from io import StringIO
import os


class SchoolAssessmentSystem:
    def __init__(self, files, web_log, parent = 'classes') -> None:
        self.files = files
        self.parent = parent
        self.url = web_log
        self.script_dir = os.path.dirname(os.path.realpath(__file__))

    def __process_file(self, file):
        self.df = pd.read_csv(os.path.join(self.script_dir, file))
    
    def __assign_grade(self, percentage):
        if percentage >= 90:
            return 'A'
        elif 80 <= percentage < 90:
            return 'B'
        elif 70 <= percentage < 80:
            return 'C'
        elif 60 <= percentage < 70:
            return 'D'
        else:
            return 'F'

    def __transfer_data(self): # some flaw here
        header = [['Class', 'Average_Score', 'Number of A', 'Number of F']]
        data = []
        for file in self.files:
            self.__process_file(f"{self.parent}/{file}")
            average_score, nA, nF = self.__analyze_content()
            data.append([file[6:9], average_score, nA, nF])
        with open(os.path.join(self.script_dir, f"all_classes {self.parent}.csv"), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(header + data)
    
    def __fetch_web_data(self):
        response = urllib.request.urlopen(self.url)
        data = response.read().decode('utf-8')
        data_file = StringIO(data)
        self.df = pd.read_csv(data_file)

        entry = self.df.shape[0]
        # print(self.df['Time Spent'])s
        time_spent = self.df['Time Spent'].apply(lambda x: int(x[:-1]))
        total_time_spent = time_spent.sum()
        average_time_spent = total_time_spent / entry
        max_time_spent = time_spent.max()
        min_time_spent = time_spent.min()
        return entry, total_time_spent, average_time_spent, max_time_spent, min_time_spent


    def __analyze_content(self):
        self.df['Average_Score'] = self.df.iloc[:, 2:].sum(axis=1) / 10
        self.df['Grade'] = self.df["Average_Score"].apply(self.__assign_grade)
        nA =(self.df['Grade'] == 'A').sum()
        nF = (self.df['Grade'] == 'F').sum()
        return round(self.df['Average_Score'].mean(), 2), nA, nF
    
    def generate_summary(self):
        self.__transfer_data()
        entry, total_time_spent, average_time_spent, max_time_spent, min_time_spent = self.__fetch_web_data()
        dataframe = pd.read_csv(os.path.join(self.script_dir, f"all_classes {self.parent}.csv"))
        max_average_score = dataframe['Average_Score'].max()
        mean_average_score = dataframe['Average_Score'].mean()
        top_class = dataframe[dataframe['Average_Score'] == max_average_score]['Class'].values[0]
        most_A = dataframe['Number of A'].max()
        class_most_A = dataframe[dataframe['Number of A'] == most_A]['Class'].values[0]
        print(f"""
School Assessment Summary Report for {self.parent}:

1. Overall Performance of Student: 
    - Average score: {mean_average_score}
    - Top-performing class: Grade {top_class} with average score of {max_average_score}
    - Class {class_most_A} has the most number of A students with {most_A} students
   
2. Web Data Insights:
    - Online participation: Students accessed assessment resources online {entry} times.
    - Total time spent: {total_time_spent} minutes
    - Average time spent: {average_time_spent} minutes
    - Maximum time spent: {max_time_spent} minutes
    - Minimum time spent: {min_time_spent} minutes

Report generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
""")