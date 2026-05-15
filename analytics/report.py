class Report:
    def __init__(self, analyser, saver):
        self.analyser = analyser
        self.saver = saver

    def generate(self):
        print("Generating report...")
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.save_json()
        print("Report complete.")

    def __str__(self):
        return f"Report using {type(self.analyser).__name__}"