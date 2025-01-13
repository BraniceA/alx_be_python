from datetime import datetime
  
def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(current_date)

display_current_datetime()

# PROMPT THE USER TO ENTER NUMBER OF DAYS(AS AN INTEGER)
number_of_days = int(input("Enter number of days: "))

def calculate_future_date():
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days = number_of_days)
    future_date = future_date.strftime("%Y-%m-%d")

    print(future_date)

calculate_future_date()
