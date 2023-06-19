# GHOSTSURF 
![GhostsurfLogo](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/logos/ghostsurf_rounded.png)

Ghostsurf is a desktop application which redirects your internet traffic over tor. You can use it to surf on the internet anonymously. Read the following articles to get more information. 

[Wikipedia: Tor Anonimity Network](https://en.wikipedia.org/wiki/Tor_%2anonymity_network%29)

[Tor Project Website](https://www.torproject.org/)

[Transparent Proxy Brief Notes](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TransparentProxy#brief-notes)

<br>

## INSTALLATION
1) Install the dependencies: 	

		sudo apt install tor netfilter-persistent iptables-persistent secure-delete bleachbit macchanger net-tools -y

2) Download the installer

		curl -L https://github.com/dogaegeozden/ghostsurf/releases/download/tor/ghostsurf.deb -o ghostsurf.deb		

3) Start the installer 

		sudo dpkg -i ghostsurf.deb		

4) Open a new terminal and type: 
	
		ghostsurf

<br>

## FEATURES

<table align="center">
    <thead>
    <tr>
      <th align="center"><img width="225" height="0"> <p>Feature name</p></th>
      <th align="center"><img width="225" height="0"> <p>Description</p></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Log killer</td> 
       <td>Destroys the log files in system with the overwrite method</td>
    </tr>
    <tr>
      <td>IP changer</td>
       <td>Hides your real ip address by redirecting all network traffic to tor transparent proxy</td>
    </tr>
    <tr>
      <td>Dns change</td>
       <td>Replaces the default dns servers provided by your isp with privacy based servers</td>
    </tr>
    <tr>
      <td>Mac changer</td>
       <td>Replaces each network interface in the system with a fake mac address</td>
    </tr>
        </tr>
    <tr>
      <td>Anti cold boot</td>
      <td>Avoids ram dump by deleting traces in the system</td>
    </tr>
        </tr>
    <tr>
      <td>Timezone changer</td>
       <td>Sets the time in utc to avoid location leaks from the system clock</td>
    </tr>
        </tr>
    <tr>
      <td>Hostname changer</td>
       <td>Replaces the host name with a random name to hide it</td>
    </tr>
        </tr>
    <tr>
      <td>Browser anonymization</td>
       <td>Configures the browser to be privacy focused</td>
    </tr>
  </tbody>
</table>

<br>

![AppScreenShot](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/app_images/app_sc.png)

## HELP

Ghostsurf is identifying your ip address by sending a get request to https://ifconfig.io. And, if the app sends too many requests in short time that may cause issues and you may not get a proper response.

<br>

---

<br>

# GHOSTSURF 
![GhostsurfLogo](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/logos/ghostsurf_rounded.png)

Ghostsurf cihazın internet trafiğini tor üzerinden yönlendiren bir bilgisayar uygulamasıdır. İnternette kimlğin gizli olarak haraket etmeni sağlar. Daha fazla bilgi için aşağıdaki makaleleri oku.

[Wikipedia: Tor Anonimity Network](https://en.wikipedia.org/wiki/Tor_%2anonymity_network%29)

[Tor Project Website](https://www.torproject.org/)

[Transparent Proxy Brief Notes](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TransparentProxy#brief-notes)

<br>

## YÜKLEME
1) Bağımlılıkları yükle: 	

		sudo apt install tor netfilter-persistent iptables-persistent secure-delete bleachbit macchanger net-tools -y

2) Yükleyiciyi indir

		curl -L https://github.com/dogaegeozden/ghostsurf/releases/download/tor/ghostsurf.deb -o ghostsurf.deb		

3) Yükleyiciyi başlat

		sudo dpkg -i ghostsurf.deb		

4) Terminali aç ve aşağıdaki metni gir: 
	
		ghostsurf

<br>

## ÖZELLİKLER

<table align="center">
    <thead>
    <tr>
      <th align="center"><img width="225" height="0"> <p>Özellik adı</p></th>
      <th align="center"><img width="225" height="0"> <p>Açıklama</p></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Kayıt silici</td> 
       <td>Kayıt dosyalarının uzerine yazarak yok eder</td>
    </tr>
    <tr>
      <td>IP değiştirici</td>
       <td>Bütün internet trafiğini tor transparent proxy üzerinden yönlendirerek gerçek ip adresini saklar</td>
    </tr>
    <tr>
      <td>Dns değiştirici</td>
       <td>İnternet hizmeti sağlayıcın tarafından verilen dns sunucularını gizlilik odaklı olanları ile değiştir</td>
    </tr>
    <tr>
      <td>Mac değiştirici</td>
       <td>Her bir internet adaptörünün mac adresini sahtesi ile değistirir</td>
    </tr>
        </tr>
    <tr>
      <td>Anti soğuk başlatma</td>
      <td>Sistemdeki izleri silerek ram dökümünü önler</td>
    </tr>
        </tr>
    <tr>
      <td>Saat dilimi değiştirici</td>
       <td>Sistem saatinden konum sızıntılarını önlemek için zamanı utc olarak ayarlar</td>
    </tr>
        </tr>
    <tr>
      <td>Hostname değiştirici</td>
       <td>Ana bilgisayar adını gizlemek için rastgele bir adla değiştirir</td>
    </tr>
        </tr>
    <tr>
      <td>Tarayıcı anonimleştirme</td>
       <td>Tarayıcıyı gizlilik odaklı olacak şekilde yapılandırır</td>
    </tr>
  </tbody>
</table>

<br>

![AppScreenShot](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/app_images/app_sc.png)

## YARDIM

Ghostsurf senin genel ip adresini https://ifconfig.io 'ya talep göndererek alıyor. Ve, eğer sen çok fazla talep gönderirsen, düzgün yanıt alamaya bilirsin.