class demo:
	def __init__(self,msg):
		self.msg=msg
	def __str__(self):
		return f"Hello_{self.msg}"
	def addition(self):
		return 3+3

a=demo(msg="KF")
print(a)

