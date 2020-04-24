# COVID-19 Twitter Veritabanı: Türkiye Örneklemi

## Araştırmanın Amacı ve İçeriği

Bu veri seti çalışması, 2020 yılının ilk aylarından beri dünyada etkisini gösteren COVID-19 virüsünün Türkçe konuşan Twitter kullanıcılarının gündemine tesirini tespit etmek amacıyla kurulmuştur.  Bu çalışma halihazırda birçok dilde hazırlanan kapsamlı bir Twitter veri setinin [#COVID-19: The First Public Coronavirus Twitter Dataset](https://github.com/echen102/COVID-19-TweetIDs) tamamlayacısı olarak görülebilir. Böyle bir çalışmanın şimdiye kadar yapılmamış olması bizi motive eden önemli bir nedendir. Yukarda belirtilen çalışmada ise kelime havuzunun dar olması ve temalara göre ayrılmaması, Türkçe tweet sayısının az olması, Türkçe tweetleri ayıklamaktaki zorluklar yeni bir veri seti çıkarmayı zorunlu hale getirmiştir. 

"COVID-19 Twitter Veri Tabanı: Türkiye Örneklemi" adlı bu çalışmada tweetler hem temalara göre ayrı ayrı elde edilmiş hem de açıklanan ilk vakanın öncesi ve sonrasındaki gündemler ayrı ayrı tespit edilmiştir. Araştırma, aynı zamanda, Türkçe yazan Twitter kullanıcılarının Ortadoğu ve Avrupa'da vakaların artmasıyla beraber koronavirüsü gündemlerine aldıklarını ve Türkiye'de ilk vakanın açıklanmasıyla birlikte hem dini hem ekonomik hem politik hem de dış ülkeler hakkındaki gündemlerinde kırılmalar olduğunu varsaymaktadır. Bu raporda, bu kırılmaları göstermek için en çok geçen kelimeler üzerinden bir ön analiz sunulacaktır. 

## Araştırmanın Dizaynı

Aşağıda bu araştırmanın dizaynı, içeriği ve kullanılan kodlar özetlenecektir. Aynı zamanda, bu veri setini kullanarak yürütülebilecek gelecek çalışmalara bazı tavsiyeler sıralanacaktır. İlk olarak, anahtar kelimeler temalara göre çıkartılmıştır. Daha sonra, tarih aralığı belirlenip tweetler çekilmiştir. Elde edilen tweetler, Twitter'ın [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy) ile uyumlu olarak ID'ler halinde herkese açık olarak depolanmıştır. En sonunda ise programlamalı metin analizi teknikleri kullanılarak tweetler üzerinden temel çıktılar alınıp takdim edilmiştir. 

### Anahtar kelimelerin çıkarılması ve temalara bölünmesi

Temalar, COVID-19 tartışmaları döneminde muhtemel olarak etkilenen veya etkilenebilecek alanlar olan politika, ekonomi, din, dezenformasyon, dış ülkeler hakkındaki algılar, ve virüsün kendisi olarak belirlenmiştir. Bu 6 başlık altındaki anahtar kelimeler rastgele tweet araması yapılıp okuma yapılarak çıkarılmıştır:

  * COVID-19: Covid-19, Covid 19, Kovid-19, korona, koronavirus, virüs, corona 
  * Politika: Bilim Kurulu, Bakan, Başkan, Sağlık Bakanlığı, Savaş, Seferberlik, Barış Pınarı, Fahreddin Koca, Cumhurbaşkanı
  * Ülkeler: Çin, Avrupa, Amerika, İngiltere, İtalya, İspanya, Almanya, Fransa, Japonya, Güney Kore, İran, Türkiye, DSÖ (WHO), Nato, İsrail
  * Dezenformasyon: Asılsız, provakatif, sahte, provakasyon, palavra, komplo, oyun, büyük oyun,  siyonizm
  * Din: Diyanet, cami, Cuma, muska, din, ezan, sela, sabır, müsibet, musibet, 
  * Ekonomi: Kredi, burs, işsiz, işsizlik, nakit, destek, dayanışma, gıda, mücadele, memur, şirket, gümrük
  
### Verilerin Tarih Aralığının Belirlenmesi

  * Yukarıda belirtilen kelime havuzları iki tarih aralığı belirlenerek ayrı ayrı depolanmıştır. 
  * Türkiye'de ilan edilen ilk vaka 11 Mart tarihindedir. 
  * Verileri önce ve sonra diye iki ayrı şekilde ayırmamızın amacı, gündemlerdeki süreklilik ve kırılımların belirlenmesini kolaylaştırmaktır.
  * 11 Mart öncesi gündem, İran'da açıklanan ilk vaka tarihi olan 19 Şubat ile sınırlandırılmıştır. Buradaki amaç, Ortadoğu ve Avrupa bölgelerinde ilk vakaların açıklanmasını bir dönüm noktası olarak belirlemektir. 
  * Veriler 7 Nisan tarihine kadar çekilmiştir. Bu tarih Türkiye'de ilk vakanın açıklanmasından yaklaşık olarak bir ay sonrasına denk gelmektedir. 
  * Bu açılardan, bu dosyadaki veri seti ilk vakanın açıklanmasından önce ve sonraki gündem değişimlerini ve sürekliliklerini incelemeye imkan tanımaktadır.

### Verilerin Depolanması ve ID'lerin Çıkarılması

  * Twitter'ın [Terms of Service](https://developer.twitter.com/en/developer-terms/agreement-and-policy) ile uyumlu olarak toplanılan tweetlerin sadece Tweet ID'leri temalara bölünerek dosyalar halinde depolanmıştır. ID'ler çıkarılırken tekrar eden  tweetler temizlenerek her tema için özgün tweetlerden oluşan veri setleri oluşturulmuştur.
  * Bu ID'leri kullanarak çalışma yapmak isteyenler için [Hydrator](https://github.com/DocNow/hydrator) and [Twarc](https://github.com/DocNow/twarc) gibi araçları kullanmayı tavsiye ediyoruz. Detaylı talimatlar için linklerdeki açıklamalara bakılabilir. 

### Kullanılan Kodlar

Bu çalışma, temel olarak üç kod setine dayanarak yapılmıştır.
 * İlk olarak Twitter'dan veri çekebilmek için Python dilinde yazılmış [Twint](https://github.com/twintproject/twint) paketinden yararlanılmıştır.
 * Daha sonra, elde edilen verileri düzenlemek ve ID'lerini çıkarıp kamusallaştırmak işlemleri gerekli [kodlar](https://github.com/burakozturan/tria-covid19/blob/master/kodlar%20(codes)/data/data_birlestirme.ipynb) kullanılarak gerçekleştirilmiştir.
 * En son olarak, içeriğe dair ilk fikirlerimizi elde etmek için [programlamalı metin analizi kodları](https://github.com/burakozturan/tria-covid19/blob/master/kodlar%20(codes)/analiz/Covid_quantitative_text_analysis.ipynb)
kullanılmıştır.

## Temel Çıktılar

Bu bölümde ilk olarak tweetlerin temel istatistikleri sunulacaktır. Daha sonra, elde edilen tweetler üzerinden, ilk vakanın açıklanmasının öncesi ve sonrasında en çok geçen kelimeler veya anahtar kelimeler [tablolar](https://github.com/burakozturan/tria-covid19/tree/master/sonuç%20tabloları) halinde görselleştirilecektir. Önemli görülen devamlılık ve kırılmalar kısaca not edilecektir. Daha detaylı analizler bir sonraki çalışmanın araştırma konusu olacaktır.

### Temel İstatistikler
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


### Temel Görseller

**Tablo 1: COVID hakkındaki en çok geçen kelimeler**

![COVID](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Covid_karşılaştırma.png)

* Öncesinde, İran, İtalya ve Çin gibi vakaların yoğunlukla görüldüğü yerlere sıkça referans verilmiştir. Bu bize, Türkiye'deki ilk vakanın açıklanmasından önce de dış ülkelere yönelik gündemin virüs yoğunluklu olduğunu göstermektedir. Vaka açıklandıktan sonra ise Allah ve sağlık gibi kelimeler öne çıkmaktadır. Bu durum bize Türkçe yazan twitter kullanıcılarının süreci dini argümanlar ile açıkladığına dair bir fikir sunmaktadır. 

**Tablo 2: Din hakkındaki en çok geçen kelimeler**

![Din no keywoord](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Din_comparison_no_keyword.png)

* Daha önce şehit vurgusu yüksek iken, COVID-19 sonrası dönemde dua vurgusunun ön plana çıktığı görülmektedir. 

**Tablo 3: Politika hakkındaki anahtar kelimeler**

![politika](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Politikaaaaa_comparison.png)

* Daha önce mülteci ve şehit vurguları öne çıkarken, sonrasında bilim ve sağlık vurgusu göze çarpmaktadir. 

**Tablo 4: Dezenformasyon hakkındaki anahtar kelimeler**

![Dezenformasyon](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Dezenformasyon_Karşılaştırma.png)

* Komplo kelimesindeki bariz artış, Türkçe konuşan twitter kamuoyunun olası dezenformasyonlara açık olduğunu göstermektedir. 

**Tablo 5: Ekonomi hakkındaki anahtar kelimeler**

![ekonomi](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Ekonomi_Karşılaştırma.png)

* Daha önceleri doların durumu ve işsizlik gibi temalar öne çıkarken, sonrasında ise sokağa çıkma yasağı ve devlet temaları öne çıkmaktadır. Devlet kelimesini ön plana çıkması sorunun çözümünün devlet elinde görüldüğüne dair bir fikir verebilir.

**Tablo 6: Ülkeler hakkindaki anahtar kelimeler**

![ulkeler](https://github.com/burakozturan/tria-covid19/blob/master/sonuç%20tabloları/Ulkeler_Karşılaştırma.png)

* İlk donemde, Türkiye'nin son dönem dış politikasında önemli bir yer tutan Suriye, İdlib ve Rusya öne çıkmaktadır. Daha sonra ise, Almanya, AB, ABD ve İtalya gündemde öne çıkan kelimeler olarak göze çarpmaktadır. Batı'nın yoğunlukla ülke gündemine girmesi ayrıca çalışılması gerekli olan bir araştırma konusudur.


## Gelecek Çalışmalar

Bu veri seti çalışması öncelikli olarak gelecek çalışmalara zemin hazırlamak için tasarlanmıştır. Vakit sınırlılığından dolayı sadece en çok geçen kelimeler karşılaştırmalı olarak sunulmuş ve bunlar üzerinden görülebilecek temel süreklilik ve kırılmalar not alınmıştır. 

Bundan sonraki süreçte;

* Tweet içerikleri daha detaylı bir şekilde incelenilerek Türkçe konuşan Twitter kullanıcılarınn gündem değişiklikleri, kırılımları, ve devamlılıkları tespit edilebilir. 

* 'Topic Modelling' gibi makine öğrenmesi metodları kullanılarak içerik hakkında farklı çalışmalar yapılabilir. 

## Detaylı Bilgi İçin

Bu veri seti hakkındaki teknik sorular ya da içeriğe dair sorularınız için aşağıdaki iletişim maillerine yazabilirsiniz.
* Burak Özturan **burakoztrn@gmail.com**
* Yunus Emre Tapan **tapanyemre@gmail.com**



