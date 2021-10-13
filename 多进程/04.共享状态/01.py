from multiprocessing import Process,Value,Array
# 共享内存
def f(n,a):
    # value传入数值 arr传入的数组
    n.value=3.1415926
    for i in range(len(a)):
        a[i]=-a[i]
    


if __name__=="__main__":
    num=Value('d',0.0)
    arr=Array('i',range(10))

    p=Process(target=f,args=(num,arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])