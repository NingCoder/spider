from multiprocessing import Process,Queue
# 使用队列通信
def f(q):
    q.put(['遗憾在',21,"岁"])

if __name__=="__main__":
    q=Queue()
    p=Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()