import dns.resolver
import dns.reversename
import argparse
import ipaddress

def query_record(domain, record_types, timeout=3):
    resolver = dns.resolver.Resolver()
    resolver.timeout = timeout
    resolver.lifetime = timeout

    for record_type in record_types:
        try:
            res = resolver.resolve(domain, record_type)
            print(f"\n[{record_type} records for {domain}]:")
            for answer in res:
                print(answer)
        except dns.resolver.NoAnswer:
            print(f"No {record_type} records found for {domain}")
        except dns.resolver.NXDOMAIN:
            print(f"The domain {domain} does not exist")
            return
        except dns.exception.Timeout:
            print(f"Timeout while querying {domain}")
        except Exception as e:
            print(f"Unexpected error ({record_type}): {e}")

def reverse_lookup(ip, timeout=3):
    try:
        ipaddress.ip_address(ip)  # Ip validation
        resolver = dns.resolver.Resolver()
        resolver.timeout = timeout
        resolver.lifetime = timeout
        
        name = dns.reversename.from_address(ip)
        answer = resolver.resolve(name, "PTR")

        print(f"\n[PTR records for {ip}]:")
        for rdata in answer:
            print(rdata)
    except ValueError:
        print(f"Invalid IP address: {ip}")
    except dns.resolver.NoAnswer:
        print(f"No PTR records found for {ip}")
    except dns.resolver.NXDOMAIN:
        print(f"The IP {ip} has no associated domain name")
    except dns.exception.Timeout:
        print(f"Timeout while querying {ip}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    parser = argparse.ArgumentParser(description="DNS Audit and Resolution Tool")
    parser.add_argument("--version", "-v", action="store_true", help="Show the version of the tool")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Subcommand for querying DNS records
    parser_query = subparsers.add_parser("query", aliases=["q"], help="Query DNS records")
    parser_query.add_argument("domain", type=str, help="Domain to query")
    parser_query.add_argument("--type", type=str, default="A", 
                              help="Type of DNS record(s) to query (comma-separated, e.g., A,AAAA,MX)")
    parser_query.add_argument("--timeout", type=int, default=3, help="Timeout for DNS queries (default: 3s)")

    # Subcommand for reverse lookup
    parser_reverse = subparsers.add_parser("reverse-lookup", aliases=["rl"], help="Perform reverse IP lookup")
    parser_reverse.add_argument("ip", type=str, help="IP address to lookup")
    parser_reverse.add_argument("--timeout", type=int, default=3, help="Timeout for DNS queries (default: 3s)")

    args = parser.parse_args()

    if args.version:
        print("DNS Audit and Resolution Tool version 1.1")
        return

    if args.command in ["query", "q"]:
        record_types = args.type.split(",")  
        query_record(args.domain, record_types, args.timeout)
    elif args.command in ["reverse-lookup", "rl"]:
        reverse_lookup(args.ip, args.timeout)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
