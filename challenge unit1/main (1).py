def fact_rec(n):
    if n == 0 or n==1:
      return 1
    else:
      return n*fact_rec(n-1)

n = 5
result = fact_rec(n)
print('the factorial of',n,'is',result)
