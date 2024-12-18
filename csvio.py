import csv
from pathlib import Path

def read_csv(path):
    path_file = Path(path / 'Data.csv')
    if not path_file.exists():
        print("Path doesn't exist")
        return

    data = []
    with open(path_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data

def write_to_csv(path, rows):
    if not path.exists():
        print("Path doesn't exist")
        return

    with open(path / 'Data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
    return