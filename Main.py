import os
import csv
import json

import os
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
        except Exception as e:
            print(f"Error: {e}")
        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for student in self.students[:n]:
            print(f"{student['student_id']} | {student['age']} | {student['gender']} | {student['country']} | GPA: {student['GPA']}")
        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        top_scorers = list(filter(lambda s: float(s['final_exam_score']) > 95, self.students))
        gpa_values = list(map(lambda s: float(s['GPA']), self.students))
        good_assignments = list(filter(lambda s: float(s['assignment_score']) > 90, self.students))

        sorted_students = sorted(self.students, key=lambda x: float(x['final_exam_score']), reverse=True)
        top10 = sorted_students[:10]

        top10_list = []
        for i, s in enumerate(top10):
            try:
                top10_list.append({
                    "rank": i + 1,
                    "student_id": s['student_id'],
                    "country": s['country'],
                    "major": s['major'],
                    "final_exam_score": float(s['final_exam_score']),
                    "GPA": float(s['GPA'])
                })
            except ValueError:
                print(f"Warning: could not convert value for student {s.get('student_id', '?')} — skipping row.")
                continue

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top10_list,
            "lambda_filter_stats": {
                "final_exam_score_gt_95": len(top_scorers),
                "gpa_values_first_5": gpa_values[:5],
                "assignment_score_gt_90": len(good_assignments)
            }
        }
        return self.result

    def print_results(self):
        top10 = self.result.get("top_10", [])
        stats = self.result.get("lambda_filter_stats", {})

        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)
        for s in top10:
            print(f"{s['rank']}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
        print("-" * 30)

        print()
        print("-" * 30)
        print("Lambda / Map / Filter")
        print("-" * 30)
        print(f"final_exam_score > 95  : {stats.get('final_exam_score_gt_95')}")
        print(f"GPA values (first 5)   : {stats.get('gpa_values_first_5')}")
        print(f"assignment_score > 90  : {stats.get('assignment_score_gt_90')}")
        print("-" * 30)

        print()
        print("=" * 30)
        print("ANALYSIS RESULT")
        print("=" * 30)
        print(f"Analysis       : {self.result['analysis']}")
        print(f"Total students : {self.result['total_students']}")
        print("Top 10 saved to output/result.json")
        print("=" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


fm = FileManager('students.csv')
if not fm.check_file():
    print('Stopping program.')
    exit()
fm.create_output_folder()

dl = DataLoader('students.csv')
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()

dl_bad = DataLoader('wrong_file.csv')
dl_bad.load()