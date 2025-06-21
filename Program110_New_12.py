# 12: Calculate income tax
# 	Calculate income tax for the given income by adhering to the rules below
# 	Taxable Income	Rate (in %)
# 	First $10,000	0
# 	Next $10,000	10
# 	The remaining	20
# 	For example, suppose the income is 45000, and the income tax payable is
#
# 	10000*0% + 10000*10%  + 25000*20% = $6000

sal = int(input("Please enter the salary: "))
total_tax_payable = 0
print(f"Total Income: {sal}")
if sal <= 10000:
    total_tax_payable = 0
elif sal <= 20000:
    x = sal - 10000
    total_tax_payable = x * 10 /100
else:
    total_tax_payable = 10000 * 10 / 100
    total_tax_payable += (sal-20000) * 20 /100

print(f"Total Payable Tax is : {total_tax_payable}")
