import datetime as dt
import math
from geometry import circle
from geometry import rectangle


_count = 0
def bump():
    global _count
    _count += 1

def value():
    return _count
bump()
bump()
bump()
#print(value())

def make_counter():
    countt = 0
    def inner():
        nonlocal countt
        countt += 1
        print( countt)
    return inner

c = make_counter()
c()

print(dt.datetime.now())

#def public(m):
    #return sorted[name for name in m]
def public_names(m):
    """Returns a sorted list of public attribute names on module m."""
    return sorted([name for name in dir(m) if not name.startswith('_')])
print(public_names(math))


def add_item(item, bag=None):
    if bag is None:
        bag = []  
    bag.append(item)
    return bag

print(add_item(1))

# main.py


# Calculate and print the areas
circle_area = circle.area(5)
rectangle_area = rectangle.area(4, 6)

print(f"Circle area: {circle_area}")          # Output: 78.53975
print(f"Rectangle area: {rectangle_area}")    # Output: 24
