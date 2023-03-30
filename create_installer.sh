#!/usr/bin/bash

# Create the executable file
echo 'Creating the executable file...'
pyinstaller ghostsurf.spec

# Create a directory hierarchy to package your application
echo 'Creating the directory hierarchy...'
mkdir -p package/opt
mkdir -p package/usr/bin

# Copy the application to package/opt
echo 'Copying the executable application into package/opt/...'
cp -r dist/ghostsurf package/opt/

# Create the installer
echo 'Creating the installer...'
fpm -C package -s dir -t deb -n "ghostsurf" -v 0.1.0 -p ghostsurf.deb --after-install post_install_script.sh
