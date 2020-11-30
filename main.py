# Author: Chatchawal Sangkeettrakarn
# Date: September 20,2020.

from fastapi import FastAPI
import uvicorn
import numpy as np
import re
import math
import requests
from bs4 import BeautifulSoup
from fastapi.responses import PlainTextResponse

app = FastAPI()


def result(res):
    return {"result": res}


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


@app.get("/pow")
async def pow(a: int = 0, b: int = 0):
    return math.pow(a, b)


@app.get("/BMI")
async def bmi(h: int = 1, w: int = 0):
    des = ""
    h = (h / 100) ** 2
    bmi = w / h

    if (bmi < 29.9 and bmi > 25.0):
        des = "โรคอ้วน"
    elif (bmi < 24.9 and bmi > 23.0):
        des = "น้ำหนักเกิน"
    elif (bmi < 22.5 and bmi > 18.5):
        des = "สมส่วน"
    elif (bmi < 18.5):
        des = "น้ำหนักต่ำกว่าเกณฑ์"
    else:
        des = "โรคอ้วนอันตราย"

    jsonout = {'bmi': f'{bmi:.2f}', 'des': des}
    return jsonout


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


@app.get("/NormalizeNumber")
async def number(Num: str = ""):
    if '.' in Num:
        nsplit = Num.split('.')
        if (',' in nsplit[0]):
            n2split = nsplit[0].split(',')
            for ch in n2split[1::]:
                if len(ch) == 3:
                    a1 = float(Num.replace(',', ''))
                    status = 'True'
                else:
                    a1 = Num
                    status = 'False'
        else:
            a1 = float(Num.replace(',', ''))
            status = 'True'
    elif len(Num) == 3:
        a1 = float(Num.replace(',', ''))
        status = 'True'
    elif ',' in Num:
        Csplit = Num.split(',')
        for b in Csplit[1::]:
            if len(b) == 3:
                a1 = float(Num.replace(',', ''))
                status = 'True'
            else:
                a1 = Num
                status = 'False'
    else:
        a1 = Num
        status = 'False'

    jsonout = {'a1': a1, 'status': status}
    return jsonout


@app.get("/validation-ctzid")
async def validation_ctzid(text):
    if(len(text) != 13):
        return False

    sum = 0
    listdata = list(text)

    for i in range(12):
        sum += int(listdata[i])*(13-i)

    d13 = (11-(sum % 11)) % 10

    return d13 == int(listdata[12])


@app.get("/validation-email")
async def validation_email(text):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, text):
        return True
    else:
        return False


@app.get("/google-search", response_class=PlainTextResponse)
def google_search(text):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    url = 'https://www.google.com/search?q=' + str(text)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')

    t = soup.findAll('div', {'class': "r"})
    i = 0
    result = ''
    for a in t:
        href = a.a['href']
        head = a.h3.text
        result = result + head + '<br>' + href + '<br><br>'
        i += 1
        if(i >= 5):
            break

    return(result)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80, debug=True)
