import requests,os,re,asyncore
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'
}

async def Download_hero_pic(skils,path):
    if 'skinName'in skils:
        path=os.path.join(path,skils['skinName'])
        if not os.path.exists(path):
            await os.makedirs(path)
        
        pic_ls=['iconImg','loadingImg','mainImg','sourceImg','videoImg']
        for i,j in zip(skils[skils['skinName']],pic_ls):
            async with open(os.path.join(path,f"{j}.jpg"),'wb')as fp:
                fp.write(await requests.get(i,headers=headers).content)

def Get_hero_info(heroId,path):
    Detail_hero_page='https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(heroId)
    # Detail_hero_page='https://game.gtimg.cn/images/lol/act/img/js/hero/1.js'
    r=requests.get(Detail_hero_page,headers=headers)
    if r.status_code==200:
        res=r.json()['skins']

        for i in res:
            #不打印炫彩皮肤 进行判断选择
            skils={}
            if i['chromaImg']=='':
                
                name=re.sub(r'[》？：‘！@# “✨\|｜、 |(*^ω^*?]+','-',i['name'])
                skils['skinName']=name
                skils[name]=[i['iconImg'],i['loadingImg'],i['mainImg'],i['sourceImg'],i['videoImg']]
            # Download_hero_pic(skils,path)
            future_to_url={}
            with ThreadPoolExecutor(max_workers=5)as t:
                pass
                # t.submit(Download_hero_pic,skils,path)
def main():
    heros_link='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    r=requests.get(heros_link,headers=headers)
    if r.status_code==200:
        res=r.json()['hero']
        for i in res:
            heroId=i['heroId']
            name=i['name']
            print(heroId,name," 下载完成!")
            path=os.path.join("LOL壁纸下载",name)
            if not os.path.exists(path):
                os.makedirs(path)

            with ThreadPoolExecutor(max_workers=5)as t:
                t.submit(Get_hero_info(heroId,path))
           
if __name__ =="__main__":
   with ProcessPoolExecutor(max_workers=5) as p:
        p.submit(main())
    