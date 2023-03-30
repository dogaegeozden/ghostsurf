main() {
    # The main function which runs the entire script

    # Calling the declare_variables function.
    declare_variables
    # Calling configure_tor function.
    configure_tor
    # Calling backup_iptables_rules function.
    backup_iptables_rules
    # Calling declare_variables function.
    declare_variables
    # Calling set_up_iptables_rules function.
    set_up_iptables_rules
}

configure_tor() {
    # A function which configures tor

    printf "VirtualAddrNetwork 10.192.0.0/10\nAutomapHostsOnResolve 1\nTransPort 9040\nDNSPort 5353" > torrc
    killall tor > /dev/null 2>&1
    tor -f ./torrc > tor.log &
    systemctl start tor
}

backup_iptables_rules() {
    # A function which backs up iptables

    iptables-save > backup
}

declare_variables() {
    # A function which declares variables

    tor_uid=`id -u debian-tor`
    NON_TOR="192.168.1.0/24 192.168.0.0/24"
}

set_up_iptables_rules() {
    # A function which sets up iptables rules

    # Accept all traffic first to avoid ssh lockdown  via iptables firewall rules #
    iptables -P INPUT ACCEPT
    iptables -P FORWARD ACCEPT
    iptables -P OUTPUT ACCEPT
    
    # Flush All Iptables Chains/Firewall rules #
    iptables -F
    
    # Delete all Iptables Chains #
    iptables -X
    
    # Flush all counters too #
    iptables -Z 
    # Flush and delete all nat and  mangle #
    iptables -t nat -F
    iptables -t nat -X
    iptables -t mangle -F
    iptables -t mangle -X
    iptables -t raw -F
    iptables -t raw -X

    iptables -t nat -A OUTPUT -m owner --uid-owner 0 -j RETURN
    iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 5353

    for NET in $NON_TOR 127.0.0.0/9 127.128.0.0/10; do
        iptables -t nat -A OUTPUT -d $NET -j RETURN
    done

    iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports 9040

    iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    
    for NET in $NON_TOR 127.0.0.0/8; do
        iptables -A OUTPUT -d $NET -j ACCEPT
    done

    iptables -A OUTPUT -m owner --uid-owner 0 -j ACCEPT
    iptables -A OUTPUT -j REJECT
}

# Calling the main function.
main