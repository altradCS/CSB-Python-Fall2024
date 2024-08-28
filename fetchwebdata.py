import pandas as pd
import urllib.request
from io import StringIO

class ReadGithubFile:
    def fetch_web_data(self, url):
        try:
            response = urllib.request.urlopen(url)
            data = response.read().decode('utf-8')
            data_file = StringIO(data)
            self.df = pd.read_csv(data_file)
            print("Data from GitHub URL:")
            print(self.df)
        except Exception as e:
            print(f"An error occurred: {e}")

# Use the raw URL to the CSV file from GitHub
github_file_url = 'https://raw.githubusercontent.com/altradCS/CSB-Python-Fall2024-FileSystem/main/semester%202/web%20log.csv'

# Define the SchoolAssessmentSystem instance
school_system = ReadGithubFile()

# Fetch and process the file from GitHub
school_system.fetch_web_data(github_file_url)
