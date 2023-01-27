num = int(input("enter your number-:")) 
sum =0
order = len(str(num))
temp = num
while temp>0:
    digit = temp%10
    sum +=digit**order
    temp//=10
if num == sum:
      print(num, "is an armstrong number")
else:
       print(num, "is not an armstrong number")   

