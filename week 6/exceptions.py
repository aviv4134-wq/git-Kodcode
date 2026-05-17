


def safe_init(s):
    try:
        return int(s)
    except ValueError:
        return None

def safe_devided(a,b):
    try:
        a, b = int(a),int(b)
        return a / b
    except ValueError as e:
        print(f'undefined {e} error ')
    except ZeroDivisionError:
        print('dont enter 0')

def get_value(d,key):
    try:
        return d[key]
    except KeyError:
        return 'missing'

def parse_ints(values):
    list_int:list = []
    for v in values:
        try:
            v = int(v)
            list_int.append(v)
        except ValueError:
            continue
    return list_int

def set_age(age):
    try:
        if age < 0 or age > 150:
            raise ValueError
    except TypeError:
        print('enter only int')
    else:
         return age

def retry(func, n):
   last_exception = None
   for i in range(n):
       try:
          return func()
       except Exception as e:
           last_exception = e
   raise last_exception

def count_errors(funcs:list):
    count_errors = 0
    for f in funcs:
        try:
            f()
        except Exception:
            count_errors += 1
    return count_errors

def load_config(path):
    try:
        with open(path,'r') as f:
            int(f.readline())
    except Exception as original_error:
        raise RuntimeError('failed to load config') from original_error


if __name__ == '__main__':
    #print(safe_init('d'))
    #safe_devided(1,'sd')
    #print(get_value({'a': 2 },'a'))
    #print(parse_ints(['1','w',3,'e','g']))
    #set_age(12)
    #retry(safe_init,5)
    #print(count_errors([lambda :1,lambda: 2 / 0,lambda: 2+2 ]))
    print(load_config('dasda'))

