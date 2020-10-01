## TODO: complete the function "lowest_terms" below
#x = str(input('pls input the fraction: '))
def lowest_terms(x):
	# Testing denominator value equals zero
    try:
        return float(x)
    except ValueError:
        n, d = x.split('/')
        try:
            leading, n = n.split(' ')
           
        except ValueError: 
            greatest_common_denom = 0
    num = int(n)
    denom = int(d)
    if denom == 0:
        return "Undefined"
    elif num  == 0:
        return "0"
    
    # calculate the greatest common denominator
    for i in range(min(abs(num), abs(denom)), 1, -1):
            if num % i == 0 and denom % i == 0:
                greatest_common_denom = i
                break
	# divide the fraction
    nums = num // greatest_common_denom
    denoms = denom // greatest_common_denom
    
    return (f"{abs(nums)}/{abs(denoms)}" if nums < 0 and denoms < 0 else f"{nums}/{denoms}")
    
