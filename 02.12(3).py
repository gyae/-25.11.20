def my_sum(a,b):
  a+=1
  b-=1
  if b>0:
    return my_sum(a,b)
  else:
    return a

print ('Введите число a>>')
a = int(input())
print ('Введите число b>>')
b = int(input())
print ('Сумма>>', my_sum(a,b))