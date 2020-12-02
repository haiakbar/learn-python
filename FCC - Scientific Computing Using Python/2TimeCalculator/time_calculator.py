def format_time(time):
    
    splitted = time.split()
    merid = ''    
    
    if len(splitted) != 1:
        merid = splitted[1]
    
    hour, minutes = splitted[0].split(':')[0], splitted[0].split(':')[1]
    
    return (int(hour), int(minutes), merid)

def combine_time(start, interval):
    
    sum_hour = start[0] + interval[0]
    sum_minutes = start[1] + interval[1]
    
    sum_hour += sum_minutes//60
    sum_minutes = sum_minutes%60
    
    half_day_passed = 0

    while sum_hour > 12:
        sum_hour -= 12
        half_day_passed += 1
    
    if sum_hour == 12:
        half_day_passed += 1

    return (sum_hour, sum_minutes, start[2], half_day_passed)

def string_time(hour, minutes):
    
    hour = str(hour)
    minutes = str(minutes)
    '''
    if len(hour) != 2:
        hour = '0' + hour
    '''
    if len(minutes) != 2:
        minutes = '0' + minutes
    
    return (hour, minutes)

def get_merid(start_merid, half_day_passed):
    
    merid = ['AM', 'PM']
    
    half_day_end = half_day_passed + merid.index(start_merid)
    
    day_passed = half_day_end//2
    new_merid = merid[half_day_end%2]
    
    return (day_passed, new_merid)

def get_day(day_passed, day):
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
    day = day.capitalize()
    day_index = days.index(day)
    
    return days[(day_index+day_passed)%7]

def add_time(start, interval, day=False):
    
    combined_time = combine_time(format_time(start), format_time(interval))
    
    end_hour, end_minutes, start_merid, half_day_passed = combined_time
    
    hour, minutes = string_time(end_hour, end_minutes)
    
    day_passed, new_merid = get_merid(start_merid, half_day_passed)
    
    if day:
        end_day = get_day(day_passed, day)
        result = '{}:{} {}, {}'.format(hour, minutes, new_merid, end_day)
    else:
        result = '{}:{} {}'.format(hour, minutes, new_merid)
    
    if day_passed == 1:
        result += ' (next day)'
    elif day_passed > 1:
        result += ' ({} days later)'.format(day_passed)
    
    return result