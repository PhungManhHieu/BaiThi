TenDem = input("Nhập Tên Đệm của bạn: ")
n = int(input("Nhập số nguyên dương n = "));

def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;

print("Tên đệm của b là")
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));