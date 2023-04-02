main() {
    # The main function which runs the entire script

    # Calling clear_iptables_rules function.
    clear_iptables_rules
    # Calling default_drop function.
    default_drop
    # Calling allow_input_and_output_on_loopback_interface function.
    allow_input_and_output_on_loopback_interface
    # Calling set_iptables_rules_v4and6 function.
    set_iptables_rules_v4and6
    # Calling stop_tor_service function.
    stop_tor_service    
    # Calling delete_the_unneccesary_files function.
    delete_the_unneccesary_files
}

clear_iptables_rules() {
    # A function which clears the iptables rules

    iptables -t filter -F
    iptables -t filter -X
    iptables -t nat -F
    iptables -t nat -X
}

default_drop () {
    # A function which drops all the connections on all chains

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
}

allow_input_and_output_on_loopback_interface() {
    # A function which allows, packages to come in and go out of the interface.

    # Loopback: The loopback device is a special, virtualnetwork interface that your computer uses to communicate with itself. It is used mainly for diagnostics and troubleshooting, and to connect to servers running on the local machine. · The Purpose of Loopback · When a network interface is disconnected--for example, when an Ethernet port is unplugged or Wi-Fi is turned off or not associated with an access point--no communication on that interface is possible, not even communication between your computer and itself. The loopback interface does not represent any actual hardware, but exists so applications running on your computer can always connect to servers on the same machine. · This is important for troubleshooting (it can be compared to looking in a mirror). The loopback device is sometimes explained as purely a diagnostic tool. But it is also helpful when a server offering a resource you need is running on your own machine.
    # You need the allow the communications with this interface to be able use your computer to communicate with services.
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A OUTPUT -o lo -j ACCEPT
    ip6tables -A INPUT -i lo -j ACCEPT
    ip6tables -A OUTPUT -o lo -j ACCEPT
}

set_iptables_rules_v4and6 () {
    # A function which restores iptables policies

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
    # Note: You should allow incoming and out going communications to this port if you want to use URLs instead of ipaddresses. ExURL: https://dogaege.pythonanywhere.com
    iptables -A INPUT -p udp --sport 53 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    iptables -A OUTPUT -p udp --dport 53 -m udp -j ACCEPT
    ip6tables -A INPUT -p udp --sport 53 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    ip6tables -A OUTPUT -p udp --dport 53 -m udp -j ACCEPT
    
    # SSH: The Secure Shell Protocol (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network. Its most notable applications are remote login and command-line execution.
    # Puting input -> Packages coming into the destionation port(Destination Port: It is the other machine's port, thats why you are only allowing when the state is either new or established. Because your security is what matters most for you, not the other's.)
    iptables -A INPUT -p tcp -m conntrack --ctstate NEW,ESTABLISHED --dport 22 -j ACCEPT
    iptables -A OUTPUT -p tcp -m conntrack --ctstate ESTABLISHED --sport 22 -j ACCEPT
    ip6tables -A INPUT -p tcp -m conntrack --ctstate NEW,ESTABLISHED --dport 22 -j ACCEPT
    ip6tables -A OUTPUT -p tcp -m conntrack --ctstate ESTABLISHED --sport 22 -j ACCEPT
    # Geting output -> Packages coming into  the source port(Source Port: It is your machine's port, that's why you are only allowing when the state is established. Becase your security is what matters most for you.)
    iptables -A OUTPUT -p tcp -m conntrack --ctstate NEW,ESTABLISHED --dport 22 -j ACCEPT
    iptables -A INPUT -p tcp -m conntrack --ctstate ESTABLISHED --sport 22 -j ACCEPT
    ip6tables -A OUTPUT -p tcp -m conntrack --ctstate NEW,ESTABLISHED --dport 22 -j ACCEPT
    ip6tables -A INPUT -p tcp -m conntrack --ctstate ESTABLISHED --sport 22 -j ACCEPT

    # Saving the iptables rules
    iptables-save > /etc/iptables/rules.v4
    ip6tables-save > /etc/iptables/rules.v6
}

stop_tor_service() {
    # A function which stops tor service
    
    systemctl stop tor
}

delete_the_unneccesary_files() {
    # A function which deletes unneccesary files

    rm tor.log
}

# Calling the main function.
main