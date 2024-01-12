# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days
import re
from datetime import datetime

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


# initialize dictionary of starting and end indices since text file is fixed width
fwf_dict = {"time":(3,14),
            "athlete":(14,56),
            "race_date": (56,73),
            "dob": (73,87),
            "loc":(87,150)}

def get_age_yrs_days(age_in_days):
    age_yrs = int(age_in_days//365.25)
    age_days = int(age_in_days%365.25//1)
    
    age = f"{age_yrs}y{age_days}d"
    return age

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""

    race_time = line[fwf_dict["time"][0]:fwf_dict["time"][1]].strip()
    birth_date = line[fwf_dict["dob"][0]:fwf_dict["dob"][1]].strip()
    birth_date = datetime.strptime(birth_date, '%d %b %Y')
    race_date = line[fwf_dict["race_date"][0]:fwf_dict["race_date"][1]].strip()
    race_date = datetime.strptime(race_date, '%d %b %Y')
    
    age_in_days = race_date-birth_date
    
    age = get_age_yrs_days(age_in_days.days)

    return (age, race_time)

def format_time_to_secs(time_str):
    """ database is currently formatted as mm:ss
        where m is minutes,
        and s is seconds
    """
    mins = float(time_str.split(":")[0])
    secs = float(time_str.split(":")[1])
    time_secs = (mins*60) + secs
    return time_secs

def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    
    # get all Jennifer Rhines race lines
    pattern = re.compile(r".*Jennifer Rhines.*", re.IGNORECASE)
    runner_lines = [line for line in races.split('\n') if pattern.match(line)]
    # Find race that has the slowest time
    curr_slowest = 0
    for line in runner_lines:
        res = get_event_time(line)
        race_time = format_time_to_secs(res[1])
        if curr_slowest == 0:
            curr_slowest = race_time
            slowest_stats = res
        else:
            if curr_slowest < race_time:
                slowest_stats = res
            else:
                pass
    return slowest_stats