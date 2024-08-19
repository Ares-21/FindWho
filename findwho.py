import socket
import re
import requests
from colorama import Fore, Style, init

# Initialize colorama
init()

def is_ip_address(input_str):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return ip_pattern.match(input_str)

def dns_reverse_dns_lookup():
    print(Fore.CYAN + Style.BRIGHT + r"""
  ┏┓•   ┓     ┓   
  ┣ ┓┏┓┏┫  ┓┏┏┣┓┏┓
  ┻ ┗┛┗┗┻  ┗┻┛┛┗┗┛                                                           
""")
    while True:
        print(Fore.YELLOW + "\nFind Who!! A DNS and Reverse DNS Lookup Tool")
        print(Fore.GREEN + "Enter a domain, website, or IP address (or type 'exit' to quit): ", end='')
        user_input = input()

        if user_input.lower() == 'exit':
            print(Fore.RED + "Exiting the tool." + Style.RESET_ALL)
            break

        if is_ip_address(user_input):
            try:
                domain = socket.gethostbyaddr(user_input)
                print(Fore.CYAN + f"\nReverse DNS Lookup for {user_input}:")
                print(Fore.MAGENTA + f"Domain: {domain[0]}")
                
                try:
                    response = requests.get(f"http://{domain[0]}")
                    if response.status_code == 200:
                        print(Fore.GREEN + f"Website linked to {user_input}: {response.url}")
                    else:
                        print(Fore.RED + f"No website could be retrieved for domain {domain[0]}.")
                except requests.RequestException as e:
                    print(Fore.RED + f"Error fetching website linked to {user_input}: {e}")

            except socket.herror:
                print(Fore.RED + f"Error: Could not resolve IP address {user_input}. No PTR record found.")
        else:
            try:
                ip = socket.gethostbyname(user_input)
                print(Fore.CYAN + f"\nDNS Lookup for {user_input}:")
                print(Fore.MAGENTA + f"IP Address: {ip}")
            except socket.gaierror:
                print(Fore.RED + f"Error: Could not resolve domain {user_input}")

        print(Style.RESET_ALL)

if __name__ == "__main__":
    dns_reverse_dns_lookup()
