# a= "hello"
# for x in a:
#     print(x)
# for a in "kullu":
#      print(a)
# for a in range(0,10):
#      print(a)
     
# a=1
# while a<10:
#      print(a*2)
#      a = a+1


# for a in range (10):
#      if a==7:
#           break
#      print(a)
# for a in range(10):
#      if a==6:
#           continue
#      print(a)


# number =int(input("enter a number"))
# i=0
# while i <=10:
#      print(f"{number}+{i} ={number +i}")
#      i =i+1

# sum=0
# for a in range(11):
#      sum = sum +a
#      print(sum)
     
# sum=0
# for a in range(20):
#       if a % 2== 0:
#            sum= sum +a
# print(sum)
 
for num in range(2, 30):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
                print(num)    
     
     