tuple_1 = (1,2,3,4,5,6,5,9)
tuple_2 = (1,2,3,4,5)
def sum_of_tuple(tuple_1):
    sum_of_tuple = 0
    for number in tuple_1:
        sum_of_tuple += number
    return sum_of_tuple

def max_number_of_tuple(tuple_1):
     max_number = 0
     for number in tuple_1:
         if number > max_number:
             max_number = number
     return max_number

def count_duplicats(tuple_1,value_init):
    count_duplicats = 0
    for number in tuple_1:
        if number == value_init:
            count_duplicats += 1
    return value_init

def reverse_tuple(tuple_1):
     reversed_tuple = []
     for index in range(len(tuple_1)-1,-1,-1):
         reversed_tuple.append(tuple_1[index])
     reversed_tuple = tuple(reversed_tuple)
     return reversed_tuple

def switch_pairs(tuple_1):
    switched_pairs:list = []
    for index in range(len(tuple_1)):
        if index % 2 != 0:
            switched_pairs.append(tuple_1[index])
            switched_pairs.append(tuple_1[index - 1])
    return switched_pairs
                    
def find_min_max_number(tuple_1):
    max_number = 0
    min_number = tuple_1[0]
    for number in tuple_1:
        if number > max_number :
            max_number = number
        if number < min_number :
            min_number = number
    return max_number, min_number

def find_distance(point_1,point_2):
    x1, y1 = point_1
    x2, y2 = point_2

    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    return distance 

def merge_and_sort_tuples(tuple_1,tuple_2):
    tuple_1,tuple_2 = list(tuple_1),list(tuple_2)
    tuple_1.extend(tuple_2)
    tuple_1.sort()
    merged_tuples = tuple(tuple_1)
    return merged_tuples

def items_to_count(tuple_values):
    list_of_pairs = []
    for i in tuple_values:
        count = tuple_values.count(i)   
        if (i,count) not in list_of_pairs:
           list_of_pairs.append((i,count))
    return tuple(list_of_pairs)

def rotate_tuple(tuple_1,k):
    try:
        tuple_1[k-1]

        rotate_list:list = []    
        for index in range(-k,len(tuple_1) - k):
           rotate_list.append(tuple_1[index])
        rotate_tuple = tuple(rotate_list)
        return rotate_tuple
    except:
        print('enter k that positive and equel or less to the length of tuple')


    



if __name__ == "__main__":
    #print(sum_of_tuple(tuple_1))
    #print(max_number_of_tuple(tuple_1))
    #print(count_duplicats(tuple_1,4))
    #print(reverse_tuple(tuple_1))
    #print(switch_pairs(tuple_1))
    #print(find_min_max_number(tuple_1))
    point_1 = (0,0)
    point_2 = (3,4)
    #print(find_distance(point_1,point_2))
    tuple_values =  ("a", "b", "a", "c", "b", "a")
    #print(merge_and_sort_tuples(tuple_1,tuple_2))
    #print(items_to_count(tuple_values))
    print(rotate_tuple(tuple_1,3))
 