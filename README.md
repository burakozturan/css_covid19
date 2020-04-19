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
  * Twitter'ın [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy) ile uyumlu olarak toplanılan twitlerin sadece Tweet ID'leri temalara bölünerek dosyalar halinde depolanmıştır. ID'ler çıkarılırken iki defa çekilen twitler temizlenmiştir.
  * Bu ID'leri kullanarak çalışma yapmak isteyenler için [Hydrator](https://github.com/DocNow/hydrator) and [Twarc](https://github.com/DocNow/twarc) gibi araçları kullanmayı tavsiye ediyoruz. Detaylı talimatlar için linklerdeki açıklamalara bakılabilir. 

### Kullanılan Kodlar
Bu çalışmada temel olarak üç kod setine dayanarak yapılmıştır.
 * İlk olarak Twitter'dan veri çekebilmek için Python dilinde yazılmış [Twint](https://github.com/twintproject/twint) paketinden yararlanılmıştır.
 * Daha sonra, elde edilen verileri düzenlemek ve ID'lerini çıkarıp kamusallaştırmak için bazı [kodları](https://github.com/burakozturan/tria-covid19/blob/master/kodlar%20(codes)/data/data_birlestirme.ipynb) birleştirerek düzenlenmiştir.
 * En son olarak, içeriğe dair ilk fikirlerimizi elde etmek için [hesaplamalı metin analizi kodlarını](https://github.com/burakozturan/tria-covid19/blob/master/kodlar%20(codes)/analiz/Covid_quantitative_text_analysis.ipynb)
kullanılmıştır.

## Temel Çıktılar

Elde edilen twitler üzerinden, ilk vakanın acıklanmasının öncesi ve sonrasi en çok geçen kelimelere göre [tablo](https://github.com/burakozturan/tria-covid19/tree/master/sonuç%20tabloları) olarak eklenmiştir. 

6 farklı temanın iki farklı zaman diliminde twitlerinin temel istatistikleri aşağıdaki gibidir:

Toplam Twit Sayısı : **4,369,870**

| **Tema**        | Önce          | Sonra            | **Toplam**         |
|-------------    |-----          |------------      |----------------    |
| COVID           | 161,109       | 1,427,569        | 1,588,678          |
| Politika        | 355,992       | 367,992          | 723,984            |
| Dezenformasyon  | 51,521        | 88,007           | 139,528            |
| Din             | 215,699       | 436,309          | 652,008            |
| Ekonomi         | 19,532        | 74,682           | 94,214             |
| Ülkeler         | 326,030       | 845,428          | 1,171,458          |
| **Toplam**      | 1,129,883     | 3,239,987        | **4,369,870**      |

## Gelecek Çalışmalar

Bu veriseti çalışması öncelikli olarak gelecek çalışmalara zemin hazırlamak için tasarlanmıştır. Vakit sınırlılığından dolayı sadece en çok geçen kelimeler karşılaştırmalı olarak sunulmuştur. 

Bundan sonraki süreçte, twit içerikleri daha detaylı bir şekilde incelenilerek Türkçe konuşan Twitter kullanıcılarınn gündem değişiklikleri, kırılımları, ve devamlılıkları tespit edilmeli ve bilimsel çalışmaları desteklemelidir. 

## Detaylı Bilgi İçin

Bu veriseti hakkındaki teknik sorular ya da içeriğe dair sorularınız için aşağıdaki iletişim maillerine yazabilirsiniz.
* Burak Özturan **burakoztrn@gmail.com**
* Yunus Emre Tapan **tapanyemre@gmail.com**



