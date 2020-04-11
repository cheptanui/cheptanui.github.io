# Written by Viola Melly
# A credit scoring algorithm using FICO's Generalized  additive formula

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

	# for i in range(len_of_char):
	# 	total_score += characteristic_score(keys[i],values[i], score_card)
	# print(total_score)

	return str(total_score)

# def characteristic_score(characteristic,value,score_card):
# 	char_list = score_card[characteristic]
# 	score_weight = 0

# 	for i in range (len(char_list)):
# 		list_bin = char_list[i]
# 		bin_range = list_bin[0]
# 		bin_score = list_bin[1]

# 		if value >= min(bin_range) or value <= max(bin_range):
# 			score_weight = bin_score
# 			break
 
# 	return score_weight








