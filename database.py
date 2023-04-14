import pandas as pd
from bs4 import BeautifulSoup
import requests


def make_database():
    df=pd.DataFrame()
    q=[]
    a=[]
    for i in range (1,1000):
        i=str(i)
        number = i.zfill(4)
        url = 'https://walkccc.me/LeetCode/problems/{}/'.format(number)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        code_element = soup.find('code')
        if code_element == None:
            continue
        else:
            code = code_element.text.strip()
        print(number)
        print(code)
        q.append(code)
        a.append(i)
    df['Question']=q
    df['Answer']=a
    df.to_csv('/Users/eemanmajumder/code_shit/leapcode/LeapCode/Database/database.csv')

make_database()