import datetime
import random
earlier_date = date(2017, 6, random.randint(1, 25))
later_date = date(2017, 6, random.randint(earlier_date.day + 1, 28))

earlier_date = datetime.datetime.strptime(earlier_date, "%Y-%m-%d").date()
later_date = datetime.datetime.strptime(later_date, "%Y-%m-%d").date()

days_between = (later_date - earlier_date).days()

print(type(days_between))

print("There are", days_between.days, "days between", earlier_date, "and", later_date)
