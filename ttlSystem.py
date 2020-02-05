#!/usr/bin/python3

import subprocess
import re
import sys


def return_ttl_number(address):
    try:
        proc = subprocess.Popen(
            ["ping {} -c 1".format(address), ""], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        out = out.decode("utf-8").split()
        out[13] = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", out[12])
        return float(out[13][0])
    except Exception:
        pass


def return_ttl_os_name(ttl_number):
    ttl = ttl_number
    if ttl:
        if ttl >= 0 and ttl <= 64:
            return ('linux-ttl={}'.format(ttl))
        elif ttl >= 65 and ttl <= 128:
            return('Windows-ttl={}'.format(ttl))
        elif ttl >= 129 and ttl <= 254:
            return ('Solaris/AIX-ttl={}'.format(ttl))
        else:
            return ('unknown={}'.format(ttl))
    else:
        pass


if len(sys.argv) != 2:
    print("\n[*] Uso: {} <ip-address>\n".format(sys.argv[0]))
    sys.exit(1)

addr = sys.argv[1]
ttl = return_ttl_number(addr)

print('\n{} -> {}'.format((addr, return_ttl_os_name(ttl))))
