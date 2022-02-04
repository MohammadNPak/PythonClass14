
# i=0
# y=[0,0,0]
# while i<3:
#     y[i]=int(input())
#     i+=1

# if (y[1]**2)==(y[0]**2)+(y[2]**2):
#     print("YES")
# elif (y[0]**2)==(y[1]**2)+(y[2]**2):
#     print("YES")
# elif (y[2]**2)==(y[1]**2)+(y[0]**2):
#     print("YES")
# else:
#     print("NO")

# x,y,z = int(input()),int(input()),int(input())
# if x**2 == y**2+z**2 or y**2 ==x**2 +z**2 or  z**2 ==x**2 + y**2:
#     print("YES")
# else:
#     print("NO")






# x=input()
# print(f"saal:{x[0:2]}")
# print(f"maah:{x[2:]}")




# x=input()
# i=0
# is_symmetric = True
# while i < len(x):
#     if x[i]!=x[-i-1]:
#         is_symmetric = False
#     i+=1

# if is_symmetric:
#     print("YES")
# else:
#     print("NO")



# x=input()
# if x == x[::-1]:
#     print("YES")
# else:
#     print("NO")







# Compute power of two greater than or equal to `n`
# n = int (input())
# j = 1
# while j<n:
#     j*=2
# print(j)





# n = int(input())

# i=0
# max_input = 0
# while i < n:
#     x = int(input())
#     if x > max_input:
#         x=max_input
#     i+=1

# print(max_input)


# n = int(input())
# numbers = input().split()

# i = 0
# max_ = int(numbers[0])
# while i< len(numbers):
#     if int(numbers[i])> max_:
#         max_ = int(numbers[i])
#     i+=1
# print(max_)




# a = int(input())#عداد کامل بودن یا نبودن
# b = 1
# c = 0
# while b < a:
#     if a % b == 0:
#         c += b
#     b += 1

# if c == a:
#     print("YES")
# else:
#     print("NO")


# num = int(input())
# sum = 0
# for i in range(1, num):
#     if (num % i == 0):
#       sum += i
# if (sum == num):
#     print("YES")
# else:
#     print("NO")


x=input()
c=0
while c < len(x):
    print(f"{x[c]}:", x[c]*int(x[c]))
    c +=1

