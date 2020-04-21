#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def function(i):
    print ('called function in process: %s' %i)
    return

if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=function, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()

