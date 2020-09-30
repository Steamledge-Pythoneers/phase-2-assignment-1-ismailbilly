## TODO: complete the function "lowest_terms" below

def lowest_terms(num, denom):
	greatest_common_denom = 0
    if denom == 0:
        print("Division by zero")
    return denom
    
    for i in range(min(abs(num), abs(denom)), 1, -1):
            if num % i == 0 and denom % i == 0:
                greatest_common_denom = i
                break
    return (num // greatest_common_denom,  denom // greatest_common_denom)
	
