#リスト
temperatures=[20.5, 21.3, 19.8, 22.1, 20.0]

print(temperatures[0])
print(temperatures[-1])
print(len(temperatures))

#リストの操作
temperatures.append(23.0)
print(temperatures)

#for文でリストを回す
for t in temperatures:
    print(f"{t}℃")

#リスト内包表記
squared=[x**2 for x in range(1, 6)]
print(squared)

#辞書
particle={"name": "electron", "mass": 9.11e-31, "charge": -1.6e-19}

print(particle["name"])
print(particle["mass"])

#辞書をfor文で回す
for key, value in particle.items():
    print(f"{key}: {value}")
               