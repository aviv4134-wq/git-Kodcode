list_of_numbers= [1, 2, 2, 3, 1, 4, 3]
list_1= [1, 2, 3, 4,7] 
list_2 = [3, 4, 5, 6,7] 
name = 'ari'
words = "The cat and the dog and the bird"


def q1(list_of_numbers):
    return list(set(list_of_numbers))

def q2(list_of_numbers):
    unique_numbers = set(list_of_numbers)
    return len(unique_numbers)

def q3(list_1,list_2):
   numbers_on_both = set(list_1) & set(list_2)
   return sorted(list(numbers_on_both))

def q4(list_1,list_2):
        unique_numbers= set(list_1) ^ set(list_2)
        return unique_numbers

def q5(list_1,list_2):
    numbers_on_both =  set(list_1) & set(list_2)
    if list(numbers_on_both) == list_1:
         return True
    return False

def q6(name):
    if len(set(name)) != len(name):
       return False
    return True

def q7(list_of_numbers):
    seen = set()
    for num in list_of_numbers:
        if num in seen:
            return num
        seen.add(num)
    return None

def q8(words:str):
    words = words.lower().split()
    return len(set(words))
#    
def q9(list_of_numbers :list, target):
      seen = set()
      for number in list_of_numbers:
          comlement = target - number
          if comlement in seen:
              return True
          seen.add(number)
      return False

def q10(list_1, list_2):
    seen = set()
    list_1.extend(list_2)
    for value in list_1:
        if value not in seen:
            seen.add(value)
        else:
            seen.remove(value)
    return list(seen)


         


print(q1(list_of_numbers))
print(q2(list_of_numbers))
print(q3(list_1,list_2))
print(q4(list_1,list_2))
print(q5(list_1,list_2))
print(q6(name))
print(q7(list_of_numbers))
print(q8(words))
print(q9(list_of_numbers, 6))
print(q10(list_1,list_2))