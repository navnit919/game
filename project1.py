import random
while 1 :
	Name = input("hey type your name:")
	print("hellow",Name,"welcome to my game")
	should_we_play = input("do you want to play ?: ")
	#play = should_we_play = "yes"
	#we can combine above statement to the if statement
	if should_we_play == "yes".lower():
		print("we are going to play")
	else:
		print("we are not going to play")
	direction = input("do you want to go right or left ?(right/left):").lower()
	direction_int =0
	if direction=='left':
			direction_int = 1;
	else:
			direction_int =2;
	direction_die = random.randint(1,2)        
	if direction_int == direction_die:
			print("you went left  and fell of a clif,game over,try again ,best wishes")
	elif direction != direction_die :
			print("okay we went right")
			bridge_int =0
			choice = input("okay,you will see a bridge yo want to swim under it or crossit ?(swim/cross)").lower()
			if choice == "swim":
					bridge_int =1
			elif choice == "crossit":
				brigde_int =2;
			else:
					print("wrong option selected !! you lost ")       
			bridge_die = random.randint(1,2)
			if(bridge_int==bridge_die):
					print("you fell and aligator eaten you  !! you lost")
			else:
					print("you found the gold !! you won")
							
	else:
			print("sorry not valid replay ,you die,good luck try next time")
			
	exit_choice = input("do you want exit ? yes or no:")
	if exit_choice=="yes":
		break
	else:
		continue
     
			
				

