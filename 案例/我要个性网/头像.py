# encoding "utf-8"
import requests,threading,os,re
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'
}
#下载图片
def get_pic_link(path,index,pic):
    with open(os.path.join(path, f'{index + 1}.jpeg'), 'wb') as fp:
        fp.write(requests.get(pic, headers=headers).content)
        print(f"{title}中第{index + 1}下载成功!")

url='https://www.woyaogexing.com/touxiang/katong/index_3.html'
r=requests.get(url,headers=headers)
r.encoding=r.apparent_encoding
if r.status_code==200:
    html=etree.HTML(r.text)
    for i in html.xpath('//*[@id="main"]/div[3]/div[1]/div[2]/div'):
        #对于title进行处理
        title=re.sub(r'[》？：‘！@# “\|｜、?|(*^ω^*)]+','-',i.xpath('./a[2]/text()')[0])
        href='https://www.woyaogexing.com'+i.xpath('./a[2]/@href')[0]

        # 创建对应的文件夹
        path=os.path.join('images',title)
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
            t1=threading.Thread(target=get_pic_link,args=(path,index,pic))
            t1.start()


