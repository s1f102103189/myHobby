def find_addition_to_get_remainder(value, divisor, remainder_target):
    addition = 0
    while (value + addition) % divisor != remainder_target:
        addition += 1
    return addition

value = 428750
divisor = 256
remainder_target = 42
addition_required = find_addition_to_get_remainder(value, divisor, remainder_target)

print(f"Number to add to {value} to get a remainder of {remainder_target} when divided by {divisor} is: {addition_required}")

print(428842%256)