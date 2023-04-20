main() {
    # The main function which runs the entire script

    # Calling the declare_variables function.
    declare_variables
    # Calling configure_tor function.
    configure_tor
    # Calling declare_variables function.
    declare_variables
    # Calling set_up_iptables_rules function.
    set_up_iptables_rules
}

configure_tor() {
    # A function which configures tor

    # Starting tor with a the torrc file that just have been created and, storing the logs in a file called tor.log
    tor -f /opt/ghostsurf/tor_configuration_files/torrc.custom > tor.log &
    # Starting the tor service
    systemctl start tor
}

declare_variables() {
    # A function which declares variables
   
    # Getting the tor app's uid 
    tor_uid="$(id -u debian-tor)"
    non_tor="192.168.1.0/24 192.168.0.0/24"
    trans_port="9040"
    dns_port="5353"
}

set_up_iptables_rules() {
    # A function which sets up iptables rules

    # Accept all traffic first to avoid ssh lockdown  via iptables firewall rules #
    iptables -P INPUT ACCEPT
    iptables -P FORWARD ACCEPT
    iptables -P OUTPUT ACCEPT
    
    # Flush All Iptables Chains/Firewall rules
    iptables -F
    
    # Delete all Iptables Chains
    iptables -X
    
    # Flush all counters
    iptables -Z 

    # Flush and delete all nat and mangle
    iptables -t nat -F
    iptables -t nat -X
    iptables -t mangle -F
    iptables -t mangle -X
    iptables -t raw -F
    iptables -t raw -X

    # This is where I left.
    iptables -t nat -A OUTPUT -m owner --uid-owner 0 -j RETURN
    iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports $dns_port

    for net in $non_tor 127.0.0.0/9 127.128.0.0/10; do
        iptables -t nat -A OUTPUT -d $net -j RETURN
    done

    iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports $trans_port

    iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    
    for net in $non_tor 127.0.0.0/8; do
        iptables -A OUTPUT -d $net -j ACCEPT
    done

    iptables -A OUTPUT -m owner --uid-owner 0 -j ACCEPT
    iptables -A OUTPUT -j REJECT
}

# Calling the main function.
main