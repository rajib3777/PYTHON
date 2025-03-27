def islucky(n):
    while n > 0:
        digit = n % 10
        if digit != 4 and digit != 7:
            return False
        n //= 10
    return True



A ,B = input().split()
A = int(A)
B = int(B)

found = False

for i in range(A,B + 1):
    if islucky(i):
      print(i,end = " ")
      found = True

if not found:
    print(-1)

    