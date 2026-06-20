import sys
import whois
import dns.resolver
import shodan
import requests
import argparse
import socket
import os

# --- Color Codes for Professional UI ---
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# --- Professional Banner ---
def print_banner():
    print(CYAN + "="*60)
    print("    ADVANCED INFORMATION GATHERING TOOL v1.0")
    print("   Built for Passive Reconnaissance & Footprinting")
    print("="*60 + RESET + "\n")

argparse = argparse.ArgumentParser(description="Advanced Information Gathering Tool", usage="python3 info_gathering.py -d DOMAIN [-s IP]")
argparse.add_argument("-d","--domain",help="Enter the domain name for footprinting.", required=True)
argparse.add_argument("-s","--shodan",help="Enter the IP for Shodan search.")
argparse.add_argument("-o","--output",help="Enter the file to write output to.")

args = argparse.parse_args()
domain = args.domain
ip = args.shodan
output = args.output

try:
    target_ip = socket.gethostbyname(domain)
except:
    target_ip = None

print_banner()

# ----------------- WHOIS Module -----------------
print(YELLOW + "[+] Getting WHOIS info..." + RESET)
whois_result = ''
try:
    py = whois.whois(domain)
    whois_result += f"[+] Registrar: {py.registrar}\n"
    whois_result += f"[+] Creation Date: {py.creation_date}\n"
    whois_result += f"[+] Expiration Date: {py.expiration_date}\n"
    whois_result += f"[+] Registrant Country: {py.registrant_country}\n"
    print(GREEN + whois_result.strip() + RESET + "\n")
except Exception as e:
    print(RED + f"[-] WHOIS Error: {e}" + RESET + "\n")

# ----------------- DNS Module -----------------
dns_result = ''
print(YELLOW + "[+] Getting DNS info..." + RESET)
try:
    for a in dns.resolver.resolve(domain,'A'):
        dns_result += f"[+] A Record: {a.to_text()}\n" 
    for ns in dns.resolver.resolve(domain,'ns'):
        dns_result += f"[+] NS Record: {ns.to_text()}\n"  
    for mx in dns.resolver.resolve(domain,'mx'):
        dns_result += f"[+] MX Record: {mx.to_text()}\n" 
    print(GREEN + dns_result.strip() + RESET + "\n")
except Exception as e:
    print(RED + "[-] DNS records not found or error occurred." + RESET + "\n")

# ----------------- Geolocation Module -----------------
geo_result = ''
print(YELLOW + "[+] Getting Geolocation info..." + RESET)
if target_ip:
    try:
        response = requests.get(f"https://geolocation-db.com/json/{target_ip}").json()
        geo_result += f"[+] Country: {response.get('country_name', 'N/A')}\n" 
        geo_result += f"[+] City: {response.get('city', 'N/A')}\n"  
        geo_result += f"[+] State: {response.get('state', 'N/A')}\n" 
        print(GREEN + geo_result.strip() + RESET + "\n")
    except Exception as e:
        print(RED + f"[-] Geolocation error: {e}" + RESET + "\n")

# ----------------- Tech Stack & CMS Module -----------------
tech_result = ''
print(YELLOW + "[+] Getting Technology Stack & CMS info..." + RESET)
try:
    url = "http://" + domain
    response = requests.get(url, timeout=10)
    headers = response.headers
    page_content = response.text.lower()

    if 'Server' in headers:
        tech_result += f"[+] Web Server: {headers['Server']}\n"
    if 'X-Powered-By' in headers:
        tech_result += f"[+] Powered By: {headers['X-Powered-By']}\n"

    if "wp-content" in page_content or "wordpress" in page_content:
        tech_result += "[+] CMS: WordPress detected\n"
    elif "joomla" in page_content:
        tech_result += "[+] CMS: Joomla detected\n"
    else:
        tech_result += "[-] CMS: No common CMS detected\n"
    
    print(GREEN + tech_result.strip() + RESET + "\n")
except Exception as e:
    print(RED + f"[-] Technology Stack error: {e}" + RESET + "\n")

# ----------------- HetrixTools Blacklist Check -----------------
blacklist_result = ''
print(YELLOW + "[+] Checking IP Reputation (HetrixTools)..." + RESET)
HETRIX_API_KEY = os.environ.get("HETRIX_API_KEY")

if not HETRIX_API_KEY:
    print(RED + "[-] HETRIX_API_KEY environment variable not found! Skipping Blacklist check." + RESET + "\n")
elif target_ip:
    try:
        # HetrixTools API Request
        url = f"https://api.hetrixtools.com/v2/{HETRIX_API_KEY}/blacklist-check/ipv4/{target_ip}/"
        response = requests.get(url).json()
        
        if response.get('status') == 'SUCCESS':
            blacklisted_count = response.get('blacklisted_count', 0)
            if blacklisted_count > 0:
                blacklist_result += f"[!] WARNING: IP is blacklisted on {blacklisted_count} lists!\n"
                print(RED + blacklist_result.strip() + RESET + "\n")
            else:
                blacklist_result += "[+] IP is CLEAN (Not found in any blacklists).\n"
                print(GREEN + blacklist_result.strip() + RESET + "\n")
        else:
            print(RED + f"[-] Hetrix API Error: {response.get('error_message')}" + RESET + "\n")
    except Exception as e:
         print(RED + f"[-] Blacklist check failed: {e}" + RESET + "\n")

# ----------------- Shodan Module -----------------
if ip:
    print(YELLOW + f"[+] Getting info from Shodan for IP: {ip}" + RESET)
    SHODAN_API_KEY = os.environ.get("SHODAN_API_KEY")
    
    if not SHODAN_API_KEY:
         print(RED + "[-] SHODAN_API_KEY environment variable not found! Skipping Shodan scan." + RESET + "\n")
    else:
        api = shodan.Shodan(SHODAN_API_KEY)
        try:
            host = api.host(ip)
            print(GREEN + f"[+] Organization: {host.get('org', 'n/a')}")
            print(f"[+] Operating System: {host.get('os', 'n/a')}")
            print(f"[+] Open Ports: {host['ports']}" + RESET)
        except Exception as e:
            print(RED + f"[!] Shodan Error: {e}" + RESET + "\n")

# ----------------- Output to File -----------------
if output:
    with open(output, 'w') as file:
        file.write("--- INFO GATHERING REPORT ---\n\n")
        file.write(whois_result + '\n')
        file.write(dns_result + '\n')
        file.write(geo_result + '\n')
        file.write(tech_result + '\n') 
        file.write(blacklist_result + '\n')
    print(CYAN + f"\n[+] Output successfully written to {output}" + RESET)
