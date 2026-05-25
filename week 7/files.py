import os

with open('diary.txt','w',encoding='utf-8') as f:
        f.write('2024-01-15 start of the week\n')
        f.write('2024-01-16 I study about files \n')
        f.write('2024-01-17 complete exersize\n')
#with open('diary.txt','r',encoding='utf-8') as f:
 #       content = f.read()
  #      print(content)



def add_entry(filename, date, content):
    with open(filename,'a',encoding='utf-8') as f:
         f.write(date)
         f.write(content)
     



add_entry("diary.txt","2024-01-18 " ,'I finish q1 ')

def search_diary(filename, keyword):
     '''
     keyword מחזיר רשימה של שורות שמכילות את
    '''
     with open(filename,'r',encoding='utf-8') as f:
        lines = f.readlines()
        lines_with_keyword = []
        for line in lines:
              if keyword in line:
                    lines_with_keyword.append(line)
        return lines_with_keyword

     
print(search_diary('diary.txt','I'))

def safe_read_diary(filename):
    if not os.path.exists(filename):
         raise FileNotFoundError('filename not in the system')


with open('diary.txt','r',encoding='utf-8') as f:
        content = f.read()
        print(content)

safe_read_diary('diary.t')