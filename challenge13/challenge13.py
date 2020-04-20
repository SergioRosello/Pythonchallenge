# Are you just 'browsing' to the address of the xmlrpc folder?
# It looks from the response like you didn't submit an xml
# 'request' document to the url.
# XMLRPC requires that you post a request in the form
# of commands via an xml file.

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy(
    "http://www.pythonchallenge.com/pc/phonebook.php")

print(proxy)
print(proxy.system.listMethods())

phone = proxy.phone("Bert")
print(phone)

