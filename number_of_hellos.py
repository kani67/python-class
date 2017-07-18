n = int(input("Number of hellos "))
i=1

while i <= n:
    r10 = i % 10
    

    
    if r10 == 1:
        print(str(i) + "st" + " hello")
    elif r10 == 2:
        print(str(i) + "nd" + " hello")
    elif r10 == 3:
        print(str(i) + "rd" + " hello")
    elif r10 >= 4 or r10 == 0:
        print(str(i) + "th" + " hello")

    i +=1
		
