# coding: utf-8

class Tanks:
	model = str('t34')
	wheels = int(18)
	speed = int(0)
	truck = bool(True)
	def status(self, speed):
		self.speed = speed
		if self.speed != 0 and self.truck == True:
			print('Speed:',self.speed,'Model:', self.model, 'Moving!!!')
		else:
			print('Speed:',self.speed,'Model:', self.model, 'Standing.')	
		
class Cars:
	model = 'e30'
	wheels = 4
	speed = 0
	def status(self, speed):
		self.speed = speed
		if self.speed != 0 and self.wheels >= 4:
			print('Speed:',self.speed,'Model:', self.model, 'Moving!!!')
		else:
			print('Speed:',self.speed,'Model:', self.model, 'Standing.')			

class Carts:
	wheels = 2
	speed = 0
	model = 'typeA'
	def status(self, speed):
		self.speed = speed
		if self.speed != 0:
			print('Speed:',self.speed,'Model:', self.model, 'Moving!!!')
		else:
			print('Speed:',self.speed,'Model:', self.model, 'Standing.')	

#Objects association to classes:
obj1 = Tanks()
obj2 = Cars()
obj3 = Carts()

#Some action with objects:
obj2.speed = 90
obj1.truck = False

#Creating list of objects:
lst = [obj1, obj2, obj3]

#Getting objects status:
for a in lst:
	a.status(a.speed)