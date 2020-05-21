import time

#pow((rate+(1-rate)/2),8)

scale = 50
print("执行开始".center(scale//2, '-'))
start = time.perf_counter()
for i in range(scale + 1):
    rate = i/scale
    fastPower = pow((rate+(1-rate)/2),8)
    a = "*" * int(scale*fastPower)
    b = '.' * int(scale * (1-fastPower))
    c = fastPower*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s" .\
          format(c,a,b,dur),end='')
    time.sleep(0.2)
print("\n"+"执行结束".center(scale//2,'-'))