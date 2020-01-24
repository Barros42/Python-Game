from time import sleep

N=12

for i in range(N):
   sleep(0.5)
   print(f"{i/N*100:.1f} %", end="\n")