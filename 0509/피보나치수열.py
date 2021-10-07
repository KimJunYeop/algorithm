n = 10

save_list = [0] * 101

def fibo(n) :
    if n == 1 or n == 2:
        return 1
    if save_list[n] != 0:
        return save_list[n]
    save_list[n] = fibo(n-1) + fibo(n-2)
    return save_list[n]

print(fibo(100))