num = int(input("enter a number"))
rev=0
while(num>0):
    rem = num%10;
    rev = (rev*10)+ rem
    num = num//10
print("\n reverse of a number is: %d" %rev)


''' Number = int(input("Enter any Number: "))
Reverse = str(Number)[::-1]
print("\n Reverse of entered number is = %s" %(Reverse)) '''


