#!/bin/bash

main() {
    # The function which runs the entire script

    # Getting the reguler user's username
    username=${SUDO_USER:-${USER}}
    # Changing the file ownerships recursively
    chown -R $username:$username /opt/ghostsurf/
    # Backing up the original torrc file
    sudo cp /etc/tor/torrc /etc/tor/torrc.original
}

# Calling the main function
main
