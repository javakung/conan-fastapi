from fastapi import FastAPI
import uvicorn

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


@app.get("/asc")
async def asc(li):
    ls = li.split(',')
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    return ls.sort()

@app.get("/desc")
async def desc(li):
    ls = li.split(',')
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    return ls.sort(reverse=True)

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