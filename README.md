# 🕵️‍♂️ Advanced Information Gathering Tool

A powerful, passive reconnaissance and footprinting tool built with Python. Designed for Bug Bounty Hunters, Security Researchers, and Penetration Testers to gather essential intelligence about a target domain without raising alarms.

## ✨ Features

* **WHOIS Lookup:** Extracts domain registration details, registrar, and expiry dates.
* **DNS Enumeration:** Retrieves A, NS, and MX records for the target domain.
* **Geolocation:** Pinpoints the server's physical location (Country, City, State).
* **Tech Stack & CMS Detection:** Identifies web servers, PHP versions, and common CMS platforms (like WordPress, Joomla).
* **IP Reputation (HetrixTools):** Checks if the target IP is listed on any active blacklists.
* **Shodan Integration:** Scans for open ports, operating systems, and organization details.

## ⚙️ Prerequisites

* Python 3.x
* Shodan API Key
* HetrixTools API Key

## 🚀 Installation

1. Clone the repository to your local machine:
```bash
git clone [https://github.com/Securx-H/Info-Gathering-Tool.git](https://github.com/Securx-H/Info-Gathering-Tool.git)
cd Info-Gathering-Tool
Install the required dependencies:

Bash
pip install -r requirements.txt
🛠️ Usage
Set up your API keys in your terminal environment before running the tool to keep them secure:

Bash
export HETRIX_API_KEY="your_hetrixtools_api_key_here"
export SHODAN_API_KEY="your_shodan_api_key_here"
Run the script by providing the target domain and IP:

Bash
python3 info_gathering_try.py -d example.com -s 1.2.3.4
Arguments:
-d or --domain : Target domain name (Required)

-s or --shodan : Target IP address for Shodan and Blacklist checks (Optional but recommended)

-o or --output : Save the result to a specified text file (Optional)

⚠️ Disclaimer
This tool is developed for educational purposes and ethical hacking only. Do not use it against any system, network, or application without explicit, prior permission from the owner. The developer is not responsible for any misuse or damage caused by this program.
