# name of student: Aisha Wijngaarden
# number of student: 99073560
# purpose of program: To give you exact change depending on how much
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #This code takes an input from the user in the form of a floating-point number and converts it to an integer representing the number of cents. 
paid = int(float(input('Paid amount: ')) * 100) #This code takes an input from the user in the form of a floating-point number and converts it to an integer representing the number of cents.
change = paid - toPay #paid will subtract the topay and then the answer will equal to the change amount

if change > 0: #If the change is less than 0 then it won't be able to go further with the program
  coinValue = 50 #The varible is called coinValue and 50 is then set inside that one variable
  
  while change > 0 and coinValue > 0: #For example, the change is 362 and the coinvalue is 50.
    nrCoins = change // coinValue #// mean seeing how many times the coinvalue can fit inside the change amount. For example, you can use 50cents and see how many 50 cents fits inside the number.

    if nrCoins > 0: #Its the same as above. You are seeing how many times you can fit a specific number inside the change and then you give back whats left over. You can keep going lower and lower with the numbers until you reach 0.
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #In this line of code you returning what is left over from the change and you will continue to repeat the same thing over and over until you reach 0 or a lesser number.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) ##In this line of code you returning what is left over from the change and you will continue to repeat the same thing over and over until you reach 0 or a lesser number.
      change -= nrCoinsReturned * coinValue #

# comment on code below: This code checks if the value of the variable "change" is greater than 0. If it is, it will print a message that says "Change not returned" followed by the value of change and the word "cents". If the value of change is less than or equal to 0, it will print the message "done".
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #This code checks if the value of the variable "nrCoins" is greater than 0. If it is, it will print a message that says "return maximal" followed by the value of nrCoins, the word "coins" and the value of coinValue, "cents". 
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')