mevcutPara=1000



islem=0
while(islem!=4):
    print("***1-Para Yatırma***")
    print("***2-Para Çekme***")
    print("***3-Bakiye Sorgula***")
    print("***4-Kart İade***")
    islem=int(input("Yapmak İstediğiniz İşlemi Seçiniz...: "))
    if islem==1:
        yDeger=int(input("Yatırmak istediğiniz değerini giriniz: "))
        mevcutPara=yDeger+mevcutPara
        print("*****İşlem Başarılı*****")
        input("Devam etmek için enter a basın")
        continue;
    elif islem==2:
        cDeger=int(input("Çekmek istediğiniz değerini giriniz: "))
        mevcutPara=mevcutPara-cDeger
        print("*****İşlem Başarılı*****")
        input("Devam etmek için enter a basın")
        continue;
    elif islem==3:
        print("Bakiyeniz: {}".format(mevcutPara))
        input("Devam etmek için enter a basın")
        continue;
    else:
        print("Kartınız iade ediliyor....")
        break;
        
    
           
        

