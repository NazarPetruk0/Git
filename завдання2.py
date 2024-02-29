import random

def get_numbers_ticket(min, max, quantity):
    if not(1 <= min <= max <= 1000) or quantity < 1 or quantity > (max - min + 1):
        return []
    unique_nums = set()
    while len(unique_nums) < quantity:
        unique_nums.add(random.randint(min, max))
    return sorted(unique_nums)  

lottery_numbers = get_numbers_ticket(10, 14, 5)
print("Ваші лотерейні числа:", lottery_numbers)
