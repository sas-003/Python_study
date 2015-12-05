# coding: utf-8
import random

class Animal:
	quantity = 0			# in pieces
	total_sound = 0 		# in Db
	total_eaten_cash = 0 	# in $
	total_produced_cash = 0 # in $
	total_ran_km = 0		# in Km
	total_product = 0		# in pieces

	def passed_month(self, months):
		self.total_eaten_cash += self.quantity * self.eats_cash * months * random.uniform(0.9, 1.3)
		self.total_produced_cash += self.quantity * self.produce_cash * months * random.uniform(0.8, 1.2)
		self.total_ran_km += self.quantity * self.run_speed * months * random.uniform(0, 1.3)
		self.total_sound += self.quantity * self.sound * months * random.uniform(0, 1)
		self.total_product += self.quantity * self.product * months * random.randrange(1, 3)
	
	def __init__(self):
		a = self.spiece + ' quantity: '
		self.quantity = int(input(a))
		
class Duck(Animal):
	spiece = 'Ducks'
	run_speed = 3600 * 24 * 30 	# in 'Km per month'
	sound = 2300			# in 'Db per month'
	eats_cash = 80			# in '$ per month'
	produce_cash = 130 		# in '$ per month'
	product = 65			# in pieces per month
	prod_type = 'eggs'
	
class Cow(Animal):
	spiece = 'Cows'	
	run_speed = 1800 * 24 * 30
	sound = 1800
	eats_cash = 200
	produce_cash = 300
	product = 200
	prod_type = 'milk'
	
class Dog(Animal):	
	spiece = 'Dogs'
	run_speed = 6000 * 24 * 30
	sound = 4000
	eats_cash = 40
	produce_cash = 0
	product = 0
	
class Farm:
	current_cash = 0
	total_farm_sound = 0
	total_farm_eaten_cash = 0
	total_farm_produced_cash = 0
	total_farm_ran_km = 0
	lifetime = 0
	
	def passed_month(self, months):
		for i in animal_lst:
			i.passed_month(months)
			self.total_farm_sound += i.total_sound
			self.total_farm_eaten_cash += i.total_eaten_cash
			self.total_farm_produced_cash += i.total_produced_cash
			self.total_farm_ran_km += i.total_ran_km
			try:
				print ('Produced: ', i.total_product, i.prod_type)
			except AttributeError:
				pass
		self.lifetime += months
	
	def current_report(self):
		print('Sound made(Db): 	', round(self.total_farm_sound))
		print('Distance made(Km): 	', round(self.total_farm_ran_km))
		print('Cash lost($): 		', round(self.total_farm_eaten_cash))
		print('Cash produced($): 	', round(self.total_farm_produced_cash))
		print('Farm lifetime: 	', self.lifetime, 'months.')
		print('Animals on farm: ')
		for i in animal_lst:
			print(i.spiece, i.quantity)

ducks = Duck()
cows = Cow()
dogs = Dog()

animal_lst = []
animal_lst.append(ducks)
animal_lst.append(cows)
animal_lst.append(dogs)

myfarm = Farm()
m = input('Enter farms lifetime [digits]: ')

myfarm.passed_month(int(m))
myfarm.current_report()