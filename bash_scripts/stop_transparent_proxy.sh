#!/bin/bash

main() {
    # The main function which runs the entire script

    # Calling the declare_variables function.
    declare_variables

    # Calling the drop_timezone_change function.
    drop_timezone_change

    # Calling the enable_ipv6 function.
    enable_ipv6

    # Calling set_iptables_rules_v4and6 function.
    setup_iptables_rules_v4and6

    # Calling stop_tor_service function.
    stop_tor_service    

    # Calling restore_default_configuration_files function.
    restore_default_configuration_files

}

declare_variables() {
    # A function which declares variables

    # Reading the original timezone from the backup
    original_timezone=$(cat /opt/ghostsurf/backup_files/timezone.backup)

    # Creating path which lead to the preferences script of firefox
    pref_path="$(find /home -name prefs.js)"

}

drop_timezone_change() {
    # A function which changes the timezone

    # Restoring the timezone
    timedatectl set-timezone $original_timezone

}

enable_ipv6() {
    # A function which enables ipv6 connections

    sysctl -w net.ipv6.conf.all.disable_ipv6=0 >/dev/null 2>&1
    sysctl -w net.ipv6.conf.default.disable_ipv6=0 >/dev/null 2>&1

}

setup_iptables_rules_v4and6 () {
    # A function which restores iptables policies

    # Clearing the previous rules
    iptables -t filter -F
    iptables -t filter -X
    iptables -t nat -F
    iptables -t nat -X
    ip6tables -t filter -F
    ip6tables -t filter -X
    ip6tables -t nat -F
    ip6tables -t nat -X

    # Default Drop: Drop all packages coming into, coming into the server but that are routed to somewhere else and coming out of the server. So, the packages can be accepted, sended or, routed only in the ways that you stated.
    # INPUT Chain: Network packages coming into the server.
    # FORWARD Chain: Network packages coming into the server that are routed to somewhere else.
    # OUTPUT Chain: Network packages coming out to Linux server.
    iptables -P INPUT DROP
    iptables -P FORWARD DROP
    iptables -P OUTPUT DROP
    ip6tables -P INPUT DROP
    ip6tables -P FORWARD DROP
    ip6tables -P OUTPUT DROP

    # Loopback: The loopback device is a special, virtualnetwork interface that your computer uses to communicate with itself. It is used mainly for diagnostics and troubleshooting, and to connect to servers running on the local machine. · The Purpose of Loopback · When a network interface is disconnected--for example, when an Ethernet port is unplugged or Wi-Fi is turned off or not associated with an access point--no communication on that interface is possible, not even communication between your computer and itself. The loopback interface does not represent any actual hardware, but exists so applications running on your computer can always connect to servers on the same machine. · This is important for troubleshooting (it can be compared to looking in a mirror). The loopback device is sometimes explained as purely a diagnostic tool. But it is also helpful when a server offering a resource you need is running on your own machine.
    # You need the allow the communications with this interface to be able use your computer to communicate with services.
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A OUTPUT -o lo -j ACCEPT
    ip6tables -A INPUT -i lo -j ACCEPT
    ip6tables -A OUTPUT -o lo -j ACCEPT

    # HTTP: Hypertext Transfer Protocol -> The purpose of the HTTP protocol is to provide a standard way for web browsers and servers to talk to each other.
    # These policies are required if you want to be able to connect to internet using http and https protocols. These are the most common ones and the standard way for web browsers and servers to talk to each other.
    iptables -A INPUT -p tcp -m conntrack --ctstate ESTABLISHED,RELATED --sport 80 -j ACCEPT
    iptables -A OUTPUT -p tcp -m tcp --dport 80 -j ACCEPT
    ip6tables -A INPUT -p tcp -m conntrack --ctstate ESTABLISHED,RELATED --sport 80 -j ACCEPT
    ip6tables -A OUTPUT -p tcp -m tcp --dport 80 -j ACCEPT

    # HTTPS: Hypertext Transfer Protocol Secure -> The purpose of the HTTP protocol is to provide a standard way for web browsers and servers to talk to each other with a extensive security that prevents man in the middle and etc.
    iptables -A INPUT -p tcp -m conntrack --ctstate ESTABLISHED,RELATED --sport 443 -j ACCEPT
    iptables -A OUTPUT -p tcp -m tcp --dport 443 -j ACCEPT
    ip6tables -A INPUT -p tcp -m conntrack --ctstate ESTABLISHED,RELATED --sport 443 -j ACCEPT
    ip6tables -A OUTPUT -p tcp -m tcp --dport 443 -j ACCEPT

    # DNS: Domain Name System -> The purpose of DNS is to translate a domain name into the appropriate IP address.
    # Note: You should allow incoming and out going communications to this port if you want to use URLs instead of ipaddresses. Ex-URL: www.google.com 
    iptables -A INPUT -p udp --sport 53 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    iptables -A OUTPUT -p udp --dport 53 -m udp -j ACCEPT
    ip6tables -A INPUT -p udp --sport 53 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    ip6tables -A OUTPUT -p udp --dport 53 -m udp -j ACCEPT

    # Saving the iptables rules
    iptables-save > /etc/iptables/rules.v4
    ip6tables-save > /etc/iptables/rules.v6

}

stop_tor_service() {
    # A function which stops tor service

    # Stopping the tor service
    systemctl stop tor

}

restore_default_configuration_files() {
    # A function which restores the default configuration files. Hint: Ghostsurf defaults baby!!. Reset if you don't like them.

    # Restoring the torrc file
    cp /opt/ghostsurf/backup_files/torrc.backup /etc/tor/torrc

    # Changing the dns configurations
    cp /opt/ghostsurf/configuration_files/dns_changer.resolv.conf /etc/resolv.conf

    # Reloading systemd daemons
    systemctl --system daemon-reload

}

# Calling the main function.
main
