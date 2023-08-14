import random
class demo:
	def __init__(self,msg):
		self.msg=msg
	def __str__(self):
		return f"Hello_{self.msg}"
<<<<<<< HEAD
	def addition(self):
		return 3+3
=======
>>>>>>> eb0bcafe935da8f798036e5fefc736713ee0a236
	def get_random()->int:
		return random.randrange(1,10)

a=demo(msg="KF")
print(a)

