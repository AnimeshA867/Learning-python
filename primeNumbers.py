def fact(n):
    if(n==0 or n==1):
        return 1;
    else:
        return n*fact(n-1);

# num= int(input("Enter a number to find the factorial of:"))



def prime(n):
    if n==1 or n==2 or n==0:
        return True;
    for x in range (2,int(n/2)+1):
        if(n%x==0):
            return False;
    return True;

primeNumbers=[];

for x in range (100):
    if(prime(x)):
        primeNumbers.append(x);
    else:
        continue;

print(primeNumbers);
