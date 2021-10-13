from multiprocessing import Process,Pipe
# 使用管道通信
def f(conn):
    conn.send(['遗憾在',21,"岁"])
    conn.close()


if __name__ =="__main__":
    # 返回一对 Connection 对象 (conn1, conn2) ， 分别表示管道的两端。
    parent_conn,child_conn=Pipe()
    p=Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
