from fastapi import FastAPI

app = FastAPI()

grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}

@app.get('/students')
def show_all_student():    
     return grades
@app.get('/students/top')
def top_grade_student():
     top_grade = 0 
     top_name = None
     for student in grades:
        if grades[student]['grade'] > top_grade:
            top_grade = grades[student]['grade']
            top_name = grades[student]
     return  f'{top_name}'
@app.get('/students/average')
def show_grades_average():
    count_of_grades = len(grades)
    all_grades = 0
    for student in grades:
        all_grades += grades[student]['grade']
    average_grades = all_grades / count_of_grades
    return f'the average of the class is {average_grades}'

@app.get('/students/count')
def count_students():
    count_students = len(grades)
    return f'the number of students is {count_students} '

@app.get('/students/{student_id}')
def find_student(student_id):
        return grades[student_id]

