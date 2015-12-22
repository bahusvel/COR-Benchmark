__author__ = 'denis'

from cor.api import CORModule, Message
import threading
import time

INTERVAL = 1000


class CorBurner(CORModule):

	def receiver(self, message):
		self.counter += 1
		if (self.counter % INTERVAL) == 0:
			print("Received: " + str(self.counter))

	def burner(self):
		ptime = time.time()
		ntime = time.time()+1

		for i in range(0, self.messages):
			if (i % INTERVAL) == 0:
				print(str(INTERVAL/(ntime - ptime)) + " MPS")
				ptime = ntime
				ntime = time.time()
			self.messageout(Message("BENCHMARK.MPS", {"HELLO": i}))

	def __init__(self, messages=1000000, **kwargs):
		super().__init__(**kwargs)
		self.messages = messages
		self.counter = 0
		self.add_topics({"BENCHMARK.MPS": self.receiver})
		self.t = threading.Thread(target=self.burner)
		self.t.start()
