import random
class demo:
	def __init__(self,msg):
		self.msg=msg
	def __str__(self):
		return f"Hello_{self.msg}"
	def get_random()->int:
		return random.randrange(1,10)

a=demo(msg="KF")
print(a)

