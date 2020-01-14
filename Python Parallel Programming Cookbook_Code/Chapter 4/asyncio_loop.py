#
# Asyncio.loop - Chapter 4 Asynchronous Programming
#


import asyncio
import datetime
import time

def function_1(end_time, loop):
    print ("function_1 called")
    print (end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_2, end_time, loop)
    else:
        loop.stop()

def function_2(end_time, loop):
    print ("function_2 called ")
    print (end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_3, end_time, loop)
    else:
        loop.stop()

def function_3(end_time, loop):
    print ("function_3 called")
    print (end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_1, end_time, loop)
    else:
        loop.stop()

def function_4(end_time, loop):
    print ("function_5 called")
    print (end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_4, end_time, loop)
    else:
        loop.stop()

loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
end_loop_1 = loop.time() + 9.0
loop.call_soon(function_1, end_loop_1, loop)
#loop.call_soon(function_4, end_loop_1, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()

