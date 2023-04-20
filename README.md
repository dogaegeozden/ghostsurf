# GHOSTSURF 
![GhostsurfLogo](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/logos/ghostsurf_rounded.png)

Ghostsurf is a desktop application which redirects your internet traffic over tor. You can use it to stay anonymous while you are online. Make sure to read the major flaws section.

## MAJOR FLAWS  
It's redirecting the root user's traffic. You can see this by executing the following command from your terminal -> sudo curl ifconfig.io

## INSTALLATION
1) Install the dependencies: ```apt install tor bleachbit netfilter-persistent iptables-persistent -y```
2) Download the installer ```curl -L https://github.com/dogaegeozden/ghostsurf/releases/download/tor/ghostsurf.deb```
2) Start the installer ```sudo dpkg -i ghostsurf.deb```
3) Open a new terminal and type: ```ghostsurf```

![AppScreenShot](https://raw.githubusercontent.com/dogaegeozden/ghostsurf/main/app_images/app_sc.png)

## HELP

Ghost surf is identifying your ip address by sending a get request to https://ifconfig.io. And if the app sends too many requests it may not a get proper response.