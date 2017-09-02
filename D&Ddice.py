import random  #allowsforrandomgenerator
import time    #makesitfeelgood


def dice(d_num, rolls=1):
	min = 1  #dicemin
	max = d_num  #dicemax
	total = 0
	if rolls == "1":
		print "rolling "+str(d_num)
		print "1 time"
	else:
		print "rolling "+str(d_num)
		print str(rolls)+" times"
	for x in range(rolls):
		result = random.randint(min, max) #randomgenerator
		total += result
	restart = 1
	return total


def stats(d_num, rolls, local, my_rolls, my_total, my_avg):
	my_rolls['rolls_'+str(d_num)] += rolls
	my_total['total_'+str(d_num)] += local
	avg = my_total['total_'+str(d_num)]/my_rolls['rolls_'+str(d_num)]
	my_avg['avg_'+str(d_num)] = avg
	nap_time = 0.5 + (0.5-(0.5/rolls))
	time.sleep(nap_time)
	return avg
		

def main():
	restart = 1  #enterintoloop
	tracker = 0 #startstrackerat0
	my_rolls = {'rolls_4':0, 'rolls_6':0, 'rolls_8':0, 'rolls_10':0, 'rolls_12':0, 'rolls_20':0, 'rolls_100':0}
	my_total = {'total_4':0, 'total_6':0, 'total_8':0, 'total_10':0, 'total_12':0, 'total_20':0, 'total_100':0}
	my_avg = {'avg_4':0, 'avg_6':0, 'avg_8':0, 'avg_10':0, 'avg_12':0, 'avg_20':0, 'avg_100':0}
	print "\n------------------------------------------------------------------------------"
	print "_________________________to end program enter 'off'___________________________"
	print "______________________ to see dice stats enter 'stats'________________________"
	while restart == 1:  #allowsforlooprestart
		dice_type = raw_input("What type of dice do you want to roll?: ")  #userinput
		rolls = int(raw_input("How many times do you want to roll?: ") or 1)
		while True:  #generatesloop
			if dice_type == "d4" or dice_type == "4":  #readsuserinput
				local_4 = dice(4, rolls)
				avg_4 = stats(4, rolls, local_4, my_rolls, my_total, my_avg)
				print "total ==> " + str(local_4)
				print "avg ------> " + str(avg_4)
				break
			elif dice_type == "d6" or dice_type == "6":  #readsuserinput
				local_6 = dice(6, rolls)
				avg_6 = stats(6, rolls, local_6, my_rolls, my_total, my_avg)
				print "total ==> " + str(local_6)
				print "avg ------> " + str(avg_6)
				break
			elif dice_type == "d8" or dice_type == "8":  #readsuserinput
				local_8 = dice(8, rolls)
				avg_8 = stats(8, rolls, local_8, my_rolls, my_total, my_avg)
				print "total ==> " + str(local_8)
				print "avg ------> " + str(avg_8)
				break
			elif dice_type == "d10" or dice_type == "10":  #readsuserinput
				local_10 = dice(10, rolls)
				avg_10 = stats(10, rolls, local_10, my_rolls, my_total, my_avg)
				print "total ==> " + str(local_10)
				print "avg ------> " + str(avg_10)
				break
			elif dice_type == "d12" or dice_type == "12":  #readsuserinput
				local_12 = dice(12, rolls)
				avg_12 = stats(12, rolls, local_12, my_rolls, my_total, my_avg)
				print "total ==> " + str(local_12)
				print "avg ------> " + str(avg_12)
				break
			elif dice_type == "d20" or dice_type == "20":  #readsuserinput
				local_20 = dice(20, rolls)
				avg_20 = stats(20, rolls, local_20, my_rolls, my_total, my_avg)
				print "total ==> " + str(local_20)
				print "avg ------> " + str(avg_20)
				break
			elif dice_type == "d100" or dice_type == "100":  #readsuserinput
				local_100 = dice(100, rolls)
				avg_100 = stats(100, rolls, local_100, my_rolls, my_total, my_avg)
				print "total ==> " + str(local_100)
				print "avg ------> " + str(avg_100)
				break
			elif dice_type == "off":
				restart = 0
				break
			elif dice_type == "stats":
				print my_rolls
				print "-"*5
				print my_total
				print "-"*5
				print my_avg
				restart = 1
				break
			else:
				print "\nXx-----------------------------------------xX"
				print "    We don't use that kind of dice in d&d"
				print "Xx-----------------------------------------xX\n"
				restart = 1
				break

if __name__ == '__main__':
    import plac
    plac.call(main)
