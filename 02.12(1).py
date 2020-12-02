def min4(a,b,c,d):
  min1 = min(a,b)
  min2 = min(c,d)
  m = min(min1, min2)
  return m

print ('Введите число a>>')
a = int(input())
print ('Введите число b>>')
b = int(input())
print ('Введите число c>>')
c = int(input())
print ('Введите число d>>')
d = int(input())
print ('Минимальное число>>', min4(a,b,c,d))