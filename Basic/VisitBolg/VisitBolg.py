#encoding:utf-8
import webbrowser as web
import time
import os

def startVisit():
    url = "https://blog.csdn.net/lzqg1990/article/details/"
    ids = ["93018433", "94006663", "88092773"]
    urllist = []
    for id in ids:
        urllist.append(url + id)
    print(urllist)

    for j in range(0,10000):#设置循环的总次数
        i=0
        while i < 1 :  #一次打开浏览器访问的循环次数
            for url in urllist:
                web.open(url)  #访问网址地址，语法 .open(url,new=0,Autorasise=True),设置 new 的值不同有不同的效果0、1、2
                i=i+1
                time.sleep(20)  #设置每次打开新页面的等待时间
        else:
            time.sleep(20) #设置每次等待关闭浏览器的时间
            os.system('taskkill /IM chrome.exe')  #你设置的默认使用浏览器，其他的更换下就行

if __name__ == '__main__':
    startVisit()

