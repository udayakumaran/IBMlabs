num = int(input("Enter a number: "))
for j in range(1,num+1):
    if j > 1:
        for i in range(2, j):
            if (j % i) == 0:
                print(j, "is not a prime number")
                #print(i, "times", j // i, "is", j)
                break
        else:
            print(j, "is a prime number")


    else:
        print(j, "is not a prime number")
