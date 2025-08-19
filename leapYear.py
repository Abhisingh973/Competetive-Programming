A = int(input("Enter an integer: "))
if A % 400 == 0 and A% 4==0 and A%100!=0 :
    print("Leap year")
else:
    print("no leap year")