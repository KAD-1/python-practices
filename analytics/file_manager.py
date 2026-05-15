import os


class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def check_file(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")
        print(f"File found: {self.filepath}")

    def create_output_folder(self, folder="output"):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        else:
            print(f"Folder already exists: {folder}")

    def __str__(self):
        return f"FileManager: {self.filepath}"
