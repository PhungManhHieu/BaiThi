
def isThuanNghich(n):
    str1 = str(n);     
    str2 = str1[::-1]; 
    if (str1 == str2):
        return True;
    else:
        return False;
 
n = (input("Nhập họ = "));
m = (input("Nhập tên đệm = "));
k = (input("Nhập tên = "));
print("Tổng các chữ số của", len(n), len(m), len(k) , "là", isThuanNghich(n));
