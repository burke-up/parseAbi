from eth_utils import event_abi_to_log_topic, function_abi_to_4byte_selector
import json
from modules import scanapi

def abi_to_selector(abi):
    if abi['type'] == 'event':
        selector = '0x' + event_abi_to_log_topic(abi).hex()
    else:
        selector = '0x' + function_abi_to_4byte_selector(abi).hex()
    return selector

def abi_to_selectors(info):
    result = []
    for item in info:
        if not "name" in item or item["name"] == None or item["name"] == "":
            continue
        selector = abi_to_selector(item)
        result.append({"selector":selector,"abi":item})
    return result

def fetch_abi_info(address):
    info = scanapi.read_abi_from_address(address)
    if len(info) == 0:
        return {} 
    return abi_to_selectors(info)
