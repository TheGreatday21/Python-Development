def calculate_finances(monthly_income :float, tax_rate : float, currency :str) -> None :
#the none tells the code that this will result to nothing .. Its just to execute the code
#type annotations arent really necessary but they are good practice
    yearly_salary :float = monthly_income*12
    monthly_tax : float =monthly_income * (tax_rate /100)
    yearly_tax :float =monthly_tax*12
    monthly_net_income : float = monthly_income - monthly_tax
    yearly_net_income : float = yearly_salary - yearly_tax

    print("-------------------------")
    print(f"Monthly income : {currency}{monthly_income :,.2f}")
#in f strings to format to 2dp we use the .2f 
#in f strings to format commas you first put the annotaion ":" then add a comma
calculate_finances(100, 20 ,"$")
















