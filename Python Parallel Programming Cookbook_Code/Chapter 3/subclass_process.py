#Using a process in a subclass – Chapter 3: Process Based Parallelism
import multiprocessing

class MyProcess(multiprocessing.Process):

    def run(self):
        print ('called run method in %s' %self.name)
        return

if __name__ == '__main__':
    jobs = []

    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()

