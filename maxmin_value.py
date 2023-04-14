LIST_VALUE = []

while True:
    try:
        user_value = int(input("Enter value: "))
        LIST_VALUE.append(user_value)
    except ValueError:
        user_value_str = input("Invalid input")
        if user_value_str == 'done':
            print(max(LIST_VALUE))
            print(min(LIST_VALUE))
            break







