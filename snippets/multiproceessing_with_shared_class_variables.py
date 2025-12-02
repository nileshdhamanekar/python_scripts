import multiprocessing
from multiprocessing import Process, Array

class Test:
	def __init__(self):
		pass

	def update_list(self, i, my_list):
		print("Inside update_list, i={0}, num={1}".format(i, my_list[i]))
		my_list[i] = my_list[i] * my_list[i]
		print("Updated list: {0}".format(my_list))

	def update_lists(self):
		manager = multiprocessing.Manager()
		self.my_list = manager.list([10,20,30,40,50])
		print("Before: {0}".format(self.my_list))
		processes = []
		for index, num in enumerate(self.my_list):
			process = Process(target=self.update_list, args=(index, self.my_list))
			processes.append(process)
			process.start()
		for process in processes:
			process.join()
		print(self.my_list)

t = Test()
t.update_lists()