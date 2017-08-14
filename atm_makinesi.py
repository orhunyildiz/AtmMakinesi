print("""************************************
ATM Makinesine Hoşgeldiniz.

İşlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için 'q' ya basın.
************************************
""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz: ")
    if (işlem == "q"):
        print("Yine bekleriz.")
        break
    elif (işlem == "1"):
        print("Bakiyeniz: {} TL".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        if (miktar <= 0):
            print("Böyle bir miktar yatıramazsaınız.")
            continue
        bakiye += miktar
    elif (işlem == "3"):
        miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if (miktar > bakiye):
            print("Böyle bir miktar çekemezsiniz.")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem.")