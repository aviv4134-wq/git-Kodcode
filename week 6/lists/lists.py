def q1(): 
   list_of_init = [1, 2, 3, 4, 5]
   sum_of_list:int = 0
   for int in list_of_init:
      sum_of_list += int
   return sum_of_list

def q2():
   list_of_init =  [3, 7, 2, 8, 5] 
   max_init = 0
   for number in list_of_init:
      if max_init < number:
         max_init = number
   return f'the max number in the list is {max_init}'
      
def q3(list_of_numbers:list,number_to_count:int):
    count_the_number = 0
    for number in list_of_numbers:
       if number == number_to_count:
          count_the_number += 1
    return count_the_number

def q4(list_of_numbers):
    reverse_list = []
    for number in range(len(list_of_numbers)-1,-1,-1):
            number = list_of_numbers[number] 
            reverse_list.append(number)
    return(reverse_list) 

def q5(list_5):
    list_no_duplicate = []
    for number in list_5:
        if number not in list_no_duplicate:
            list_no_duplicate.append(number)
    return list_no_duplicate

def q6(list_6):
    second_number = 0
    maximum_number  = max(list_6)
    for number in list_6:
        if number > second_number and number < maximum_number:
            second_number = number
    return second_number

def q7(list_5,list_6):
    list_5.extend(list_6)
    return sorted(list_5)

def q8(list_2,k):
    rotate_list = []
    for index in range(len(list_2)):
         number = list_2[index]
         if index > k:
          rotate_list.append(number)
    rotate_list.extend(list_2[:k+1])
    return rotate_list

    




list_1 = [1, 2, 3, 2, 4, 2]
list_2 = [1, 290, 3, 5, 4, 2]
list_5 =  [1, 2, 2, 3, 1, 4, 3,66,90,90] 
list_6 =  [1, 55, 2, 3, 1, 4, 3,66,99,90] 
print(list_6.sort())

if __name__ == "__main__": 
     #print(q1())
     #print(q2())
     #print(q3(list_1,2))
      #print(q4(list_2))
      #print(q5(list_5))
      #print(q6(list_6))
      #print(q7(sorted(list_5),sorted(list_6)))
      print(q8(list_2,2))