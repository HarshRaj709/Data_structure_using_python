# def natural(n):
#     if n>0:
#         natural(n-1)
#         print(n,end = ' ')

# natural(10)


# def printN(n):
#     if n>0:
#         print(n,end=' ')
#         printN(n-1)

# printN(10)

# def odd(n):         #10
#     if n>0:
#         odd(n-1)
#         print(2*n-1,end=' ')
# odd(10)


# def evenr(n):
#     if n>0:
#         evenr(n-1)
#         print(2*n,end = ' ')

# evenr(10)


# def oddr(n):         #10
#     if n>0:
#         print(2*n-1,end=' ')
#         oddr(n-1)
# oddr(10)

# def sum(n):
#     if n==0:
#         return 0
#     r = n + sum(n-1)
#     return r
# print(sum(10))

# def sumodd(n):
#     if n==1:
#         return 1
#     r = 2*n-1 + sumodd(n-1)
#     return r

# print(sumodd(10))

# def sumeven(n):
#     if n==1:
#         return 2
#     r = 2*n + sumeven(n-1)
#     return r

# print(sumeven(10))

# def fact(n):
#     if n==0:
#         return 1
#     r = n * fact(n-1)
#     return r
# print(fact(5))

#sum of square of 1st n natural number
# def sumsquare(n):
#     if n == 1:
#         return 1
#     r = sumsquare(n-1) + n*n
#     return r
# print(sumsquare(5))