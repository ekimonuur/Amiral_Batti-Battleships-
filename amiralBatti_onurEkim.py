import random #bilgisayarın harita koordinatlarının rastegele seçilmesi

com_savasGemisi = [0, 0] #savaş gemileri
player_savasGemisi = [0, 0]
gemi_sayisi = 5
yapay_gemi = [0, 0] #rastgele oluşturulan gemilerin tekrar etmemesini kontrol etmek için

okyanus1 = [[0 for i in range(5)] for j in range(5)] #harita oyuncu
okyanus2 = [[0 for i in range(5)] for j in range(5)] #harita bilgisayar

def computer_gemi(gemi):
    ship_coordinates = [] #boş bir liste ile rastgele üretilen değerleri tutar

    while len(ship_coordinates) < gemi_sayisi: #tekrar etmeyen koordinatlar grilinceye kadar dönecek
        yapay_gemi[0] = random.randrange(5)    #yapa_gemi kontrol amaçlı 
        yapay_gemi[1] = random.randrange(5)
        if gemi not in ship_coordinates:        #tekrar etmiyorsa ekler
            ship_coordinates.append(list(yapay_gemi))
    
    for i in range(gemi_sayisi):
        koordinat = ship_coordinates[i]         #ship_coordinates ın değerleri alınır ve savaş gemisinin koordinatları tutulup yollanır
        gemi[0] = koordinat[0]
        gemi[1] = koordinat[1]
        computer_gemi_yerlestir(okyanus2, com_savasGemisi)

def computer_gemi_yerlestir(okyanus2, c_gemi): #haritada girilen koordinatlara göre yerleştirme
    x = c_gemi[0]
    y = c_gemi[1]
    okyanus2[x][y] = 1 #gemi var ise 1 yok ise 0

#bilgisayarın haritasını oyuncu görmemesi için oluşturulmadı. istenirse hazır .

# def computer_harita_olustur(harita): 
#     for i in range(5):
#         for j in range(5):
#             print(harita[i][j], end=' ')
#         print()

def c_hamle_yap(isim, harita):
    print(f"{isim} atış yapacak mürettebat sıkı tutununn !") 
    hedef = []
    hedef_list = []
    for i in range(5):                                          
        for j in range(5):
            hedef.append(harita[i][j])                          #oyuncunun haritasında her satırda ki değeri hedef listesine liste olarak atar.[1,0,1] gibi
        hedef_list.append(hedef)                                #satırların listesi halinde bütün değerleri tutar [[1,0,1],[0,0,1],[1,0,0]] gibi

    for a in hedef_list:                           #hedef_listin elemanlarını dolaşır bulunduğu satırda "1" in olup olmadığını kontrol eder.yoksa sonraki satıra atlar

        if 1 in hedef_list[a]:
            reastgele_secilen = random.choice(hedef_list[a])        #satırda bir var ise random.choice ile rastgele değer seçer
            if reastgele_secilen == 1:                              #rastgele_secilen 1 ise haritada 1 i 0 yapar
                index = hedef_list.index(reastgele_secilen)         #buradaki seçimler ile bilgisayar ilk etapta 5 satır olduğu için yüzde 20 olan şansını
                if (harita[a][index] == 1): # 1 olan kolonu seçerek ilk etapta doğruu kolon seçme ihtimali %100 oluyor. Sonraki aşamada ise random ile yüzde 20 atış imkanı doğuyor.
                    harita[a][index] = 0
                    return True
                else:
                    return False


def gemi_gir(gemi):
    for i in range(gemi_sayisi):
        print("Amiral gemilerimizi yerleştirmek için emirlerinizi bekliyoruz")
        gemi[0] = int(input(f"gemi {i+1} x koordinatı:"))
        gemi[1] = int(input(f"gemi {i+1} y koordinatı:"))
        haritaya_gemi_yerlestir(okyanus1, player_savasGemisi)

def haritaya_gemi_yerlestir(okyanus1, p_gemi):
    x = p_gemi[0]
    y = p_gemi[1]
    okyanus1[x][y] = 1

def player_harita_olustur(harita): #oyuncunun kendi gemilerinin bulunduğu tahtası gösterilir
    for i in range(5):
        for j in range(5):
            print(harita[i][j], end=' ')
        print()

def p_hamle_yap(isim, harita, ammo):
    print(f'{isim} atış için hazırız hamle sırası bizde: ')
    x = int(input('(0,4) arasında X koordinatı gir: '))
    y = int(input('(0,4) arasında Y koordinatı gir: '))
    if (harita[x][y] == 1):  # girilen koordinat 1 ise atış isabetlidir. değer 0 a dönüştürülür. boolean döndürülür
        harita[x][y] = 0
        return True
    else:
        ammo -=1
        return False

def galibiyet_kontrol(harita):
    for i in range(5):
        for j in range(5):
            if harita[i][j] == 1: #oyun tahtasında 1 kalmadıysa oyun biter
                return False
    return True

if __name__ == '__main__':
    text = r"""
______  ___ _____ _____ _      _____ _____ _   _ ___________ 
| ___ \/ _ \_   _|_   _| |    |  ___/  ___| | | |_   _| ___ \
| |_/ / /_\ \| |   | | | |    | |__ \ `--.| |_| | | | | |_/ /
| ___ \  _  || |   | | | |    |  __| `--. \  _  | | | |  __/ 
| |_/ / | | || |   | | | |____| |___/\__/ / | | |_| |_| |    
\____/\_| |_/\_/   \_/ \_____/\____/\____/\_| |_/\___/\_|    
                                                             
"""     
    print(text)

    p1 = 'Amiral'
    c1 = 'Korsanlar'

    print("Lütfen oynamak istediğiniz zorluk seviyesini seçiniz : \n")
    print('Kolay(15 atış hakkı--  Orta(12 atış)  Zor(8 atış)\n')
    zorluk = input("kolay için 'k' --- Orta için 'o' --- Zor için 'z' giriniz")
    if (zorluk == 'k'):
        ammo = 15
    elif (zorluk == 'o'):
        ammo = 12
    else:
        ammo = 8


    print('Amiral güzel bir strateji ile gemilerimizi x ve y koordinatında  dizelim :\n')
    gemi_gir(player_savasGemisi)
    player_harita_olustur(okyanus1)

    print("Düşman gemilerini yerleştiriyor!! Hazırlanın")
    computer_gemi(com_savasGemisi)
    # computer_harita_olustur(okyanus2)

    player_atis = True
    computer_atis = True

    while True:
        while player_atis:
            player_atis = p_hamle_yap(p1, okyanus2, ammo)
            if player_atis:
                print('OOOO Tam isabet, Zafere bizim olacak !')
                # computer_harita_olustur(okyanus2)
                sonuc = galibiyet_kontrol(okyanus2)
                if ammo <=0:
                    print("Amiral kızma ama bütün cephaneyi bitirdik. Savaşı kaybettik")
                    exit(0)
            
                if sonuc:
                    print('Tebrikler Amiral kazandınız! Deniz sularımızı bu hain korsanlardan temizlediniz. ')
                    exit(0)
            else:
                print("Amiral gözlerinizde miyop olabilir mi ? Atış karavana")
                computer_atis = True
        while computer_atis:
            computer_atis = c_hamle_yap(c1, okyanus1)
            if computer_atis:
                print("Korsanların kaptanı Jack Sparrow olmalı. Bir gemimizi daha kaybettik :(")
                player_harita_olustur(okyanus1)
                sonuc = galibiyet_kontrol(okyanus1)
                if sonuc:
                    print('Resifin derinliklerinde balıklar için yeni bir yaşam alanı daha !! Amiral kaybettiniz Korsanlar kazandı !')
                    exit(0)
            else:
                print("Amiral korsanlar rom'u fazla kaçırmış heralde yine. Şans bizden yana, atış karavana :) ")
                player_atis = True