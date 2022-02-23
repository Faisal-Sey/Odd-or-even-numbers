

def odd_or_even(n) -> bool:
    if n % 2 == 0:
        return "Even number"
    else:
        return "Odd number"


number = int(input("Enter number: "))
print(odd_or_even(number))