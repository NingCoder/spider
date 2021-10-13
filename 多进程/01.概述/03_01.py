import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    #进程的启动方式 method  应该是 'fork', 'spawn（可在Unix和Windows上使用）', 'forkserver'
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()