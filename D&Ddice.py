import random  #allowsforrandomgenerator
restart = 1  #enterintoloop

print "------------------------------------------------------------------------------"
print "_________________________to end program enter 'off'___________________________"

tracker = 0

while restart == 1:  #allowsforlooprestart
	dice_type = raw_input("What type of dice do you want to roll?:")  #userinput

	while True:  #generatesloop
		if dice_type == "d6" or dice_type == "6":  #readsuserinput
			min = 1  #dicemin
			max = 6  #dicemax
			tracker += 1
			print ".............................."
			print "dice roll # %s" % (tracker)
			print "Fate rolls the dice..."
			print "and the value is...."
			x = random.randint(min, max) #randomgenerator
		        if x == 1 or x == 2:
		            print x
		            print "well derp...."
		            restart = 1
		            break
		        elif x == 3 or x == 4:
		            print x
		            print "not too bad...."
		            restart = 1
		            break
		        elif x == 5 or x == 6:
		            print x
		            print "nice roll...."
		            restart = 1
		            break
    		
		elif dice_type == "d4" or dice_type == "4":
			min = 1
			max = 4
			tracker += 1
			print tracker
			print ".............................."
			print "dice roll # %s" % (tracker)
			print "Fate rolls the dice..."
			print "and the value is...."
			x = random.randint(min, max)
		        if x == 1:
		            print x
		            print "well it's d4 what did you expect...."
		            restart = 1
		            break
		        elif x == 2 or x == 3:
		            print x
		            print "not too bad...."
		            restart = 1
		            break
		        elif x == 4:
		            print x
		            print "nice roll...."
		            restart = 1
		            break
    	
		elif dice_type == "d8" or dice_type == "8":
			min = 1
			max = 8
			tracker += 1
			print tracker
			print ".............................."
			print "dice roll # %s" % (tracker)
			print "Fate rolls the dice..."
			print "and the value is...."
			x = random.randint(min, max)
		        if x == 1 or x == 2 or x == 3:
		            print x
		            print "well derp...."
		            restart = 1
		            break
		        elif x == 4 or x == 5:
		            print x
		            print "not too bad...."
		            restart = 1
		            break
		        elif x == 6 or x == 7 or x == 8:
		            print x
		            print "nice roll...."
		            restart = 1
		            break
    				
		elif dice_type == "d10" or dice_type == "10":
			min = 1
			max = 10
			tracker += 1
			print tracker
			print ".............................."
			print "dice roll # %s" % (tracker)
			print "Fate rolls the dice..."
			print "and the value is...."
			x = random.randint(min, max)
		        if x == 1 or x == 2 or x == 3:
		            print x
		            print "well derp...."
		            restart = 1
		            break
		        elif x == 4 or x == 5 or x == 6:
		            print x
		            print "not too bad...."
		            restart = 1
		            break
		        elif x == 7 or x == 8 or x == 9:
		            print x
		            print "nice roll...."
		            restart = 1
		            break
		        elif x == 10:
		            print x
		            print "killin' it...."
		            restart = 1
		            break
    		
		elif dice_type == "d12" or dice_type == "12":
			min = 1
			max = 12
			tracker += 1
			print tracker
			print ".............................."
			print "dice roll # %s" % (tracker)
			print "Fate rolls the dice..."
			print "and the value is...."
			x = random.randint(min, max)
		        if x == 1 or x == 2 or x == 3:
		            print x
		            print "well derp...."
		            restart = 1
		            break
		        elif x == 4 or x == 5 or x == 6:
		            print x
		            print "not great...."
		            restart = 1
		            break
		        elif x == 7 or x == 8 or x == 9:
		            print x
		            print "nice roll...."
		            restart = 1
		            break
    			elif x == 10 or x == 11 or x == 12:
    			    print x
    			    print "dang...."
    			    restart = 1
    			    break
    			
		elif dice_type == "d20" or dice_type == "20":
			min = 1
			max = 20
			tracker += 1
			print tracker
			print ".............................."
			print "dice roll # %s" % (tracker)
			print "Fate rolls the dice..."
			print "and the value is...."
			x = random.randint(min, max)
		        if x == 1:
		            print x
		            print "natural fail...."
		            restart = 1
		            break
		        elif x == 2 or x == 3 or x == 4 or x == 5:
		            print x
		            print "at least you didn't roll a 1...."
		            restart = 1
		            break
		        elif x == 6 or x == 7 or x == 8 or x == 9:
		            print x
		            print "meh...."
		            restart = 1
		            break
		        elif x == 10 or x == 11 or x == 12 or x == 13:
		            print x
		            print "not too shabby...."
		            restart = 1
		            break
		        elif x == 14 or x == 15 or x == 16 or x == 17:
		            print x
		            print "sweet roll dude...."
		            restart = 1
		            break
		        elif x == 18 or x == 19:
		            print x
		            print "ooo kill 'em...."
		            restart = 1
		            break
		        elif x == 20:
		            print x
		            print "natural crit...."
		            restart = 1
		            break
			
		elif dice_type == "off":
		    restart = 0
		
		else:  #unrelateduserinput
			print "...."
			print "we don't use that kind of dice in d&d"
			print "...."
			restart = 1
			break