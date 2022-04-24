from deta import Deta
import urllib.request
from getmac import get_mac_address as gma
from datetime import datetime

def get_deta_base(base_name):
    project_key = 'c04flkqb_QoD4z8rN7hBmJqZtUDM2BxCxUBngd2N4'
    deta = Deta(project_key)
    users = deta.Base(base_name)
    return users

def insert_data_higher(email, name, mac):
    deta_base = get_deta_base('usersv4')
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    deta_base.insert({
        'email': email.lower(),
        'name': name,
        'mac_address': mac.lower(),
        'last_opened': now
    })

def insert_data_lower(email, name, password):
    deta_base = get_deta_base('usersv5')
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    deta_base.insert({
        'email': email.lower(),
        'name': name,
        'password': password,
        'last_opened': now
    })

def insert_log_data():
    deta_base = get_deta_base('log-data')
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    mac_address = gma()
    try:
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    except urllib.error.URLError:
        external_ip = '-'
    fetch_res = deta_base.fetch({"mac_address": mac_address.lower()})
    items = fetch_res.items
    deta_base.insert({
        'mac_address': mac_address.lower(),
        'ip_address': external_ip,
        'total_attempts': len(items),
        'last_attempt': now
    })

def is_valid_user_higher(mac_address):
    deta_base = get_deta_base('usersv4')
    fetch_res = deta_base.fetch({"mac_address": mac_address.lower()})
    items = fetch_res.items
    if len(items) > 0:
        return True, items[0]['key']
    else:
        return False, ''

def is_valid_user_lower(email, password):
    deta_base = get_deta_base('usersv5')
    fetch_res = deta_base.fetch({"email": email.lower()})
    items = fetch_res.items
    if len(items) > 0 and items[0]['password'] == password:
        return True, items[0]['key']
    else:
        return False, ''

def update_time(deta_base_name, item_key):
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    deta_base = get_deta_base(deta_base_name)
    deta_base.update({
        "last_opened": now
    }, key=item_key)


if __name__ == '__main__':
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    deta_base = get_deta_base('usersv4')
    print(deta_base)
    mac_address = gma()
    # insert_data_lower(
    #     'mahmudur.rahman99@gmail.com',
    #     'Mahmudur Rahman Shovon',
    #     'hello1234'
    # )
    # try:
    #     external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    # except urllib.error.URLError:
    #     external_ip = '-'
    # deta_base = get_deta_base('usersv4')
    # fetch_res = deta_base.fetch({"mac_address": mac_address})
    # items = fetch_res.items
    # print(items)
    # deta_base.update({
    #     "last_opened": now
    # }, key=items[0]['key'])
    # resp = is_valid_user(deta_base, mac_address, external_ip)
    # print(resp)