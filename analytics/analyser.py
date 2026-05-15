class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class TopStudentsAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        valid = list(filter(
            lambda s: s.get("final_exam_score", "").strip() != "",
            self.students
        ))

        try:
            sorted_students = sorted(
                valid,
                key=lambda s: float(s["final_exam_score"]),
                reverse=True
            )
        except ValueError as e:
            print(f"Error sorting students: {e}")
            return

        top_10 = sorted_students[:10]

        scores = list(map(lambda s: float(s["final_exam_score"]), top_10))
        gpas = list(map(lambda s: float(s["GPA"]), top_10))
        study_hours = list(map(lambda s: float(s["study_hours_per_day"]), top_10))

        self.result = {
            "total_students": len(self.students),
            "top_10": top_10,
            "avg_score_top10": round(sum(scores) / len(scores), 2),
            "avg_gpa_top10": round(sum(gpas) / len(gpas), 2),
            "avg_study_hours_top10": round(sum(study_hours) / len(study_hours), 2),
        }

    def print_results(self):
        print("=" * 30)
        print("TOP STUDENTS ANALYSIS REPORT")
        print("=" * 30)

        temp = {k: v for k, v in self.result.items() if k != "top_10"}
        for key, value in temp.items():
            print(f"{key}: {value}")

        print("\nTop 10 Students:")
        for i, student in enumerate(self.result.get("top_10", []), 1):
            score = student.get("final_exam_score", "N/A")
            gpa = student.get("GPA", "N/A")
            country = student.get("country", "N/A")
            print(f"  {i}. Score: {score} | GPA: {gpa} | Country: {country}")

        print("=" * 30)

    def __str__(self):
        return f"TopStudentsAnalyser: Top Students Analysis, {len(self.students)} students"