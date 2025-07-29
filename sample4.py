try:
    Num = int(input("enter number"))        
if n > 0:
    print("The number is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
except Exception as e:
    print(e)
    