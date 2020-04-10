# Written by Viola Melly
# A credit scoring algorithm using FICO's Generalized  additive formula
#



def credit_score(user_information, score_card):
	#get the number of recharges, age of sim and balance before recharge 
	#from the user information given
	number_of_recharge = user_information["number_of_recharge"] # json object from SP
	age_of_sim = user_information["age_of_sim"]
	balance_before_recharge = user_information["balance_before_recharge"]

	len_of_char = len(score_card.keys()) #Gets the length of the characteristics from our score card
	total_score = 0

	values = [number_of_recharge ,age_of_sim,balance_before_recharge] #values from SP
	keys = score_card.keys()


	for i in range(len_of_char):
		total_score += characteristic_score(keys[i],values[i], score_card)
	print(total_score)

	return total_score


	

def characteristic_score(characteristic,value,score_card):
	char_list = score_card[characteristic]
	score_weight = 0

	for i in range (len(char_list)):
		list_bin = char_list[i]
		bin_range = list_bin[0]
		bin_score = list_bin[1]

		if value >= min(bin_range) or value <= max(bin_range):
			score_weight = bin_score
			break

	return score_weight


if __name__ == '__main__':
	score_card = {
	"1":[[[0],0],
	[[1,7],5],
	[[8,14],10],
	[[15,21],20],
	[[22,30],30],
	[[31],40]],

	"2":[[[1],5],
	[[1,2],10],
	[[3,4],15],
	[[5,6],20],
	[[6],30]],

	"3":[[[0],5],
	[[1,5],10],
	[[6,10],15],
	[[11,15],20],
	[[16,20],25],
	[[21],30]]

	}

	user_information = {

	"number_of_recharge" : 7, "age_of_sim": 2,"balance_before_recharge" : 0
	}
  
	credit_score( user_information, score_card )









