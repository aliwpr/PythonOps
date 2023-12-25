# after install certbot on server 
import subprocess
import os

def renewSslCertificate(domains, email, webrootPath):
    """
    parameters:
    - domains: list of domains
    - email: email for lets encrypt
    - webrootPath:
    """
    certbotCommand = [
        "certbot",
        "renew",
        "--non-interactive",
        "--agree-tos",
        "--email",
        email,
        "--webroot",
        "--webroot-path",
        webrootPath,
        *["-d", domain for domain in domains]
    ]

    subprocess.run(certbotCommand)
# example
if __name__ == "__main__":
    domainsToRenew = ["ali.com", "www.ali.com"]
    letsEncryptEmail = "ali@yahoo.com"
    certbotWebrootPath = "/var/www/html"

    renewSslCertificate(domainsToRenew, letsEncryptEmail, certbotWebrootPath)
