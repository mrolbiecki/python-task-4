from pathlib import Path
import random
import csvio

DAYS_OF_WEEK = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

def get_days_in_range(day_range):
    start_day, end_day = day_range
    start_index = DAYS_OF_WEEK.index(start_day)
    end_index = DAYS_OF_WEEK.index(end_day)

    return DAYS_OF_WEEK[start_index:end_index + 1]

def generate_paths(months, weekdays, daytimes):
    paths = []
    counter = 0

    for month in months:
        days = get_days_in_range(weekdays[months.index(month)])

        for day in days:
            if len(daytimes) > counter:
                path = Path(f"{month}/{day}/{daytimes[counter]}")
                counter++
            else:
                path = Path(f"{month}/{day}/{"mor"}")

            paths.append(path)

    return paths

def calculate_total_time(paths):
    print('Calculating total time...')
    time = 0

    for path in paths:
        try:
            data = csvio.read_csv(path);

            if data[0][1] == 'A':
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
        print(data_row)
        csvio.write_to_csv(path, [["Model", "Result", "Time"], data_row])

    print('Files have been created successfully.')
