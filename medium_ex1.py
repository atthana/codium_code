print("Medium ex.1")
print("=" * 50)
lower = 1  
upper = int(input("Enter your upper of prime number to find: "))  

number = []  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           # print("num is", num)
           number.append(num)
print(upper, " -> ", *number)
