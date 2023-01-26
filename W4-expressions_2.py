sales = float(input('How much was the sale for: '))
commission = float(input('How much comission did you earn (%): '))
sale_rounded = round(sales, 2)
print(f'The sale was for ${sales:,.2} or {sales_rounded}')
comission_earned = sales * commsion / 100