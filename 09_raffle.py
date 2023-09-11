import random

raffle = [1, 2, 3, 4, 5]


winner = random.choice(raffle)
if winner == 3:
    print("Congratulations you have won a $5 mitre ten voucher!!!! ")
else:
    print("Unfortunately you did not win the voucher prize (20% chance)")
