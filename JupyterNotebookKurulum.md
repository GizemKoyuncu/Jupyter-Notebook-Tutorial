# JUPYTER NOTEBOOK TUTORIAL

## Merhaba,

>  <span class="emoji">🔉 </span> NOT: EĞER BİLGİSAYARINIZDA PYTHON 2.7 SÜRÜMÜNÜN ÜSTÜ VE PİP KURULU İSE SADECE  **pip install jupyterlab** KOMUTU İLE KURULUMU GERÇEKLEŞTİREBİLİRSİNİZ. KURULUM GERÇEKLEŞTRİKTEN SONRA TERMİNALE **jupyter notebook** YAZARAK AÇABİLİRSİNİZ. DOKÜMANIN DEVAMINI OKUMANIZA GEREK YOK.

> <span class="emoji">✔️</span> NOT2: Jupyter notebook programını açmak için terminale küçük harf büyük harf farketmeksizin istediğiniz gibi JuPyTER NOTebook yazabilirsiniz.

Bu repository'de Python programlama dili ile geliştirme yapmak için seçmiş olduğum kullanımı çok kolay Jupyter Notebook programının Windows, Ubuntu ve macOS'a kurulumunu anlatacağım.
Öncelikle kısaca temel kavramlara değinmek gerekirse;

Python çok çeşitli uygulamalar için kullanılabilen öğrenmesi kolay, etkileşimli, hazır kütüphaneleri ve frameworkları kullanmayı sağlayan bir programlama dilidir. Pyhon için hazır kütüphaneleri veya frameworkları PyPI (Python Paket Dizini) adı verilen merkezi bir depoda bulabilirsiniz. Bu hazır kütüphaleri indirmek, kurmak ve yönetmek kısmı zor olan kısımdır. Python PIP gibi basit ve anlaşılır bir komutla kurmanıza, yeniden yüklemenize ve kaldırmanıza izin verir. PIP kısaltmasının açılımı “Preferred Installer Program” dır.

Jupyter Notebook, bir web tarayıcısı üzerinden notebook belgesi formatındaki kodları düzenlemeyi ve çalıştırmayı sağlayan çeşitli programlama dilleri için etkileşimli bir ortam sağlayan açık kaynak kodlu bir sunucu-istemci uygulamasıdır. Jupyter sadece Python ile değil, R, Julia, Ruby, ve Haskell gibi programlama dilleri ile de kullanılabilir. Bu programlama dilleri için ekstra yüklemeler yapılmalıdır.

Üç farklı bilgisayara aynı zamanda üç farklı işletim sistemine jupyter notebook kurulumunu gerçekleştirdim. Daha detaylı bilgi paylaşmak adına detayları dokümanda paylaşıyorum.

## Windows İşletim Sistemine Kurulum

1.  İşletim sistemi genel bilgileri, komut satırına **ver** komutu ile öğrenebilirsiniz.

![adım0-işletim sistemi](https://user-images.githubusercontent.com/61363621/75111537-046d5a00-564c-11ea-8f45-1d35f9cb55fb.png)

2. Python programını indirelim. [Buraya](https://www.python.org/downloads/), tıklayarak bilgisayarınıza uygun olan Python sürümünü indirebilirsiniz. Python 2.7 sürümü üzerindeki sürüm Jupyter Notebook için uygundur.

![adım1-python indirme](https://user-images.githubusercontent.com/61363621/75111587-c290e380-564c-11ea-9ec6-d1e78e093cef.png)

3. İndirme işlemini tamamladıktan sonra python kurulumunu gerçekleştirebilirsiniz. Kurulum için detaylı bilgiyi [Buraya](https://tutorial.djangogirls.org/tr/python_installation/) tıklayarak ulaşabilirsiniz.

4. Python kurulumu tamamladıktan sonra terminalden **python --version** komutu ile kontrol edelim. Eğer terminalden versiyon bilgisi dönüyorsa Python kurulumu başarılı demektir, diğer adıma geçebilirsiniz.

![adım3-python versiyon](https://user-images.githubusercontent.com/61363621/75111661-8316c700-564d-11ea-8e2f-1b882122b8e4.png)

5. Kolay kurulum yapmak için pip dosyasını indirme işlemini yapalım. [Buraya](https://bootstrap.pypa.io/get-pip.py) tıklayarak açılan sayfayı ctrl+s ile kaydedelim.

![adım4 pip dosyasını kaydetme](https://user-images.githubusercontent.com/61363621/75111680-beb19100-564d-11ea-9b0b-5c4eb0bf3918.png)

6. Şimdi pip kurulumunu yapabilirsiniz. Ben masaüstüne kaydettiğim için **cd** komutu ile masaüstü dizinine geldim ve  **python** **get-pip.** **py** komutu ile pip kurulumunu gerçekleştirdim. Sizde **cd , cd..** komutu ile ilgili üst/alt dizine giderek kurulumu gerçekleştirebilirsiniz.

![adım5-pip kurma](https://user-images.githubusercontent.com/61363621/75111690-ec96d580-564d-11ea-8ccd-b264058e0e95.png)

7. Pip kurulumu tamamladıktan sonra terminalden **pip --version** komutu ile kontrol edelim. Eğer terminalden versiyon bilgisi dönüyorsa pip kurulumu başarılı demektir, diğer adıma geçebilirsiniz.

![adım6-pip versiyon](https://user-images.githubusercontent.com/61363621/75111705-fe787880-564d-11ea-8c98-1431d9866aa5.png)

8. Şimdi sırada Jupyter Notebook kurulumu var. **pip install jupyterlab** komutu ile kurulumu gerçekleştirebilirsiniz.

![adım7-jn kurma](https://user-images.githubusercontent.com/61363621/75111726-1fd96480-564e-11ea-9906-168c5d0abfd7.png)

9. Kurulum işlemi tamamlandığına göre artık terminale **jupyter notebook** yazarak açabiliriz.

![adım8-jupyter notebook](https://user-images.githubusercontent.com/61363621/75111743-4b5c4f00-564e-11ea-87ea-1fbf275a0f62.png)

![adım9-son adım](https://user-images.githubusercontent.com/61363621/75111746-51eac680-564e-11ea-8c32-f70f2b8fd372.png)

10. Jupyter notebook progamını terminalden **ctrl+c** yazarak ya da arayüzden **Quit** butonuna tıklayarak kapatabilirsiniz.


## Ubuntu İşletim Sistemine Kurulum

1.  İşletim sistemi genel bilgileri, komut satırına **cat /proc/version** komutu ile öğrenebilirsiniz.

![adım0-işletim sistemi](https://user-images.githubusercontent.com/61363621/75111811-f0772780-564e-11ea-85fe-7c387779645d.png)

2. Python programını **sudo apt-get install python3** komutu ile kurabilirsiiz. Python 2.7 sürümü üzerindeki sürüm Jupyter Notebook için uygundur.

![adım1-python kurma](https://user-images.githubusercontent.com/61363621/75111835-316f3c00-564f-11ea-8f49-705ca484d761.png)

3. Python kurulumu tamamladıktan sonra terminalden **python3** komutu ile kontrol edelim. Eğer terminalden versiyon bilgisi dönüyorsa Python kurulumu başarılı demektir, diğer adıma geçebilirsiniz.

![adım2-python versiyon](https://user-images.githubusercontent.com/61363621/75111845-41871b80-564f-11ea-83b6-5723c58d3a28.png)

5. Kolay kurulum yapmak için pip dosyasını **sudo apt-get install python3-pip** komutu kuralım.

![adım3-pip kurma](https://user-images.githubusercontent.com/61363621/75111879-76936e00-564f-11ea-8c1d-0f2d7a3f171e.png)

6. Pip kurulumu tamamladıktan sonra terminalden **pip3 -V** komutu ile kontrol edelim. Eğer terminalden versiyon bilgisi dönüyorsa pip kurulumu başarılı demektir, diğer adıma geçebilirsiniz.

![adım4-pip versiyon](https://user-images.githubusercontent.com/61363621/75111886-8dd25b80-564f-11ea-9572-515fdf811f6d.png)

7. Şimdi sırada Jupyter Notebook kurulumu var. **pip install jupyterlab** komutu ile kurulumu gerçekleştirelim.

![adım5-jn kurma](https://user-images.githubusercontent.com/61363621/75111895-a478b280-564f-11ea-8b6e-7e1ff81cb900.png)

8. Kurulum işlemi tamamlandığına göre artık terminale **jupyter notebook** yazarak açabiliriz.

![adım6-jn acma](https://user-images.githubusercontent.com/61363621/75111906-b65a5580-564f-11ea-9586-b60316c0f462.png)

![adım7-jn arayüz](https://user-images.githubusercontent.com/61363621/75111907-be19fa00-564f-11ea-957f-7048d149b046.png)

9. Jupyter notebook progamını terminalden **ctrl+c** yazıp gelen soruya y olarak yanıtlayarak ya da arayüzden **Quit** butonuna tıklayarak kapatabilirsiniz.

## macOS İşletim Sistemine Kurulum

1.  İşletim sistemi genel bilgileri, komut satırına **sw_vers** komutu ile öğrenebilirsiniz.

![adım1-işletim sistemi versiyon](https://user-images.githubusercontent.com/61363621/75112017-de968400-5650-11ea-96ce-699ee0fbccd4.png)

2. Python programını indirme. [Buraya](https://www.python.org/downloads/), tıklayarak bilgisayarınıza uygun olan sürümü indirebilirsiniz. Python 2.7 sürümü üzerindeki sürüm Jupyter Notebook için uygundur.

![adım1-python indirme](https://user-images.githubusercontent.com/61363621/75111587-c290e380-564c-11ea-9ec6-d1e78e093cef.png)

3. İndirme işlemini tamamladıktan sonra python kurulumunu gerçekleştirebilirsiniz. Kurulum için detaylı bilgiyi [Buraya](https://tutorial.djangogirls.org/tr/python_installation/) tıklayarak öğrenebilrsiniz.

3. Python kurulumu tamamladıktan sonra terminalden **python -V** komutu ile kontrol edelim. Eğer terminalden versiyon bilgisi dönüyorsa Python kurulumu başarılı demektir, diğer adıma geçebilirsiniz.

![python versiyon](https://user-images.githubusercontent.com/61363621/75112463-1ef80100-5655-11ea-9b4c-47b63d6ea136.png)

5. Kolay kurulum yapmak için pip dosyasını **easy_install pip3** komutu kuralım. 

![pip install](https://user-images.githubusercontent.com/61363621/75112479-3a630c00-5655-11ea-81aa-efb5f2139df2.png)

6. Pip kurulumu tamamladıktan sonra terminalden **pip3 -V** komutu ile kontrol edelim. Eğer terminalden versiyon bilgisi dönüyorsa pip kurulumu başarılı demektir, diğer adıma geçebilirsiniz.

![pip versiyon](https://user-images.githubusercontent.com/61363621/75112485-4bac1880-5655-11ea-8813-95af15496a6c.png)

7. Şimdi sırada Jupyter Notebook kurulumu var. **pip install jupyterlab** komutu ile kurulumu gerçekleştirelim.

![jn install](https://user-images.githubusercontent.com/61363621/75112491-5ff01580-5655-11ea-8e11-c4cd2ddb85be.png)

8. Kurulum işlemi tamamlandığına göre artık terminale **jupyter notebook** yazarak açabiliriz.

![jn jupyter notebook](https://user-images.githubusercontent.com/61363621/75112442-f07a2600-5654-11ea-9b2a-8383ed83cd94.png)

![jn arayüz](https://user-images.githubusercontent.com/61363621/75112446-f96af780-5654-11ea-9870-6da0c57e1cb0.png)

9. Jupyter notebook progamını terminalden **ctrl+c** yazarak ya da arayüzden **Quit** butonuna tıklayarak kapatabilirsiniz.



> Doküman burada sona erdi. İyi günler   <span class="emoji">😊</span> 