from pathlib import Path
import random
import csvio

def generate_paths(months, weekdays, daytimes):
    paths = []
    
    for month in months:
        start_day, end_day = weekdays[months.index(month)]
        
        for time in daytimes:
            if start_day == end_day:
                path = Path(f"{month}/{start_day}/{time}")
                paths.append(path)
            else:
                paths.append(Path(f'{month}/{start_day}/{time}'))
                paths.append(Path(f'{month}/{end_day}/{time}'))

    return paths

def calculate_total_time(paths):
    print('Calculating total time...')
    time = 0

    for path in paths:
        try:
            data = csvio.read_csv(path);
            if (data[0][1] == 'A'):
                time += data[2][1];

        except FileNotFoundError:
            print(f"File not found: {path}")
        except KeyError as e:
            print(f"Missing column in file {path}: {e}")
        except ValueError as e:
            print(f"Invalid data in file {path}: {e}")
            
    print(f"Total time: {time}.")


def generate_random_data():
    model = random.choice(['A', 'B', 'C'])
    result = random.randint(0, 1000)
    time = random.randint(0, 1000)

    return [model, result, f"{time}s"]


def create_random_files(paths):
    print('Creating random files...')
    
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)

        data_row = generate_random_data()
        csvio.write_to_csv(path, [["Model", "Result", "Time"], data_row])
    
    print('Files have been created successfully.')
