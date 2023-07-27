def add_time(start, duration, current_day = None):
    time = ""
    condition = ""
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if start.find("AM")>0:
        time = start.replace(" AM","")
        condition = 0



    else:
        time = start.replace(" PM", "")
        condition = 12

    hour = int(time.split(":")[0])
    hour += condition
    minute = int(time.split(":")[1])
    add_hour = int(duration.split(":")[0])
    add_minute = int(duration.split(":")[1])

    total_minute = minute + add_minute
    total_hour = hour + add_hour
    total_day = 0
    total_weekday = ""
    if total_minute > 59:
        total_minute -= 60
        total_hour +=1

    if total_hour >23:
        total_day = total_hour // 24
        total_hour = total_hour % 24

    if current_day is not None:
        total_weekday =week.index(current_day.capitalize())
        total_weekday += total_day
        total_weekday %= 7



    output_minutes = str(total_minute).zfill(2)
    output_conditions = (" AM" if total_hour < 12 else " PM")
    output_days = " (next day)" if total_day == 1 else " ("+ str(total_day)+" days later)"
    output_weekdays = ", "+week[total_weekday] if current_day is not None else ""
    output_hours = "12" if total_hour == 0 else str(total_hour - 12 if total_hour > 12 else total_hour)

    new_time = ""
    if current_day is None:
        new_time = output_hours + ":" + output_minutes + output_conditions

    if total_day > 0:
        new_time = output_hours + ":" + output_minutes + output_conditions + output_weekdays + output_days
    else:
        new_time = output_hours + ":" + output_minutes + output_conditions + output_weekdays

    return new_time