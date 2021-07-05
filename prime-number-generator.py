#find how many primes in a given range
max=int(input("What's the last number?  "))
min=int(input("What's the starting number? "))
if (min>max):
    print("Not valid.")
else:
    for num in range (min, max+1):
        if(num>1):
            for i in range(2, num):
                if(num%i) == 0:
                    break
            else:
                print(" %d" %num, end = ' ')
