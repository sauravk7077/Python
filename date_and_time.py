
#Imports datetime and timedelta from datetime
from datetime import datetime, timedelta

# current_date = datetime.now()
# #one_date = timedelta(days=1)
# #current_date = current_date - one_date
# #print("It is now : {}".format(str(current_date)))

# day = str(current_date.day)
# month = str(current_date.month)
# year = str(current_date.year)
# print(day,":",month,":",year)

date_str = input("When is your birthday?")
date = datetime.strptime(date_str, "%d/%m/%Y")
print(f"Birthday: {str(date)}")

one_week = timedelta(weeks=1)
week_before_birthday = date - one_week
print(f"A week before birthday is {str(week_before_birthday)}")