#function growth
import math

MIN_N = 2
MAX_N = 1048

i = MIN_N

print('log N\t','N\t','N \t','log N\t','N^2\t','N^')

while i <= MAX_N:

     a = int(math.log(i))
     b = int(i * (math.log(i)))
     c = int((i * i))
     d = int((i * i * i))
     
     
     print(a,'\t',b,'\t',c,'\t',d,'\t')

     i *= 2

