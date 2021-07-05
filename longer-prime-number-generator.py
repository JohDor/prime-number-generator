#ask for primes
p = int(input("How many primes?  "))
#counts for primes
counts = 2
#counts for iterations
nums=2
while(counts<=p+1):
    #count for the numbers
    count = 0
    #i is first prime number
    i=2
    #check for non-primes
    while(i<= nums//2):
        if (nums % i == 0):
            #skip to the next number
            count += 1
            #break out of the loop
            break
            #i will always increase for checking the condition
        i+=1
        #confirm if number is prime
    if (count == 0 and nums != 1 ):
        print(" %d" %nums, end = ' ')
        #only goes up when we meet the condition
        counts += 1
    #will always go up
    nums += 1

print("")
