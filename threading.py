import threading
satir = 4
sutun = 4

matris= [[1,2,3,4],
         [1,2,3,4]]

def coder(number):
    print(f'Coder ID: {number}')


threads = []
for k in range(4):
    for j in range(4):
        t = threading.Thread(target=coder, args=(k,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
