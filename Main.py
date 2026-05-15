from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import TopStudentsAnalyser, DataAnalyser


class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        try:
            gpas = list(map(lambda s: float(s["GPA"]), self.students))
        except (KeyError, ValueError) as e:
            print(f"GpaAnalyser error: {e}")
            return

        high = list(filter(lambda s: float(s["GPA"]) > 3.5, self.students))

        self.result = {
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": len(high),
        }

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        for key, value in self.result.items():
            print(f"{key}: {value}")
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


def main():
    fm = FileManager('students.csv')
    try:
        fm.check_file()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    fm.create_output_folder('output')

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    if not dl.students:
        print("No students loaded, stopping.")
        return

    print("-" * 30)
    base = DataAnalyser(dl.students)
    print(base)
    base.analyse()
    print()

    analyser = TopStudentsAnalyser(dl.students)
    print(analyser)
    print()

    analyser.analyse()
    analyser.print_results()
    print()

    saver = ResultSaver(analyser.result, 'output/result.json')
    report = Report(analyser, saver)
    report.generate()
    print()

    small_sample = dl.students[:10]
    analysers = [
        TopStudentsAnalyser(dl.students),
        GpaAnalyser(small_sample),
    ]

    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)
    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()
        print()


if __name__ == '__main__':
    main()