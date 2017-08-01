from datetime import datetime
import argparse
import sys

from whois import whois
import requests


def load_urls(urls_file):
    urls_with_newline_breaks = urls_file.readlines()
    urls = [url.strip() for url in urls_with_newline_breaks]
    return urls


def is_server_respond_with_200(url):
    try:
        return requests.head(url, allow_redirects=True).ok
    except requests.exceptions.ConnectionError:
        return False


def is_domain_registered(domain_name):
    whois_info = whois(domain_name)
    return whois_info.expiration_date is not None


def is_domain_expiring_soon(domain_name):
    max_allowed_difference_in_days = 31
    whois_info = whois(domain_name)
    difference_in_days = (whois_info.expiration_date[0] - datetime.today()).days
    return difference_in_days < max_allowed_difference_in_days


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--url_file', '-u', type=argparse.FileType('r'), default=sys.stdin)
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    urls = load_urls(args.url_file)
    for url in urls:
        if not is_domain_registered(url):
            print('(-) {} domain is not registered'.format(url))
            continue
        if not is_server_respond_with_200(url):
            print('(!) {} appears to be unresponsive'.format(url))
        if is_domain_expiring_soon(url):
            print('(*) {} domain expires soon'.format(url))
