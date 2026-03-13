#基本的な関数
def greet(name):
    return f"こんにちは、{name}さん！"

print(greet("物理"))

#引数が複数ある関数
def add(a,b):
    return a+b

print(add(3,5))

#運動エネルギーを計算する関数
def kinetic_energy(m,v):
    return 0.5 * m * v**2

print(f"運動エネルギー: {kinetic_energy(2,3)} J")

#デフォルト引数
def kinetic_energy_default(m,v=1.0):
    return 0.5 * m * v**2

print(f"v=1のとき:{kinetic_energy_default(2)} J")
print(f"v=3のとき:{kinetic_energy_default(2,3)} J")
