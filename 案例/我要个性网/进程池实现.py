# encoding "utf-8"
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests,os,re,time,random
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'
}
#下载图片
def get_pic_link(path,index,pic,title):
    with open(os.path.join(path, f'{index + 1}.jpeg'), 'wb') as fp:
        fp.write(requests.get(pic, headers=headers).content)
        print(f"{title}中第{index + 1}下载成功!")

def get_mainPage(url,page):
    r=requests.get(url,headers=headers)
    r.encoding=r.apparent_encoding
    if r.status_code==200:
        html=etree.HTML(r.text)
        for i in html.xpath('//*[@id="main"]/div[3]/div[1]/div[2]/div'):
            #对于title进行处理 因为windows系统对于 文件名创建有要求 剔除特殊字符

            # 提醒:如果头像数据不完全下载的话 很有可能是title处理不到位
            title=re.sub(r'[》？：‘！@# “✨\|｜、|(*^ω^*?]+','-',i.xpath('./a[2]/text()')[0])
            href='https://www.woyaogexing.com'+i.xpath('./a[2]/@href')[0]

            # 创建对应的文件夹
            path=os.path.join('image',os.path.join(page,title))
            if not os.path.exists(path):
                os.makedirs(path)
            else:
                continue

            res=requests.get(href,headers=headers)
            res.encoding=res.apparent_encoding
            html=etree.HTML(res.text)
            for index,i in enumerate(html.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/ul/li')):
                pic='https:'+i.xpath('./a/@href')[0]
                #借用简单的多线程 直接下载文件!
                # t1=threading.Thread(target=get_pic_link,args=(path,index,pic))
                # t1.start()
                time.sleep(random.random()) #时间间隔停息 避免ip频繁
                # 使用线程池
                with ThreadPoolExecutor(max_workers=7) as t:
                    t.submit(get_pic_link,path,index,pic,title)


if __name__=="__main__":
    urls=[]
    for i in range(1,6):
        if i==1:
            urls.append('https://www.woyaogexing.com/touxiang/katong/')
        else:
            urls.append(f'https://www.woyaogexing.com/touxiang/katong/index_{i}.html')

    # 使用进程池
    with ProcessPoolExecutor(max_workers=5) as p:
        for index,url in enumerate(urls):
            page=f'第{index+1}页'
            p.submit(get_mainPage,url,page)