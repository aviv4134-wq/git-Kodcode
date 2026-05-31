from fastapi import FastAPI

app = FastAPI()

@app.get('/calc/{a}/{op}/{b}')
def result(a,op,b):
    try:
        a,b= int(a),int(b)
        if op == 'add':
           result = a + b
        elif op == 'sub':
            result = a - b
        elif op == 'mul':
            result = a * b
        elif op == 'div':
            result = a / b
    except ZeroDivisionError:
        return 'dont enter 0'
    except Exception as e:
        return e

    return {'operation': op,'result':result}