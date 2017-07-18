#function growth
import math
open("function_growth", r)


MIN_N = 2
MAX_N = 2048

i = MIN_N

function_growth.write('log N \tN \tN log N\tN^2 \tN^3')


while i <= MAX_N:
    print(int(math.log(i)))
    print('\t')
    print(i)
    print('\t')
    print(int(i * math.log(i)))
    
    print(i * i)
    
    print(i * i * i)
    print()
    i *= 2
	
# python functiongrowth.py 
# log N   N       N log N N^2 	  N^3
# 0       2       1       4       8
# 1       4       5       16      64
# 2       8       16      64      512
# 2       16      44      256     4096
# 3       32      110     1024    32768
# 4       64      266     4096    262144
# 4       128     621     16384   2097152
# 5       256     1419    65536   16777216
# 6       512     3194    262144  134217728
# 6       1024    7097    1048576 1073741824
# 7       2048    15615   4194304 8589934592	