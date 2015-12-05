# coding: utf-8
import pickle
import os

data = {
 1: ['mazda',
     'three',
     107],
 2: ['suzuki',
     'grandvitara',
     176],
 3: ['suzuki',
     'sxfour',
     107]
        }

while True:
	if not os.path.exists("data.pickle"):
		f = open('data.pickle', 'wb')
		pickle.dump(data, f)
	act = input("Choose action ([l]ist / [a]dd / [e]xit / [s]earch) ")
	if act == "l":
		with open('data.pickle', 'rb') as f:
			data = pickle.load(f)
		for i in list(data.values()):
			print(i)		
	elif act == "s":
		filter = input("Choose filter ([p]ower / [w]ord / [e]xactword) ")
		if filter == "p":
			filter2 = input("Power ([e]xact / [m]ore / [l]ess / [b]etween)? ")
			if filter2 == "e":
				sp = input("Exact power?")
				for i in list(data.values()):
					if i[2] == int(sp):
						best = i[2]
						print (i)
			elif filter2 == "m":
				sp = input("More then? ")
				for i in list(data.values()):
					if i[2] > int(sp):
						best = i[2]
						print (i)
			elif filter2 == "l":
				sp = input("Less then? ")
				for i in list(data.values()):
					if i[2] < int(sp):
						best = i[2]
						print (i)
			elif filter2 == "b":
				sp1 = input("Lower border? ")
				sp2 = input("Higher border? ")
				for i in list(data.values()):
					if int(sp2) > i[2] > int(sp1):
						best = i[2]
						print (i)
		elif filter == "w":
			word = input("Enter any word you wish: ")
			for i in list(data.values()):
				if i[0].lower().count(word.lower()) or i[1].lower().count(word.lower()):
					print (i)
		elif filter == "e":
			word = input("Enter exact word you wish: ")
			for i in list(data.values()):
				if i[0].lower() == word.lower() or i[1].lower() == word.lower():
					print (i)
		else:
			print("Wrong filter!")	 
	elif act == "a":
		ncar = []
		brand = input("Brand? (letters)")
		while not brand.isalpha():
			print("Only letters allowed!")
			brand = input("Brand? (letters)")
		else:
			ncar.append(brand)
		model = input("Model? (letters)")
		while not model.isalpha():
			print("Only letters allowed!")
			model = input("Model? (letters)")
		else:
			ncar.append(model)
		power = input("Power? (digits)")
		while not power.isdigit():
			print("Only digits allowed!")
			power = input("Power? (digits)")
		else:
			ncar.append(int(power))
		print("Car {} added".format(ncar))
		data[max(data.keys())+1] = ncar
		with open('data.pickle', 'wb') as f:
			pickle.dump(data, f)
			f.close()
	elif act == "e":
		break
