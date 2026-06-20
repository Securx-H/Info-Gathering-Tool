# 🕵️‍♂️ Advanced Information Gathering Tool

A powerful, passive reconnaissance and footprinting tool built with Python. 

## 💡 Why I Built This (My Journey)
I developed this tool as part of my journey in learning **Python for Cybersecurity, VAPT, and Bug Hunting**. Instead of just watching tutorials, I wanted to build something practical to understand how different Python libraries work under the hood. 

My goal is to show other beginners that building your own security tools is one of the best ways to learn programming. By exploring the source code of this tool, you can see how libraries like `requests`, `python-whois`, `dnspython`, and `shodan` are utilized in real-world footprinting. I hope this inspires you to start building your own tools!

---

## ✨ Features
* **WHOIS Lookup:** Extracts domain registration details, registrar, and expiry dates.
* **DNS Enumeration:** Retrieves A, NS, and MX records for the target domain.
* **Geolocation:** Pinpoints the server's physical location (Country, City, State).
* **Tech Stack & CMS Detection:** Identifies web servers, PHP versions, and common CMS platforms (like WordPress, Joomla).
* **IP Reputation (HetrixTools):** Checks if the target IP is listed on any active blacklists.
* **Shodan Integration:** Scans for open ports, operating systems, and organization details.

---

## ⚙️ Prerequisites
* Python 3.x
* Shodan API Key
* HetrixTools API Key

---

## 🚀 Installation

**1. Clone the repository to your local machine:**
```
git clone https://github.com/Securx-H/Info-Gathering-Tool.git
cd Info-Gathering-Tool
2. Install the required libraries:


pip install -r requirements.txt
🛠️ Usage
Step 1: Set up your API keys in your terminal environment before running the tool to keep them secure:


export HETRIX_API_KEY="your_hetrixtools_api_key_here"
export SHODAN_API_KEY="your_shodan_api_key_here"
Step 2: Run the script by providing the target domain and IP:


python3 info_gathering_try.py -d example.com -s 1.2.3.4
📌 Arguments:
-d or --domain : Target domain name (Required)

-s or --shodan : Target IP address for Shodan and Blacklist checks (Optional but recommended)

-o or --output : Save the result to a specified text file (Optional)

⚠️ Disclaimer
This tool is developed for educational purposes and ethical hacking only.
Do not use it against any system, network, or application without explicit,
prior permission from the owner. The developer is not responsible for any misuse or damage caused by this program.
