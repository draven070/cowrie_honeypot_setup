# Cowrie SSH Honeypot with Discord Alert and VirusTotal Integration

This project documents the setup of an SSH honeypot using [Cowrie](https://github.com/cowrie/cowrie) to capture malicious login attempts and command executions in a fake environment.

# Features

- SSH honeypot using Cowrie
- Logs attacker IPs, credentials, and executed commands
- **Real-time alerts to Discord via Webhooks**
- **VirusTotal integration**: Automatically scans files downloaded by attackers

# Files Included in this project

- `cowrie.cfg`: Example Cowrie config
- `discord_server`:Create your own webhook in your server to get the api key

# Requirements

- Linux (tested on Parrot OS / Kali)
- Python 3
- Cowrie
- Discord webhook URL
- VirusTotal API key

# Setup Summary

1. clone Cowrie and install dependencies (use virtual environment)
2. configure `cowrie.cfg` with `[output_discord]` and `[output_virustotal]`
3. you can add your own custom alerts if you have any
4. data can be visualized using different tool as i used streamlit
5. run honeypot using systemd or using bin/cowrie start if you have created a different virtual environment

# Author

- [Bijay Dahal](https://www.linkedin.com/in/bijay-dahal-226286334/)
- Cybersecurity Enthusiast | Honeypot | Cowrie
