def create_list_of_allowed_people(list_of_lists_of_pepole):
    people_allowed_to_enter = []
    allowed_age = 18
    for l in list_of_lists_of_pepole:
        name = l[0]
        age  = l[1]
        status = l[2]
        if age >= allowed_age and status:
            people_allowed_to_enter.append(name)
    return people_allowed_to_enter

people_data = [
    ["Dan", 25, True],
    ["Noa", 16, False],
    ["Yael", 30, True],
]

print(create_list_of_allowed_people(people_data))




