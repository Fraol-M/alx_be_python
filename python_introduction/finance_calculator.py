# monthly_income = int(input("Enter your monthly income: "))
# monthly_expenses = int(input("Enter your total monthly expenses: "))
# monthly_savings = monthly_income - monthly_expenses
# projected_savings = monthly_savings * 12 + (monthly_savings*12*0.05)
# print(f"Your monthly savings are ${monthly_savings}.")
# print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

    h = Counter(nums)
    n = len(nums)
    for i, j in h.items():
        if j > n/2:
        return i
