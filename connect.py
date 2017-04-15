#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

app = EClient(EWrapper())
app.connect("127.0.0.1", 7497, clientId=0)
print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
if __name__ == '__main__':
    pass
