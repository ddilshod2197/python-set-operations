# Lug'at (Dictionary) va To'plam (Set) masalasi

# Lug'at (Dictionary)
lugat = {"apple": "o'lma", "banana": "banan", "cherry": "cherry"}

# To'plam (Set)
toplom = {"apple", "banana", "cherry"}

# Lug'atdan ma'lumot olish
def lugatdan_ma'lumot_o'ladi(lugat, key):
    return lugat.get(key)

# To'plamdan ma'lumot olish
def toplamdan_ma'lumot_o'ladi(toplom, key):
    return key in toplom

# Lug'atga yangi ma'lumot qo'shish
def lugatga_yangi_ma'lumot_qo'shadi(lugat, key, value):
    lugat[key] = value

# To'plamga yangi ma'lumot qo'shish
def toplamga_yangi_ma'lumot_qo'shadi(toplom, key):
    toplom.add(key)

# Lug'atdan ma'lumot o'chirish
def lugatdan_ma'lumot_o'chiradi(lugat, key):
    if key in lugat:
        del lugat[key]

# To'plamdan ma'lumot o'chirish
def toplamdan_ma'lumot_o'chiradi(toplom, key):
    if key in toplom:
        toplom.remove(key)

# Lug'atni ko'rsatish
def lugatni_korsatadi(lugat):
    for key, value in lugat.items():
        print(f"{key}: {value}")

# To'plamni ko'rsatish
def toplamni_korsatadi(toplom):
    for key in toplom:
        print(key)

# Test qismi
lugatga_yangi_ma'lumot_qo'shadi(lugat, "grape", "greyp")
lugatga_yangi_ma'lumot_qo'shadi(lugat, "pear", "pere")
toplomga_yangi_ma'lumot_qo'shadi(toplom, "grape")
toplomga_yangi_ma'lumot_qo'shadi(toplom, "pear")

lugatni_korsatadi(lugat)
toplomni_korsatadi(toplom)

print(lugatdan_ma'lumot_o'ladi(lugat, "apple"))
print(toplamdan_ma'lumot_o'ladi(toplom, "apple"))

lugatdan_ma'lumot_o'chiradi(lugat, "apple")
toplamdan_ma'lumot_o'chiradi(toplom, "apple")

lugatni_korsatadi(lugat)
toplomni_korsatadi(toplom)
