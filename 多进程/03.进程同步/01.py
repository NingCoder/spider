from multiprocessing import Process,Lock

def f(l,i):
    l.acquire()

    try:
        print("num: ",i)
    finally:
        l.release()



if __name__=="__main__":
    lock=Lock()
    for i in range(10):
        # 多进程的输出很容易产生混淆。
        Process(target=f,args=(lock,i)).start()