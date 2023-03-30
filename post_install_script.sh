#!/bin/bash

main() {
    # The function which runs the entire script

    username=${SUDO_USER:-${USER}}
    chown -R $username:$username /opt/ghostsurf/
    chown $username:$username /usr/bin/ghostsurf

}

# Calling the main function
main
