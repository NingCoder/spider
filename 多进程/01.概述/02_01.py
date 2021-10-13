from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    # join()方法可以在当前位置阻塞主进程，带执行join()的进程结束后再继续执行主进程的代码逻辑。
    p.join()