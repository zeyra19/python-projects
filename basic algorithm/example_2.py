#özet: harfleri tersine çevirir
title = "bu benim başlığım"
index = "BU DA BENİM İÇERİĞİM"

print(title.swapcase())
print(index.swapcase())


#özet: istenilen karakterin değişkende kaç kere geçtiğini söyler
p = "oğulcana"
print(p.count("a"))


#özet: kullanıcıcdan şifre al ve şifrede bir eleman 2 kere kullanılıyorsa uyar
parola = input("Şifreniz:")
sifre_onay_durumu = True

for i in parola:
    if parola.count(i) > 1:
        sifre_onay_durumu = False

if sifre_onay_durumu:
    print("Şifre onaylandı!")
else:
    print("oluşturulmaadı")


#özet: kullanıcıdan geçersiz şifre aldıysa geçerli şifre alana kadar devam ediyuor
def sifre_kontrol():
    while True:
        sifre = input("Şifreniz:")

        for i in sifre:
            if sifre.count(i) > 1:
                print("tekrar eden harf var")
                break
        else:
            print("şifre oluşturuldu")
            break

sifre_kontrol()