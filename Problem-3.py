def conditional_odd_series(a: int):
    if a % 2 == 0:
        a -= 1
    return [2 * i + 1 for i in range(a)]

n = int(input())
print(conditional_odd_series(n))  
