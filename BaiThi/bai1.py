Ten = input("Nhập tên của bạn: ")
print (len(Ten))
n = len(Ten)
 
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
print (d)