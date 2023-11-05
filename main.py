from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    # Check if the list is empty
    if not users:
        return {}
    
    # Create a dictionary for days of the week and initialize empty lists
    week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    # Get the current date
    current_date = date.today()

    # Get the current day of the week (Monday - 0, Tuesday - 1, ..., Friday - 4)
    current_weekday = current_date.weekday()
    current_year = current_date.year

    for user in users:
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=current_year)
        # Check if the birthday has already occurred this year and calculate the next birthda

        if birthday_this_year < current_date :
            birthday_this_year = birthday.replace(year=current_year + 1)
        if current_date <= birthday_this_year <= current_date + timedelta(days=7):
            day_of_week = birthday_this_year.strftime("%A")

            if day_of_week in week:
                week[day_of_week].append(user["name"])
            else:
                week["Monday"].append(user["name"])

        week_with_greetings = {day_name: names for day_name, names in week.items() if names}

    return week_with_greetings


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Print the result
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
