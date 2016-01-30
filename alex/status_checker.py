from slackclient import SlackClient
import json
from time import sleep

token = '' #insert token here
sc = SlackClient(token)


def val_predicate(val):
    if val:
        return val != ["[{u'type': u'hello'}]"]
    else:
        return False

while True:
    sc.rtm_connect()
    marker = None
    for i in range(30):
        sleep(1)
        val = "test"
        while val_predicate(val):
            val = sc.rtm_read()
            if val:
                print val
