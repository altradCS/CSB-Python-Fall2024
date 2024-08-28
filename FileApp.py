# from school_assessment import SchoolAssessmentSystem
# from report_generator import ReportGenerator
# from io import StringIO
# import urllib.request
# import pandas as pd

# class ReadGithubFile:
#     def fetch_web_data(self, url):
#         try:
#             response = urllib.request.urlopen(url)
#             data = response.read().decode('utf-8')
#             data_file = StringIO(data)
#             df = pd.read_csv(data_file)
#             return df
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             return None

# def main():
#     try:
#         # Raw URL to the CSV file on GitHub
#         github_file_url = 'https://raw.githubusercontent.com/altradCS/CSB-Python-Fall2024-FileSystem/main/classes/all_semester.csv'
        
#         # Fetch data from GitHub
#         github_file_reader = ReadGithubFile()
#         df = github_file_reader.fetch_web_data(github_file_url)
        
#         if df is None:
#             print("Failed to load data from GitHub. Exiting.")
#             return

#         # Instantiate the SchoolAssessmentSystem with the DataFrame
#         analyzer = SchoolAssessmentSystem(df)
        
#         while True:
#             student_name = input("Enter student name (or type 'exit' to quit): ")
#             if student_name.lower() == 'exit':
#                 break
            
#             analyzer.analyze_content(student_name)
#             summary = ReportGenerator.generate_summary(analyzer.summary_data)
#             print(summary)
#             ReportGenerator.save_summary_to_file(summary, 'assessment_summary_report.txt')
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()
