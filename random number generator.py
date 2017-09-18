

print("--------------Random number generator---------")

##########    taking inputs   #################

a=int(input("Enter starting bnumber: "))
b=int(input("Enter ending number: "))
c=int(input("Enter number of times you want to generate:"))
i=0
num=a

######### initialize a counter i from 0 to 73% of c  ###########
c_new=int((c*73)/100)
print("----------Number more than 50% of maximum range---")
print()

######### printing number greater than half of upper limit ########
while i<c_new:
    num=3.14*(a*(num+a-i)+a)%b
    if num>=b//2 and num<=b:
        input("Click to generate new...")
        print (int(num))
        i+=1

######### printing number less than half of upper limit ########

        
num=a
print()
print("----------Number less than 50% of minimum range---")
print()
i=1
while i<=(c-c_new):
    num=3.14*(a*(num+a-i)+a)%b
    if num<=b//2:
        input("Click to generate new...")
        print (int(num))
        i+=1

print()
print("---------------------Thanks----------------------")
input()

############# END ####################
