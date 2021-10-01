def fiboSum(n):
     #logic her
     if N == 0:

        return 0
 

     

     Sum = 0

     a, b = 0, 1

     Sum += a 
     count += 1

     while count <= N: 
 

        Sum += a

        a, b = b, a + b 

     

     return Sum

Nterms= int(input())
out_ = fiboSum(Nterms)
print(out_)
