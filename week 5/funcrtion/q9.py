python_numbers = [4, 7, 2, 9, 1, 5] # Print: sum, average, minimum, maximum

def show_stats_of_the_list(list):
    max_number = max(list)
    min_number = min(list)
    sum_of_numbers = sum(list)
    average = sum_of_numbers/len(list)

    return f'the max number is:{max_number}\nthe min number is {min_number}\nthe sum of numbers is:{sum_of_numbers}\nthe average of numbers is:{average}'



print(show_stats_of_the_list(python_numbers))