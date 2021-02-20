def primeFirst(value):
    print ("-----",value)

def primeSecond(value):
    print (value,"-----")
    
for i in range(1000):
    if i <= 500:
        primeFirst(i)
    else:
        primeSecond(i)