from fastapi import FastAPI
import uvicorn
import numpy as np

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
    return np.sum(ls, dtype = np.float32)

@app.get("/avg")
async def avg(li):
    ls = tonumlist(li)
    return np.average(ls)

@app.get("/mean")
async def avg(li):
    ls = tonumlist(li)
    return np.mean(ls)

@app.get("/max")
async def avg(li):
    ls = tonumlist(li)
    return np.amax(ls)

@app.get("/min")
async def avg(li):
    ls = tonumlist(li)
    return np.amin(ls)

@app.get("/ctzid-validation")
async def ctzIdValidate(ctzid):
    if(len(ctzid) != 13):
        return False
    
    num=0 
    sum=0
    num2=13
    listdata=list(ctzid)
    
    while num<12:
        sum+=int(listdata[num])*(num2-num)
        num+=1
    
    digit13 = sum%11
    
    if digit13==0:
        digit13=1
    elif digit13==1:
        digit13=0
    else:
        digit13=11-digit13
        
    if digit13==int(listdata[12]):
        return True
    else:
        return False


if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True) 