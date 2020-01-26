import _thread
import time
def print_time(threadName,delay):
	count=0
	while count<5:
		time.sleep(delay)
		count+=1
		print(threadName,time.ctime(time.time()))

try:
	_thread.start_new_thread(print_time,("thread1",2,))
	_thread.start_new_thread(print_time,("thread2",4,))
except :
	print("error unable to strat the thread")
while 1 :
	pass

