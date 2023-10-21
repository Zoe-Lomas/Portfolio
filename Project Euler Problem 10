def sqrt(a):
    x = a/2
    y = 0
    while abs(x-y)>0.4:
        y=x
        x=0.5*(y+a/y)
    return(int(x))
def isPrime(num):
    for i in range(2,int(sqrt(num))+1):
        if (num % i == 0):
            return False
    return True
 
sum = 0
 
for i in range(2,2000000):
    if isPrime(i):
        sum += i

print('The sum of all primes below 2 million is: ' + str(sum))
