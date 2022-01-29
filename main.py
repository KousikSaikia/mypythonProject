# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


var1 = 60


def cal_secs(days_count):
        return f"There are {days_count * var1} mins in a {days_count} hours"

def validate():
    if user_input.isdigit():
        my_var = int(user_input)
        if my_var > 0:
            calucated_value = cal_secs(my_var)
            print(calucated_value)
        elif my_var == 0:
            print("You have entered 0, Please enter a positive number")
    else:
        print("This is a invalid input please input positive number")


user_input = input("Please enter a value\n")
validate()


