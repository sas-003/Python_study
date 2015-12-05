# coding: utf-8
import pickle, os

def pickle_load(a):
	with open(a, 'rb') as f:
		data = pickle.load(f)
	return data
	
def pickle_dump(a, data):
	with open(a, 'wb') as f:
		pickle.dump(data, f)
	f.close()
	
def input_check(phrase, datatype):
	a = input(phrase)
	if datatype == 'digit':
		while not a.isdigit():
			print(("Value should be {}").format(datatype))
			a = input(phrase)
	elif datatype == 'alpha':
		while not a.isalpha():
			print(("Value should be {}").format(datatype))
			a = input(phrase)
	return a

def act_list(a):
	data = pickle_load(a)
	for i in list(data.values()):
		print(i)

def act_add(a):
	ncar = []
	brand = input_check("Brand? (letters)", "alpha")
	ncar.append(brand)
	model = input_check("Model? (letters)", "alpha")
	ncar.append(model)
	power = input_check("Power? (digits)", "digit")
	ncar.append(int(power))
	print("Car {} added".format(ncar))
	data = pickle_load(a)
	data[max(data.keys())+1] = ncar
	pickle_dump(a, data)
	
def search_more(a):
	sp = input("More then? ")
	for i in list(pickle_load(a).values()):
		if i[2] > int(sp):
			best = i[2]
			print (i)
			
def search_less(a):
	sp = input("More then? ")
	for i in list(pickle_load(a).values()):
		if i[2] < int(sp):
			best = i[2]
			print (i)
			
def search_between(a):		
	sp1 = input("Lower border? ")
	sp2 = input("Higher border? ")
	for i in list(pickle_load(a).values()):
		if int(sp2) > i[2] > int(sp1):
			best = i[2]
			print (i)

def wrong_input():
	print("Wrong parameter given. Please try again.")

def input_main():
	a = input("Choose action ([l]ist / [a]dd / [e]dit / [d]elete / [s]earch / [q]uit) ")
	return a

def act_delete(a):
	data = pickle_load(a)
	for i in list(data.keys()):
		print(i,data[i])
	n = input("Select item number to delete: ")
	print (("Item {} was deleted").format(data.pop(int(n))))
	pickle_dump(a,data)
	
def act_edit(a):
	data = pickle_load(a)
	for i in list(data.keys()):
		print(i,data[i])
	n = input("Select item number to edit: ")
	print (("Editing item: {}").format(data[int(n)]))
	act = input("Choose what to edit ([b]rand / [m]odel / [p]ower) ")
	if act == "p":
		p = input("Enter new power: ")
		data[int(n)].pop(2)
		data[int(n)].insert(2, int(p))
		print ("Updated item: ", data[int(n)])
		pickle_dump(a,data)
	elif act == "m":
		p = input("Enter new model: ")
		data[int(n)].pop(1)
		data[int(n)].insert(1, p)
		print ("Updated item: ", data[int(n)])
		pickle_dump(a,data)
	elif act == "b":
		p = input("Enter new brand: ")
		data[int(n)].pop(0)
		data[int(n)].insert(0, p)
		print ("Updated item: ", data[int(n)])
		pickle_dump(a,data)
	else:
		wrong_input()
		
def search_main(a):
	filter = input("Choose filter ([p]ower / [w]ord / [e]xactword) ")
	if filter == "p":
		filter2 = input("Power ([e]xact / [m]ore / [l]ess / [b]etween)? ")
		if filter2 == "e":
			sp = input("Exact power?")
			for i in list(pickle_load(a).values()):
				if i[2] == int(sp):
					best = i[2]
					print (i)
		elif filter2 == "m":
			search_more(a)
		elif filter2 == "l":
			search_less(a)
		elif filter2 == "b":
			search_between(a)
		else:
			wrong_input()
	elif filter == "w":
		word = input("Enter any word you wish: ")
		for i in list(pickle_load(a).values()):
			if i[0].lower().count(word.lower()) or i[1].lower().count(word.lower()):
				print (i)
	elif filter == "e":
		word = input("Enter exact word you wish: ")
		for i in list(pickle_load(a).values()):
			if i[0].lower() == word.lower() or i[1].lower() == word.lower():
				print (i)
	else:
		wrong_input()
	
# Default data for beginning
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

# Operation body
while True:
	
	if not os.path.exists("data.pickle"):
		pickle_dump('data.pickle', data)
		
	act = input_main()
	
	FUNCS = {"l": "act_list('data.pickle')", 
		"d": "act_delete('data.pickle')", 
		"e": "act_edit('data.pickle')", 
		"s": "search_main('data.pickle')", 
		"a": "act_add('data.pickle')" }

	if act in FUNCS.keys():
		exec(FUNCS[act])
	elif act == "q":
		break
	else:
	    wrong_input()