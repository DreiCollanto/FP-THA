# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()

    pattern = re.compile(r".*Jennifer Rhines.*", re.IGNORECASE)
    
    runner_lines = [line for line in races.split('\n')
                      if pattern.match(line)]
    
    racetimes = [line.split()[0].strip() for line in runner_lines]
    
    return racetimes

def format_time_to_secs(time_str):
    """ database is currently formatted as mm:ss
        where m is minutes,
        and s is seconds
    """
    mins = float(time_str.split(":")[0])
    secs = float(time_str.split(":")[1])
    time_secs = (mins*60) + secs
    return time_secs

def format_secs_to_time(s):
    """ There is currently no function from datetime and time packages that support milliseconds
        This function extracts mins, seconds and milliseconds from seconds
    """
    mins = int(s//60)
    secs = int(s%60//1)
    M = int(s%60%1*1000)
    return '{:02}:{:02}:{:02}'.format(mins,secs,M)

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    
    racetimes = [format_time_to_secs(t) for t in racetimes]
    avg_racetime = sum(racetimes)/len(racetimes)
    
    
    return format_secs_to_time(avg_racetime)