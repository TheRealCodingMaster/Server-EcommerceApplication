import ipaddress
import logging

class NGFW:
    def __init__(self):
        # Initialize the firewall rules
        self.allowed_ips = set()
        self.blocked_ips = set()
        logging.basicConfig(level=logging.INFO)

    def allow_ip(self, ip):
        # Allow an IP address
        try:
            ip_addr = ipaddress.ip_address(ip)
            self.allowed_ips.add(ip_addr)
            logging.info(f"IP address {ip} allowed.")
        except ValueError:
            logging.error(f"Invalid IP address: {ip}")

    def block_ip(self, ip):
        # Block an IP address
        try:
            ip_addr = ipaddress.ip_address(ip)
            self.blocked_ips.add(ip_addr)
            logging.info(f"IP address {ip} blocked.")
        except ValueError:
            logging.error(f"Invalid IP address: {ip}")

    def is_allowed(self, ip):
        # Check if an IP address is allowed
        try:
            ip_addr = ipaddress.ip_address(ip)
            if ip_addr in self.allowed_ips:
                return True
            if ip_addr in self.blocked_ips:
                return False
            return True  # Default to allow if not explicitly blocked
        except ValueError:
            logging.error(f"Invalid IP address: {ip}")
            return False

# Example usage:
if __name__ == '__main__':
    ngfw = NGFW()
    ngfw.allow_ip('192.168.1.1')
    ngfw.block_ip('192.168.1.2')
    
    test_ip = '192.168.1.1'
    if ngfw.is_allowed(test_ip):
        logging.info(f"IP address {test_ip} is allowed.")
    else:
        logging.info(f"IP address {test_ip} is blocked.")
