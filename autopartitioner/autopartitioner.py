
def RETURN_HOUR_FORMAT(LENGTH_OF_LECTURE):
    hours = LENGTH_OF_LECTURE // 60 
    minutes = LENGTH_OF_LECTURE % 60
    if hours == 0 and minutes == 1:
        return f"{minutes} minute"
    elif hours == 0:
        return f"{minutes} minutes"
    else:
        return f"{hours} hr {minutes} minutes"
def PARTITION_BASED_ON_DAYS(LENGTH_OF_LECTURE,DAYS_AVAILABLE):
    if LENGTH_OF_LECTURE/DAYS_AVAILABLE == 1:
        return str(f"{int(LENGTH_OF_LECTURE/DAYS_AVAILABLE)} minute")
    else:
        return str(f"{int(LENGTH_OF_LECTURE/DAYS_AVAILABLE)} minutes")
def PARTITION_BASED_ON_TIME(LENGTH_OF_LECTURE,TIME_AVAILABLE):

    if LENGTH_OF_LECTURE/TIME_AVAILABLE == 1:
        return str(f"{float(LENGTH_OF_LECTURE/TIME_AVAILABLE)} day")
    else:
        return str(f"{float(LENGTH_OF_LECTURE/TIME_AVAILABLE)} days")
def main():
    LENGTH_OF_LECTURE = int(0)
    while True:
        USER_INPUT = (input(f"How long is your lecture video in minutes? type {"DONE"} when you finish input your time."))
        if USER_INPUT.upper() == "DONE" or USER_INPUT == "":
            break
        LENGTH_OF_LECTURE += int(USER_INPUT)
    DAYS_AVAILABLE = int(input("How many days per week available for watching the videos?"))
    TIME_AVAILABLE = int(input("How many minutes do you have available per day?"))
    print(f"You need to watch the lecture videos for a total of {RETURN_HOUR_FORMAT(LENGTH_OF_LECTURE)}.")
    print(f"That means that you need to watch an average of "
          f"{PARTITION_BASED_ON_DAYS(LENGTH_OF_LECTURE,DAYS_AVAILABLE)} "
          f"per day if you want to finish watching it within {DAYS_AVAILABLE} day(s).")
    print(f"Or, you need to spend {PARTITION_BASED_ON_TIME(LENGTH_OF_LECTURE,TIME_AVAILABLE)} ({TIME_AVAILABLE}minute(s) per day) to completely watch all the videos required.")
    if (LENGTH_OF_LECTURE/TIME_AVAILABLE).is_integer() != True:

        print(f"{round(LENGTH_OF_LECTURE/TIME_AVAILABLE)+ 1} days, if rounded up.")

if __name__ == "__main__":
    main()
