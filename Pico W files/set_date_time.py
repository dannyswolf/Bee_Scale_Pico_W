# from Chat Gpt
import ntptime
import utime
import time

def get_date_time():
    try :
        time.sleep(2)
        # print("get_date_time")
        ntptime.settime()  # UTC time
        current_datetime = time.localtime()


        # Extract the components of the date and time
        year, month, day, hour, minute, second, _, _ = current_datetime

        # Print the date and time
        # print("Current Date: {}/{}/{}".format(day, month, year))
        # print("Current Time: {}:{}:{}".format(hour, minute, second))
        # +3 ωρες για Ελλάδα
        current_datetime = f"{day}/{month}/{year} {hour+3}:{minute}:{second}"
        # print("current_datetime", current_datetime)
        return current_datetime
    except Exception as e:
        # filename = "log.txt"
        # file = open(filename, "a")
        # file.write(f"\nDateTime Exception: {e}")
        # file.close()
        return  f'No Date TIme Exception: {e}'
