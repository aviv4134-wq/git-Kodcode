
arry = [0,0,0,0,1,0,3,0,6,0]
def order_arry(arry):
    count_zeros = 0
    while 0 in arry:
        arry.remove(0)
        count_zeros +=1

    for n in range(count_zeros):
        arry.append(0)
    return arry


print(order_arry(arry))