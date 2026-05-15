import csv


class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.students = []

    def load(self):
        try:
            with open(self.filepath, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = [row for row in reader]
            print(f"Loaded {len(self.students)} students from {self.filepath}")
        except FileNotFoundError:
            print(f"Error: cannot find file {self.filepath}")
        except Exception as e:
            print(f"Something went wrong while loading: {e}")

    def preview(self, n=3):
        print(f"\nFirst {n} rows:")
        for i, row in enumerate(self.students[:n]):
            print(f"  [{i}] {row}")
        print()

    def __str__(self):
        return f"DataLoader: {self.filepath}, {len(self.students)} students loaded"