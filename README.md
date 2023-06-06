# GHOSTSURF 
![GhostsurfLogo](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/logos/ghostsurf_rounded.png)

Ghostsurf is a desktop application which redirects your internet traffic over tor. You can use it to surf on the internet anonymously. Read the following articles to get more information. 

[Wikipedia: Tor Anonimity Network](https://en.wikipedia.org/wiki/Tor_%2anonymity_network%29)

[Tor Project Website](https://www.torproject.org/)

[Transparent Proxy Brief Notes](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TransparentProxy#brief-notes)

## INSTALLATION
1) Install the dependencies: 	

		sudo apt install tor netfilter-persistent iptables-persistent secure-delete bleachbit -y

2) Download the installer

		curl -L https://github.com/dogaegeozden/ghostsurf/releases/download/tor/ghostsurf.deb -o ghostsurf.deb
		
3) Start the installer 

		sudo dpkg -i ghostsurf.deb
		
4) Open a new terminal and type: 
	
		ghostsurf

![AppScreenShot](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/app_images/app_sc.png)

## HELP

Ghostsurf is identifying your ip address by sending a get request to https://ifconfig.io. And, if the app sends too many requests in short time that may cause issues and you may not get a proper response.

---
---

# GHOSTSURF 
![GhostsurfLogo](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/logos/ghostsurf_rounded.png)

Ghostsurf cihazın internet trafiğini tor üzerinden yönlendiren bir bilgisayar uygulamasıdır. İnternette kimlğin gizli olarak haraket etmeni sağlar. Daha fazla bilgi için aşağıdaki makaleleri oku.

[Wikipedia: Tor Anonimity Network](https://en.wikipedia.org/wiki/Tor_%2anonymity_network%29)

[Tor Project Website](https://www.torproject.org/)

[Transparent Proxy Brief Notes](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TransparentProxy#brief-notes)


## YÜKLEME
1) Bağımlılıkları yükle: 	

		sudo apt install tor netfilter-persistent iptables-persistent secure-delete bleachbit -y

2) Yükleyiciyi indir

		curl -L https://github.com/dogaegeozden/ghostsurf/releases/download/tor/ghostsurf.deb
		
3) Yükleyiciyi başlat

		sudo dpkg -i ghostsurf.deb
		
4) Terminali aç ve aşağıdaki metni gir: 
	
		ghostsurf

![AppScreenShot](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/app_images/app_sc.png)

## YARDIM

Ghostsurf senin genel ip adresini https://ifconfig.io 'ya talep göndererek alıyor. Ve, eğer sen çok fazla talep gönderirsen, düzgün yanıt alamaya bilirsin.