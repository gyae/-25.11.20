def my_power(a,n):
  if n==0:
    return 1
  else:
    return a*my_power(a, n-1)

print ('Введите число a>>')
a = int(input())
print ('Введите число n>>')
n = int(input())
print ('>>', my_power(a,n))