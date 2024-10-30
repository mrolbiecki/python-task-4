import csv
from pathlib import Path


def read_csv(path):
    path_file = Path(path)
    if not path_file.exists():
        print("Path doesn't exist")
        return

    data = []
    with open('plik.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data

def write_to_csv(path, columns):
    path_file = Path(path)
    if not path_file.exists():
        print("Path doesn't exist")
        return

    with open(path + '/Data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in columns:
            writer.writerow(row)
    return
