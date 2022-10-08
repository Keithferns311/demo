class demo:
	def __init__(self,msg):
		self.msg=msg
	def __str__(self):
		return f"Hello_{self.msg}"

a=demo(msg="KF")
print(a)

