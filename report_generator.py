import pandas as pd

class ReportGenerator:
    @staticmethod
    def generate_summary(summary_data):
        try:
            if not summary_data:
                return "No student data analyzed yet. Please run analyze_content first."
            summary_report = "\n\nSchool Assessment Summary Report:\n"
            for student in summary_data:
                summary_report += f"====================================\n"
                summary_report += f"Student name: {student['Name']}\n"
                summary_report += f"Student ID: {student['id']}\n"
                summary_report += f"Enroll in: {student['Semester']}\n\n"
                summary_report += f"1. Overall Performance:\n"
                summary_report += f"   - Average score: {student['Average Score']:.1f}\n"
                summary_report += f"   - Overall Grade: {student['Grade']}\n"
                summary_report += f"2. Subject-wise Analysis:\n"
                summary_report += f"   + Subject grades:\n{student['Subject Analysis']}\n"
                summary_report += f"   * {student['Notable Observation']}: Highest scoring subject of {student['Highest Score']}.\n"
                summary_report += f"   * {student['Lowest Class']}: Lowest scoring subject of {student['Lowest Score']}.\n"
                summary_report += f"3. Notable Observations:\n"
                summary_report += f"   - {student['Notable Observation']} course shows a great accomplishment.\n"
                summary_report += f"4. Web Data Insights:\n"
                summary_report += f"   - Student email: {student['email']}\n"
                summary_report += f"   - Online class participation duration: {student['Online Participation']} minutes\n"
                summary_report += f"5. Recommendations:\n"
                summary_report += f"   - Try to improve your performance in {student['Lowest Class']} course.\n\n"
            summary_report += f"Report generated on: {pd.Timestamp.now().strftime('%Y-%m-%d')}\n"
            return summary_report
        except Exception as e:
            print(f"An error occurred while generating the summary: {e}")

    @staticmethod
    def save_summary_to_file(summary, filename):
        try:
            with open(filename, 'w') as file:
                file.write(summary)
            print(f"Summary report saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving the summary: {e}")
