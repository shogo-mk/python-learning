# if文
x = 10

if x > 5:
    print("xは5より大きい")
elif x == 5:
    print("xは5と等しい")
else:
    print("xは5より小さい")

# for文
for i in range(5):
    print(i)

# while文
n = 0
while n < 5:
    print(n)
    n += 1  #n=n+1

# 1〜10の2乗をfor文で出力
for i in range(1, 11):
    print(f"i={i}, i²={i**2}")