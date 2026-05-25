def create_grades_file(filename):
    """create a txt file based on name file given 
     the file contine studants names and grades
      given : a filename
      return: None 
      """
    
    students = [
          ("Dan", [85, 90, 78]),
          ("MOMO", [92, 88, 95]),
          ("Yoni", [70, 65, 80]),
          ("Avi", [100, 95, 98]),
          ("Sara", [60, 72, 68]),
          ('Bob',[30,40,21])
          ]
    with open(filename,'w',encoding='utf-8') as f:
        for student in students:
            name, grades = student
            f.write(f'{name},')
            grades = [str(grade) for grade in grades]
            grades = ','.join(grades)   
            f.write(f'{grades}\n')
    return None
create_grades_file('grades.txt')


def calculate_averages(filename):
        '''read the filename and calculate the average of each student
        given: file name
        return: dict  {name:average}
            '''
        averages = {}
        number_of_grades = 3
        with open(filename,'r',encoding='utf-8') as f:
            for line in f:
                line = line.replace('\n','')
                line = line.split(',')
                name = line.pop(0)
                line = [int(grade) for grade in line]
                avrage_grades = sum(line) / len(line)
                averages[name] =  avrage_grades

        return averages


results = calculate_averages('grades.txt')
for name, avg in results.items():
    print(f'{name}: {avg:.1f}')


def save_results(averages, output_filename):
    '''
:filename_output כותבת לקובץ
שורה ראשונה: כותרת
שורות הבאות: שם וממוצע, ,ממויי ממגבו ללנמו
   '''
    with open(output_filename,'w',encoding='utf-8') as f:
          f.write('=== Student Results === \n\n')
          sort_of_avrage = sorted(averages.values(),reverse=True)
          for grade_average_sorted in sort_of_avrage:  
                for name,avrage in averages.items():       
                    if avrage == grade_average_sorted:
                       f.write(f'{name},{grade_average_sorted}\n')
                 
               
            
averages = calculate_averages('grades.txt')
save_results(averages, 'results.txt')

def add_statictics(avrages_student:dict,filename:str):
    with open('results.txt','a',encoding='utf-8') as f:
        number_of_students = len(avrages_student)
        avrage_class = sum(avrages_student.values()) / number_of_students
        max_grade = max(avrages_student.values())
        lowest_grade = min(avrages_student.values())
        highest_student_name = None
        lowest_student_name = None
        passing_grade = 60
        num_of_passeds_students = 0
        for name, average in avrages_student.items():
            if average == max_grade:
                highest_student_name = name
            elif average == lowest_grade:
                lowest_student_name = name
            if average >= passing_grade :
               num_of_passeds_students += 1

        f.write('\n=== Statistics ===\n\n')
        f.write(f'''Class avrage: {avrage_class}
Highest grade: {highest_student_name}: {max_grade}
Lowest grade: {lowest_student_name}: {lowest_grade}
passing (>=60): {num_of_passeds_students}/{number_of_students}''')          
        
                    




print(add_statictics(averages,'results.txt'))