a,b = '512','48'
def add(a,b):
   result = ''
 #YOUR CODE GOES HERE

   if(len(a) < len(b)):
    a = a.zfill(len(b))
   else:
    b = b.zfill(len(a))

    n = len(a)
    carry = 0

   for i in range(n -1, -1, -1):
     temp = int(a[i]) + int(b[i]) + carry

     result = str(temp % 10) + result
     carry = temp // 10

   return result
sum = add(a,b)
print(a,'+',b,'=', sum)
