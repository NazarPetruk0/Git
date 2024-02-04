import random

def get_numbers_ticket(min, max, quantity):
    if not(1 <= min <= max <= 1000) or quantity < 1:
        return []
    unique_nums = set()
    while len(unique_nums) < quantity:
        unique_nums.add(random.randint(min, max))
    return sorted(list(unique_nums))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)