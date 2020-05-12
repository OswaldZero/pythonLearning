import multiprocessing
import time

def worker_1(sec):
    print("worker_1 start")
    time.sleep(sec)
    print("worker_1 end")

def worker_2(sec):
    print("worker_2 start")
    time.sleep(sec)
    print("worker_2 end")

def worker_3(sec):
    print("worker_3 start")
    time.sleep(sec)
    print("worker_3 end")

def worker_4(sec):
    print("worker_4 start")
    time.sleep(sec)
    print("worker_4 end")

def worker_5(sec):
    print("worker_5 start")
    time.sleep(sec)
    print("worker_5 end")

def worker_6(sec):
    print("worker_6 start")
    time.sleep(sec)
    print("worker_6 end")

def worker_7(sec):
    print("worker_7 start")
    time.sleep(sec)
    print("worker_7 end")

def worker_8(sec):
    print("worker_8 start")
    time.sleep(sec)
    print("worker_8 end")


p1=multiprocessing.Process(target=worker_1,args=(3,))
p2=multiprocessing.Process(target=worker_2,args=(3,))
p3=multiprocessing.Process(target=worker_3,args=(3,))
p4=multiprocessing.Process(target=worker_4,args=(3,))
p5=multiprocessing.Process(target=worker_5,args=(3,))
p6=multiprocessing.Process(target=worker_6,args=(3,))
p7=multiprocessing.Process(target=worker_7,args=(3,))
p8=multiprocessing.Process(target=worker_8,args=(3,))



if __name__ == "__main__":
    print("The number of cpu is {}".format(multiprocessing.cpu_count()))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    for i in multiprocessing.active_children():
        print("child p.name:{} p.id:{}".format(i.name,str(i.pid()))         