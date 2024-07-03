def Extend_Euclidean(a,b):
    r1 = a
    r2 =b
    s1=t2=1
    s2=t1=0
    print("Q \t r1 \t r2 \t r \t s1 \t s2 \t s \t t1 \t t2 \t t")

    while(r2>0):
        quotient = int(r1/r2)

        remainder = r1%r2
        print(f"{quotient} \t {r1} \t {r2} \t {remainder} ", end=" ")
        r1 = r2
        r2 = remainder

        s = s1 -(quotient*s2)
        print(f"\t {s1} \t {s2} \t {s} ", end=" ")
        s1=s2
        s2=s

        t= t1-(quotient*t2)
        print(f"\t {t1} \t {t2} \t {t} \t ")
        t1=t2
        t2=t
    print(f"GCD = {r1}  s = {s1} and t = {t1} and (s*a)+(t*b)= GCD(a,b)")
    print(f"i.e ({s1}*{a})+({t1}*{b})={(s1*a)+(t1*b)}")


print("Niyati's Code for Extended Euclidean Algorithm")
print("Enter Two numbers whose GCD is to be found")
n1 = int(input("Enter the 1st Number: "))
n2 = int(input("Enter the 2nd Number: "))

if n1>=n2:
    Extend_Euclidean(n1, n2)
else :
    Extend_Euclidean(n2, n1)



