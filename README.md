# COVID-19 Twitter Veritabanı: Türkiye Örneklemi

## Araştırmanın Amacı

Bu veriseti çalışması, 2020 yılının ilk aylarından beri dünyada etkisini gösteren COVID-19 virüsünün Türkçe konuşan Twitter kullanıcılarının gündemini tespit etmek amacıyla kurulmuştur. Bu çalışma halihazırda birçok dilde hazırlanan kapsamlı bir Twitter verisetinin [#COVID-19: The First Public Coronavirus Twitter Dataset](https://github.com/echen102/COVID-19-TweetIDs) tamamlayacısı olarak görülebilir. Bu çalışmayı yapmaya ihtiyaç görmemimizin nedenleri şöyle sıralanabilir; yukarda belirtilen çalışmanın kelime havuzunun dar olması ve temalara göre ayrılmaması, Türkçe tweet sayısının az olması, Türkçe tweetleri ayıklamaktaki zorluklardır. COVID-19 Twitter Veritabanı: Türkiye Örneklemi adlı bu çalışmada twitler hem temalara göre ayrı ayrı elde edilmiş hem de açıklanan ilk vakanın öncesi ve sonrasındaki gündemler ayrı ayrı tespit edilmiştir. Araştırma, aynı zamanda, Türkçe yazan Twitter kullanıcılarının Ortadoğu ve Avrupa'da vakaların artmasıyla beraber koronavirüsü gündemlerine aldıklarını ve Türkiye'de ilk vakanın açıklanmasıyla birlikte hem dini hem ekonomik hem politik hem de dış ülkeler hakkındaki gündemlerinde kırılmalar olduğunu varsaymaktadır. Bu raporda, bu kırılmaları göstermek için en çok geçen kelimeler üzerinden bir ön analiz sunulacaktır. 

## Araştırmanın Dizaynı

Aşağıda bu araştırmanın dizaynı, içeriği ve kullanılan kodlar özetlenecektir. Aynı zamanda, bu verisetini kullanarak yürütülebilecek gelecek çalışmalara bazı tavsiyeler de sıralanacaktır. 

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

**Tablo 1: COVID hakkindaki anahtar kelimeleri**

![COVID](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Covid_karşılaştırma.png)

* Oncesinde, Iran, Italya ve Cin gibi vakalarin yogunlukla goruldugu yerlere sikca referans verilmistir. Bu bize, vakanin aciklanmasindan oncede dis ulkelere yonelik gundemin virus yogunluklu oldugunu gostermektedir. Vaka aciklandiktan sonra ise Allah ve saglik gibi kelimeler one cikmaktadir. Bu durum bize Turkce yazan twitter kullanicilarinin sureci dini argumanlarlar ile acikladigina dair bir fikir verebilir. 

**Tablo 2: Din hakkindaki anahtar kelimeleri**

![Din no keywoord](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Din_comparison_no_keyword.png)

* Daha once sehit vurgusu yuksek iken, COVID-19 sonrasi donemde dua vurgusunun on plana ciktigi gorulmektedir. 

**Tablo 3: Politika hakkindaki anahtar kelimeleri**

![politika](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Politikaaaaa_comparison.png)

* Daha once multeci ve sehit vurgulari one cikarken, sonrasinda bilim ve saglik vurgusu goze carpmaktadir. 

**Tablo 4: Dezenformasyon hakkindaki anahtar kelimeleri**

![Dezenformasyon](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Dezenformasyon_Karşılaştırma.png)

* Komplo kelimesindeki bariz artis, Turkce konusan twitter kamuoyunun olasi dezenformasyonlara acik oldugunu gostermektedir. 

**Tablo 5: Ekonomi hakkindaki anahtar kelimeleri**

![ekonomi](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Ekonomi_Karşılaştırma.png)

* Daha onceleri dolarin durumu ve issizlik gibi temalar one cikarken, sonrasinda ise sokaga cikma yasagi ve devlet temalari one cikmaktadir. 

**Tablo 6: Ulkeler hakkindaki anahtar kelimeleri**

![ulkeler](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Ulkeler_Karşılaştırma.png)

* Ilk donemde, Turkiye'nin son donem dis politikasinda onemli bir yer tutan suriye, idlib ve rusya one cikmaktadir. Daha sonra ise, Almanya, AB, ABD ve Italya gundemde one cikan kelimeler olarak goze carpmaktadir. 


## Gelecek Çalışmalar

Bu veriseti çalışması öncelikli olarak gelecek çalışmalara zemin hazırlamak için tasarlanmıştır. Vakit sınırlılığından dolayı sadece en çok geçen kelimeler karşılaştırmalı olarak sunulmuştur. 

Bundan sonraki süreçte, twit içerikleri daha detaylı bir şekilde incelenilerek Türkçe konuşan Twitter kullanıcılarınn gündem değişiklikleri, kırılımları, ve devamlılıkları tespit edilmeli ve bilimsel çalışmaları desteklemelidir. 

## Detaylı Bilgi İçin

Bu veriseti hakkındaki teknik sorular ya da içeriğe dair sorularınız için aşağıdaki iletişim maillerine yazabilirsiniz.
* Burak Özturan **burakoztrn@gmail.com**
* Yunus Emre Tapan **tapanyemre@gmail.com**



