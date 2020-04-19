# COVID-19 Twitter Veritabanı: Türkiye Örneklemi

Bu veriseti çalışması, 2020 yılının ilk aylarından beri dünyada etkisini gösteren COVID-19 virüsünün Türkçe konuşan Twitter kullanıcılarının gündemini tespit etmek amacıyla kurulmuştur. Aşağıda bu araştırmanın dizaynı, içeriği ve kullanılan kodlar özetlenecektir. Aynı zamanda, bu verisetini kullanarak yürütülebilecek gelecek çalışmalara bazı tavsiyeler de sıralanacaktır. 

## Araştırmanın Dizaynı

Araştırma sırasıyla aşağıdaki adımlar izlenerek tasarlanmıştır:

### Anahtar kelimelerin çıkarılması ve temalara bölünmesi
6 başlık altında kelime listesi çıkarılmıştır:
  * COVID-19: Covid-19, Covid 19, Kovid-19, korona, koronavirus, virüs, corona 
  * Politika: Bilim Kurulu, Bakan, Başkan, Sağlık Bakanlığı, Savaş, Seferberlik, Barış Pınarı, Fahreddin Koca, Cumhurbaşkanı
  * Ülkeler: Çin, Avrupa, Amerika, İngiltere, İtalya, İspanya, Almanya, Fransa, Japonya, Güney Kore, İran, Türkiye, DSÖ (WHO), Nato, İsrail
  * Dezenformasyon: Asılsız, provakatif, sahte, provakasyon, palavra, komplo, oyun, büyük oyun,  siyonizm
  * Din: Diyanet, cami, Cuma, muska, din, ezan, sela, sabır, müsibet, musibet, 
  * Ekonomi:Kredi, burs, işsiz, işsizlik, nakit, destek, dayanışma, gıda, mücadele, memur, şirket, gümrük
  
### Verilerin Tarih Aralığının Belirlenmesi
  * Yukarıda belirtilen kelime havuzları iki tarih aralığı belirlenerek ayrı ayrı depolanmıştır. 
  * Türkiye'de ilan edilen ilk vaka 11 Mart tarihindedir. 
  * Verileri önce ve sonra diye iki ayrı şekilde ayırmamızın amacı, gündemlerdeki süreklilik ve kırımlımların belirlenmesini kolaylaştırmaktır.
  * 11 Mart öncesi gündem, İran'da açıklanan ilk vaka tarihi olan 19 Şubat ile sınırlandırılmıştır. Buradaki amaç, Ortadoğu ve Avrupa bölgelerinde ilk vakaların açıklanmasını bir dönüm noktası olarak belirlemektir. 
  * Veriler 7 Nisan tarihine kadar çekilmiştir. Bu tarih Türkiye'de ilk vakanın açıklanmasından yaklaşık olarak bir ay sonrasına denk gelmektedir. 
  * Bu açılardan, bu dosyadaki veriseti ilk vakanın açıklanmasından önce ve sonraki gündem değişimlerini ve sürekliliklerini incelemeye imkan tanımaktadır.

### Verilerin Depolanması ve ID'lerin Çıkarılması
  * Twitter'ın [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy) ile uyumlu olarak toplanılan twitlerin sadece Tweet ID'leri temalara bölünerek dosyalar halinde depolanmıştır.
  * Bu ID'leri kullanarak çalışma yapmak isteyenler için [Hydrator](https://github.com/DocNow/hydrator) and [Twarc](https://github.com/DocNow/twarc) gibi araçları kullanmayı tavsiye ediyoruz. Detaylı talimatlar için linklerdeki açıklamalara bakılabilir. 

## Kullanılan Kodlar


## Temel Çıktılar


## Gelecek Çalışmalar






