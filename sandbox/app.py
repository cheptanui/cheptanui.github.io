# Written by Viola Melly

from flask import Flask, request
import Credit_score
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/formula', methods=['GET','POST'])
def fico_additive_formula():
    number_of_recharge = request.form["number_of_recharge"]
    age_of_sim = request.form["age_of_sim"]
    balance_before_recharge = request.form["balance_before_recharge"]
    user_information = {"number_of_recharge" : number_of_recharge, 
    "age_of_sim": age_of_sim,
    "balance_before_recharge" : balance_before_recharge }
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
	[[21],30]]}

    return Credit_score.credit_score(user_information, score_card)