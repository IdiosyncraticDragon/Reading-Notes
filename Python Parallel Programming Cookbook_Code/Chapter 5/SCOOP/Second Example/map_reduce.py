"""
Compare SCOOP MapReduce with a serial implementation
"""
import operator
import time

from scoop import futures


def simulateWorkload(inputData):
    time.sleep(0.01)
    return sum(inputData)

def CompareMapReduce():
    mapScoopTime = time.time()
    res = futures.mapReduce(
        simulateWorkload,
        operator.add,
        list([a] * a for a in range(1000)),
    )
    mapScoopTime = time.time() - mapScoopTime
    print("futures.map in SCOOP executed in {0:.3f}s \
           with result:{1}".format(
        mapScoopTime,
        res
        )
    )

    mapPythonTime = time.time()
    res = sum(
        map(
            simulateWorkload,
            list([a] * a for a in range(1000))
        )
    )
    mapPythonTime = time.time() - mapPythonTime
    print("map Python executed in: {0:.3f}s \
           with result: {1}".format(
        mapPythonTime,
        res
        )
    )    

if __name__ == '__main__':
    CompareMapReduce()
