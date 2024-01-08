def is_prime(number):
    for divider in range(2,int(math.sqrt(number))+1):
        if number % divider == 0:
            return False
        return True
    
test=is_prime(10223)
print(test)
