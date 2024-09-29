from datetime import datetime, timedelta

def display_current_datetime():
    
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():

    while True:
        try:
            days_input = input("Enter the number of days to add to the current date: ")
            number_of_days = int(days_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the number of days.")
    
    current_datetime = datetime.now()
    delta = timedelta(days=number_of_days)
    future_datetime = current_datetime + delta
    future_date = future_datetime.date()
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future_date}")

def main():

    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

