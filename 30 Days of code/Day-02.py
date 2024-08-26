#Task - Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, 
# Find and print the meal's total cost. Round the result to the nearest integer.

def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost/100)*tip_percent
    tax = (tax_percent/100)*meal_cost
    print(round(meal_cost+tip+tax))

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
