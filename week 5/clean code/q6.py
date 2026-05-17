def process_grades(names, all_grades):
    result_names,result_averages,result_statuses,result_highs,result_lows = init_variables()
    total, average, status, highest, lowest = caculate_stats(all_grades)
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]
        if not is_valid_name(name):
            continue
        if not is_valid_grade(grades,name):
            continue

        add_statistics_to_list(name,result_names,result_averages,result_statuses,result_highs,result_lows,average,status,highest,lowest)

    print_intro_report()
    print_stats_student(result_names,result_averages,result_statuses,result_highs,result_lows)
    passing_count = calculate_pass_grades(result_statuses)
    print_total_passing_grades(passing_count,result_names)
    return result_names, result_averages, result_statuses


def init_variables():
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    return result_names,result_averages,result_statuses,result_highs,result_lows

def is_valid_name(name):
    if not name:
        print(f"Error: missing name")
        return False
    return True

def is_valid_grade(grade,name):
    if not grade:
        print(f"Error: {name} has no grades")
        return False
    return True

def caculate_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    status = "pass" if average >= 56 else "fail"
    highest = max(grades)
    lowest = min(grades)
    return total,average,status,highest,lowest

def add_statistics_to_list(name,result_names,result_averages,result_statuses,result_highs,result_lows,average,status,highest,lowest):
    result_names.append(name)
    result_averages.append(round(average, 1))
    result_statuses.append(status)
    result_highs.append(highest)
    result_lows.append(lowest)

def print_intro_report():
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)

def print_stats_student(result_names,result_averages,result_statuses,result_highs,result_lows ):
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()

def calculate_pass_grades(result_statuses):
    passing_count = sum(1 for s in result_statuses if s == "pass")
    return passing_count

def print_total_passing_grades(passing_count,result_names):
    print(f"Total passing: {passing_count}/{len(result_names)}")


names = ['avi','bob','levi']
grades = [100,89,0]
process_grades(names,grades)