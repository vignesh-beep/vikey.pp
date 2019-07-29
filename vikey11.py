def get_all_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors
 
number = int(input())
 
for i in range(1,number+1):
    list_of_factors = get_all_factors(i)
    print(i)

