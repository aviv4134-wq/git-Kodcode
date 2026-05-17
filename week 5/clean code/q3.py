

def manage_students(names, grades, new_name, new_grade):
    # validation
    if not is_name_valid(new_name):
        return False

    if not is_grade_valid(new_grade):
        return False

    # add student
    add_student_grade_to_grades(grades,new_grade)
    # calculate stats
    total,average,top_count,failing_count =calculate_stats(grades)
    # print report
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

    # save to file
    save_file(names,grades)

    return names, grades


def is_name_valid(new_name):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
def is_grade_valid(new_grade):
    max_grade = 100
    min_grade = 0
    if new_grade < min_grade or new_grade > max_grade:
        print("Error: grade must be 0-100")
        return False
def add_student_grade_to_grades(grades,new_grade):
    grades.append(new_grade)
def calculate_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)
    return total,average,top_count,failing_count
def print_stats(names,grades,average,top_count,failing_count):
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

def save_file(names,grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")
