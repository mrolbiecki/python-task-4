import csvio
import pathgen
import argparse

MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
DAYS_OF_WEEK = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
TIMES_OF_DAY = ['mor', 'evn']

def validate_day_range(day_range):
    days = day_range.split('-')

    if len(days) > 2:
        raise argparse.ArgumentTypeError(f"Invalid day range: {day_range}. Too many days specified.")

    for day in days:
        if day not in DAYS_OF_WEEK:
            raise argparse.ArgumentTypeError(
                f"Invalid day abbreviation: {day}. Allowed values are {', '.join(DAYS_OF_WEEK)}.")

    return day_range

def parse_day_ranges(day_ranges):
    result = []
    for day_range in day_ranges:
        days = day_range.split('-')
        if len(days) == 2:
            result.append((days[0], days[1]))
        else:
            result.append((days[0], days[0]))
    return result

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--months', nargs='+', choices=MONTHS, required=True,
                    help="Select months (multiple allowed).")
parser.add_argument('-d', '--days', nargs='+', type=validate_day_range, required=True,
                    help="Select ranges of days (e.g., 'mon-tue', 'fri').")
parser.add_argument('-t', '--times', nargs='*', choices=TIMES_OF_DAY, default=['mor'],
                    help="Select time of day (mor/evn). Default is 'mor'.")
parser.add_argument('-o', '--operation', choices=['create', 'read'], default='read',
                    help="Choose operation mode: create or read files.")

args = parser.parse_args()

parsed_days = parse_day_ranges(args.days)

paths = pathgen.generate_paths(args.months, parsed_days, args.times)

if args.operation == 'create':
    pathgen.create_random_files(paths)
elif args.operation == 'read':
    pathgen.calculate_total_time(paths)
