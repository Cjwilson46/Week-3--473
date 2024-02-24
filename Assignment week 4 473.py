# Name: Christopher Wilson 
# Date: 1/28/24
# Assignment Number: 4

import os
import stat
import time

class FileProcessor:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist")

        self.file_path = file_path
        self.file_size = os.path.getsize(file_path)
        self.creation_time = time.ctime(os.path.getctime(file_path))
        self.modification_time = time.ctime(os.path.getmtime(file_path))
        self.access_time = time.ctime(os.path.getatime(file_path))
        self.owner = os.stat(file_path).st_uid
        self.mode = stat.filemode(os.stat(file_path).st_mode)

    def get_file_header(self):
        with open(self.file_path, 'rb') as file:
            self.header = file.read(20)

    def print_file_details(self):
        print(f"File Path: {self.file_path}")
        print(f"File Size: {self.file_size} bytes")
        print(f"Creation Time: {self.creation_time}")
        print(f"Modification Time: {self.modification_time}")
        print(f"Access Time: {self.access_time}")
        print(f"Owner: {self.owner}")
        print(f"Mode: {self.mode}")
        print(f"Header (Hex): {self.header.hex()}")

# Demonstration
dir_path = input("Enter a directory path: ")

for filename in os.listdir(dir_path):
    full_path = os.path.join(dir_path, filename)
    if os.path.isfile(full_path):
        file_processor = FileProcessor(full_path)
        file_processor.get_file_header()
        file_processor.print_file_details()
