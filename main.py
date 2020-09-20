#Author: Chatchawal Sangkeettrakarn
#Date: September 20,2020.

from fastapi import FastAPI
import uvicorn
import numpy as np
import re

app = FastAPI()

def result(res):
    return {"result":res}

@app.get("/")
async def main():
    return 'Hello World'

@app.get("/test")
async def test():
    return 'Test Tutorial'

@app.get("/add")
async def add(a: int = 0, b: int = 0):
    return a+b

@app.get("/mul")
async def mul(a: int = 0, b: int = 0):
    return a*b


def tonumlist(li):
    ls = li.split(',')
    for i in range(len(ls)):
        ls[i] = float(ls[i])
    return list(ls)

@app.get("/asc")
async def asc(li):
    ls = tonumlist(li)
    ls.sort()
    return ls

@app.get("/desc")
async def desc(li):
    ls = tonumlist(li)
    ls.sort(reverse=True)
    return ls

@app.get("/sum")
async def sum(li):
    ls = tonumlist(li)
    return np.sum(np.array(ls))

@app.get("/avg")
async def avg(li):
    ls = tonumlist(li)
    return np.average(ls)

@app.get("/mean")
async def mean(li):
    ls = tonumlist(li)
    return np.mean(ls)

@app.get("/max")
async def max(li):
    ls = tonumlist(li)
    return np.amax(ls)

@app.get("/min")
async def min(li):
    ls = tonumlist(li)
    return np.amin(ls)

@app.get("/validation-ctzid")
async def validation_ctzid(text):
    if(len(ctzid) != 13):
        return False
    
    sum = 0
    listdata = list(ctzid)
    
    for i in range(12):
        sum+=int(listdata[i])*(13-i)
        
    d13 = sum%11
            
    d13 = 1 if d13==0 else 0 if d13==1 else 11-d13
    
    if d13==int(listdata[12]):
        return True
    else:
        return False

@app.get("/validation-email")
async def validation_email(text):  
  regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,text)):
        return True
    else:
        return False


if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True) 