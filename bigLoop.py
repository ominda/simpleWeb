from datetime import datetime, timedelta
from time import time
startTime =  time() #datetime.now()
result = []
for a in range(10000):
    for b in range(10000):
        if (a+b)%11 == 0:
            result.append((a,b))
endTime = time() # datetime.now()

diff = endTime - startTime # timedelta(endTime, startTime)
print(f"Code took {diff} seconds")