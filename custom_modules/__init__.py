import os

current_files_folders = os.listdir()

if 'cars_data' not in current_files_folders:
    print("Folder 'cars_data' not yet in directory, creating it")
    os.mkdir('cars_data')