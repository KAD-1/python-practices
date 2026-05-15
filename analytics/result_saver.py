import json
import os


class ResultSaver:
    def __init__(self, result, filepath):
        self.result = result
        self.filepath = filepath

    def save_json(self):
        folder = os.path.dirname(self.filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4, ensure_ascii=False)
            print(f"Result saved to {self.filepath}")
        except Exception as e:
            print(f"Failed to save result: {e}")

    def __str__(self):
        return f"ResultSaver: saving to {self.filepath}"