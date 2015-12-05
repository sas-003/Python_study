# coding: utf-8
import pickle, os, sys, time
from db import act_list, act_add, act_delete, act_edit, search_main, pickle_dump, pickle_load
from debug import wrong_input, input_main

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
		try:
			exec(FUNCS[act])
		except:
			print("\n Lots of errors are still not processed \n Interrupts can injure db consistancy! Careful!")
			sys.exit(0)
		else:
			print("Congratiulations on no errors! :-)")
		finally:
			print(time.asctime())
	elif act == "q":
		break
	else:
	    wrong_input()