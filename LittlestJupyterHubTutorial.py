#!/usr/bin/env python
# coding: utf-8

# 
# # Littlest Jupyterhub'ı Google Cloud Üzerinde Kurma
# 
# Bu tutorialda takip edeceğimiz tutorialı [buraya](http://tljh.jupyter.org/en/latest/install/google.html) tıklayarak görebilirsiniz.
# 
# **Amacımız:** JupyterHub'ı Google Cloud üzerinde kurarak, kullanıcı erişimlerini sağlamak ve Jupyterhub' ın kullanımını test etmektir.
# 
# **Gereklikler:** Google hesabınız bir hesabınız olmalı.
# 
# 
# ### Step 0 : Google Cloud'a Giriş
# 
# Google Cloud'un 12 aylık ücretsiz kullanımını aktifleştireceğiz.
# 
# 1. Google Cloudun sitesine girerek Ücretsiz kullanmaya başlayın seçeneğini deniyoruz.
# 
# ![Screenshot_22](https://user-images.githubusercontent.com/61363621/79072863-0ff40d80-7cec-11ea-860f-02f0855d81cf.png)
# 
# Hizmet şartlarını kabul ederek Devam butonuna tıklıyoruz.
# 
# ![Screenshot_23](https://user-images.githubusercontent.com/61363621/79072907-3023cc80-7cec-11ea-9330-bdbf9edc53de.png)
# 
# Adres bilgileri ve ödeme yöntemi bilgilerini doldurarak sayfada altta yer alan Ücretsiz Denemeyi Başlat butonuna tıklıyoruz
# 
# ![Adsız3](https://user-images.githubusercontent.com/61363621/79073233-184d4800-7cee-11ea-8770-ea5715e37ec6.png)
# 
# Ve kayıt işlemini tamamlamış oluyoruz.
# 
# ![Screenshot_25](https://user-images.githubusercontent.com/61363621/79073286-695d3c00-7cee-11ea-9006-c0c1c5807a06.png)
# 
# ### Step 1: Littlest JupyterHub Kurulumu
# 
# JupyterHub'ı çalıştırabileceğimiz sunucuyu oluşturarak başlıyoruz.
# 
# 1. Google Hesabınızla Google Cloud Console'da oturum açın.
# 
# 2. Sayfanın sol üst köşesinde üç satırlı düğmeyi tıklayarak gezinme menüsünü açın.
# 
# ![Screenshot_26](https://user-images.githubusercontent.com/61363621/79073376-df61a300-7cee-11ea-97fb-506fdf9ae097.png)
# 
# Gezinme menüsü, Google Cloud'un sunduğu tüm bulut ürünlerinin bulunduğu menüyü açar.
# 
# 3. Compute Engine altında, Sanal Makine Örnekleri'ni seçin.
# 
# ![Screenshot_27](https://user-images.githubusercontent.com/61363621/79073415-146df580-7cef-11ea-9518-85cb2262c470.png)
# 
# ![Screenshot_28](https://user-images.githubusercontent.com/61363621/79073446-5139ec80-7cef-11ea-9690-e2b018051421.png)
# 
# 4. Takip ettiğim tutorialda 4. adımda faturalandırmayı etkinleştirmek gerekebileceği bir adım vardı, ancak böyle bir ekran karşıma gelmediği için bu adımı es geçiyoruz.
# 
# 5. Compute Engine hazır olduğunda, TLJH çalıştıracak sunucuyu oluşturmaya başlamak için Oluştur düğmesini tıklayın.
# 
# ![Screenshot_29](https://user-images.githubusercontent.com/61363621/79073531-da512380-7cef-11ea-9aa8-33f4bb6c2757.png)
# 
# 6. Bu adımda Örnek oluşturun başlıklı bir sayfa açıldı. Bu, istediğiniz sunucuyu, sahip olacağı kaynakları ve ne adlandırılacağını özelleştirmemyi sağlar.
# 
# ![Screenshot_30](https://user-images.githubusercontent.com/61363621/79073594-2308dc80-7cf0-11ea-819c-63e82cf19a45.png)
# 
# 7. Ad altında, bu JupyterHub'ın hangi amaçla kullanılacağını tanımlayan unutulmaz bir ad verin.
# 
# 8. Bölge, bu sunucunun barındırılacağı fiziksel konumu belirtmektedir. Genellikle, kullanıcılarınızın çoğunun bulunduğu yere yakın bir bölge seçin. Bazı durumlarda sunucunuzun maliyetini artırabileceğini unutmayın!
# 
# 9. Bölge için seçeneklerden herhangi birini seçin. Varsayılanı olduğu gibi bırakmak iyidir.
# 
# 10. Makine türü altında, sunucunuz için istediğiniz CPU / RAM / GPU miktarını seçin. En az 1GB RAM gerekir.
# Varsayılan temel görünümde önceden ayarlanmış bir kombinasyon seçebilirsiniz. Ben varsayılan kombinasyon ile devam ediyorum.
# 
# ![Screenshot_32](https://user-images.githubusercontent.com/61363621/79073939-14bbc000-7cf2-11ea-8c32-94e8a0b0891a.png)
# 
# 11. Önyükleme Diski altında, Değiştir düğmesine tıklayın. Bu, işletim sistemini ve diskinizin boyutunu değiştirmemizi sağlar.
# 
# ![Screenshot_33](https://user-images.githubusercontent.com/61363621/79073970-4af93f80-7cf2-11ea-81e2-27e43ff21e16.png)
# 
# 12. İşletim sistemi görüntüleri listesinden Ubuntu 18.04 LTS'yi seçin.
# 
# ![Screenshot_34](https://user-images.githubusercontent.com/61363621/79073987-68c6a480-7cf2-11ea-83ba-3d8a7c848d67.png)
# 
# 13. Bu pop-up pencerenin altındaki diskinizin türünü ve boyutunu da değiştirebilirsiniz.
# 
# ![Screenshot_35](https://user-images.githubusercontent.com/61363621/79074002-8c89ea80-7cf2-11ea-9e76-4491ec689f08.png)
# 
# Standart kalıcı disk türü, sabit sürücüye benzer şekilde daha yavaş ancak daha ucuz bir disk sağlar. SSD kalıcı disk, SSD'ye benzer şekilde daha hızlı ancak daha pahalı bir disk sağlar.
# 
# 14. Önyükleme diski açılır penceresini kapatmak için Seç düğmesini tıklayın ve seçiminizi kaydedin.
# 
# 15. Kimlik ve API erişimi altında, Hizmet hesabı alanı için Hizmet hesabı yok'u seçin. Bu, JupyterHub kullanıcılarınızın otomatik olarak diğer bulut hizmetlerine erişmesini önleyerek güvenliği artırır.
# 
# ![Screenshot_37](https://user-images.githubusercontent.com/61363621/79074061-f0acae80-7cf2-11ea-8ad7-b8a66c0b92ae.png)
# 
# 16. Güvenlik Duvarı altında, HTTP Trafiğine İzin Ver ve HTTPS Trafiğine İzin Ver onay kutularını işaretleyin.
# 
# ![Screenshot_38](https://user-images.githubusercontent.com/61363621/79074078-0cb05000-7cf3-11ea-86a7-e3892d4df9e1.png)
# 
# 17. Daha fazla seçeneği görmek için Yönetim, güvenlik, diskler, ağ iletişimi, tek kiracılı bağlantısına tıklayın.
# 
# ![Screenshot_39](https://user-images.githubusercontent.com/61363621/79076644-74bb6200-7d04-11ea-9f71-25f3805d8c7d.png)
# 
# 18. Aşağıdaki metni kopyalayın ve Başlangıç komut dosyası metin kutusuna yapıştırın. <admin-user-name> öğesini bu JupyterHub için ilk yönetici kullanıcının adıyla değiştirin. Bu yönetici kullanıcı JupyterHub kurulduktan sonra oturum açabilir ve gereksinimlere göre güncellenebilir. Kullanıcı adınızı eklemeyi unutmayın!
#     
# > #!/bin/bash
# curl https://raw.githubusercontent.com/jupyterhub/the-littlest-jupyterhub/master/bootstrap/bootstrap.py \
#   | sudo python3 - \
#     --admin <admin-user-name>
#     
# ![photo5807542237079385054](https://user-images.githubusercontent.com/61363621/79076837-b7316e80-7d05-11ea-9ba8-7303e1aa8b64.jpg)
# 
# 19. Sunucunuzu başlatmak için alttaki Oluştur düğmesini tıklayın!
# 
# ![Screenshot_40](https://user-images.githubusercontent.com/61363621/79076899-011a5480-7d06-11ea-9f53-eff8feefbd93.png)
# 
# 20. Oluşturulan sunucumuzu VM örnekleri sayfasına göderiliriz.
# 
# ![Screenshot_42](https://user-images.githubusercontent.com/61363621/79077036-eac0c880-7d06-11ea-9348-035ac27e07f4.png)
# 
# 21. Littlest JupyterHub şimdi yeni sunucunuzda arka planda kuruluyor. Bu kurulumun tamamlanması yaklaşık 5-10 dakika sürer.
