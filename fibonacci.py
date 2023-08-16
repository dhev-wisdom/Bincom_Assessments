"""
Fibonacci series
"""

fibo = int(input("What's the length of the fibo series you want to create? "))

def fibonaci(fibo):
    """
    Fibonacci function
    """
    fibo_list = []
    for i in range(fibo):
        if i == 0:
            fibo_list.append(0)
            continue
        elif i == 1:
            fibo_list.append(1)
            continue
        else:
            current_value = fibo_list[-1] + fibo_list[-2]
            fibo_list.append(current_value)
    return fibo_list

if __name__ == '__main__':
    print(fibonaci(fibo))
