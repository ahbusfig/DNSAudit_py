# DNSAudit_py

# DNS Audit and Resolution Tool

A powerful tool for querying DNS records and performing reverse IP lookups. Supports multiple record types such as A, AAAA, MX, NS, TXT, and PTR, with customizable timeout settings.

## Features

- Query various DNS record types (A, AAAA, MX, NS, TXT, CNAME, etc.)
- Perform reverse IP lookups to retrieve PTR records
- Set custom timeout values for DNS queries
- Simple command-line interface using `argparse`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DNSAudit.git
   ```

2. Install dependencies:
   ```bash
   pip install dnspython
   ```

## Usage

### Query DNS Records
To query DNS records for a domain:
```bash
python dns_audit.py query <domain> --type <record_types> --timeout <timeout>
```
- Replace `<domain>` with the domain you want to query.
- Replace `<record_types>` with the desired record types, separated by commas (e.g., A, AAAA, MX).
- The `--timeout` parameter is optional and defaults to 3 seconds.

### Reverse IP Lookup
To perform a reverse lookup for an IP address:
```bash
python dns_audit.py reverse-lookup <ip> --timeout <timeout>
```
- Replace `<ip>` with the IP address you want to reverse lookup.
- The `--timeout` parameter is optional and defaults to 3 seconds.

## Example

- Querying multiple DNS records for a domain:
   ```bash
   python dns_audit.py query example.com --type A,MX,TXT --timeout 5
   ```

- Performing reverse IP lookup:
   ```bash
   python dns_audit.py reverse-lookup 8.8.8.8 --timeout 3
   ```
