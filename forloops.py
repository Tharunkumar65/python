
# for i in range(10):
#       print(i)
#  for i in range(20,31,+2):
#  print(i)
# for i in "Tharun kumar":
#     print(i)
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(2)
# print("Hello")
# for num in range(1,101):
#     if num>1:
#         for i in range(2,num):
#             if(num % i) == 0:
#                break
#         else:
#                 print(num)

num = "105"
reverse = ""
for i in range(len(num),0,-1):
      reverse+=num[i-1]
print("the reverse number is ",reverse)