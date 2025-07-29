try:
 Num = int(input("enter number"))
if num > 100:
    raise("Number is greater than 100")
else:
    print("ok...")
except Exception as e:
    print(e)
    
