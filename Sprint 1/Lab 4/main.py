from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():
    return {
            "message: Welcome David's API"
           }



@app.get("/sum/")

def sum(n1: int, n2: int):

    result = n1 + n2
    
    return {
            "result": f"The sum of the numbers is {result}"
           }



@app.get("/subtraction/")

def subtraction(n1: int, n2: int):

    result = n1 - n2
    
    return {
            "result": f"The subtraction of the numbers is {result}"
           }



@app.get("/multiplication/")

def multiplication(n1: int, n2: int):

    result = n1 * n2
    
    return {
            "result": f"The multiplication of the numbers is {result}"
           }



@app.get("/division/")

def division(n1: int, n2: int):

    if n1 == 0 or n2 == 0 :
        result = "an error because you can't use 0"
    else:
        result = n1 // n2
    
    
    return {
            "result": f"The division of the numbers is {result}"
           }