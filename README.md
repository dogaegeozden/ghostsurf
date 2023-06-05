# GHOSTSURF 
![GhostsurfLogo](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/logos/ghostsurf_rounded.png)

Ghostsurf is a desktop application which redirects your internet traffic over tor. You can use it to surf on the internet anonymously.

## INSTALLATION
1) Install the dependencies: 	

		sudo apt install tor netfilter-persistent iptables-persistent secure-delete bleachbit -y

2) Download the installer

		curl -L https://github.com/dogaegeozden/ghostsurf/releases/download/tor/ghostsurf.deb
		
3) Start the installer 

		sudo dpkg -i ghostsurf.deb
		
4) Open a new terminal and type: 
	
		ghostsurf

![AppScreenShot](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/app_images/app_sc.png)

## HELP

Ghost surf is identifying your ip address by sending a get request to https://ifconfig.io. And, if the app sends too many requests in short time that may cause issues and it may not a get proper response.