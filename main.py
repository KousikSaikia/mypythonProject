# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


var1 = 60


def cal_secs(days_count):
    return f"There are {days_count * var1} mins in a {days_count} hours"


user_input = input("Please enter a value\n")

my_var = cal_secs(int(user_input))
print(my_var)
