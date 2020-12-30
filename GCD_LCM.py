import math

x = int(input("Enter first number  "))
y = int(input("Enter second number  "))
lcm=x
while lcm%x !=0 or lcm%y != 0:
    lcm+=x

print("lcm = ",lcm);
gcd=2;
GCD=1;
while gcd < x and gcd < y:
    if(x%gcd==0 and y%gcd==0):
        GCD=gcd
    gcd+=1

print("gcd = ",GCD)
