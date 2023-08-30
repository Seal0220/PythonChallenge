# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client

url = "http://www.pythonchallenge.com/pc/phonebook.php"
with xmlrpc.client.ServerProxy(url) as proxy:
    print(proxy.system.listMethods())
    print(proxy.system.methodHelp('phone')) # Returns the phone of a person
    print(proxy.phone('Bert')) # Bert is Evil -> 555-ITALY