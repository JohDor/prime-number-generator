#check if number is a prime
def isPrime(n):
    prime = True
    for i in range(2, n):
        if (n%i==0):
            prime=False
            break
        else:
            prime=True
    return prime
h=isPrime(int(input("Enter a number:  ")))
print(h)
