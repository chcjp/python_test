#encoding:utf-8

#pip install bs4 breautifulsoup4
#pip install 
import requests
from bs4 import BeautifulSoup
import json
import time

def main():
    headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Host':'www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest'
    }
    form_data = {
        'first':'true',
        'pn':'1',
        'kd':'python'
    }

    positions = []

    for x in range(1,31):
        form_data = {
            'first':'true',
            'pn':x,
            'kd':'python'
        }
        result = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false',headers=headers,data=form_data)
        json_result = result.json()
        page_positions = json_result['content']['positionResult']['result']
        positions.extend(page_positions)
        print('-'*30+str(x))
        print(page_positions)
        print('-'*30+str(x))
        #1.要么把sleep时间改大一点
        #2.每次请求不要请求太多，分多次请求
        time.sleep(2)

    line = json.dumps(positions, ensure_ascii=False)
    with open('lagou.json','wb') as fp:
        fp.write(line.encode('utf8'))

if __name__ == '__main__':
    main()
