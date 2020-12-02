def my_div(n):
       largest = None
       for i in range(2, n):
           while n % i == 0:
               largest = i
               n //= i
           if n == 1:
               return largest
       if n > 1:
           return n

print ('Введите число n>>')
n = int(input())
print ('>>', my_div(n))