#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class MyWrapper(EWrapper):

    def contractDetails(self, reqId, contractDetails):
        super().contractDetails(reqId, contractDetails)

        print("ContractDetails. ReqId:", reqId,
              contractDetails.summary.symbol,
              contractDetails.summary.secType,
              "ConId:", contractDetails.summary.conId,
              "@", contractDetails.summary.exchange)

    def contractDetailsEnd(self, reqId):
        super().contractDetailsEnd(reqId)
        print("ContractDetailsEnd. ", reqId, "\n")


wrapper = MyWrapper()
app = EClient(wrapper)
app.connect("127.0.0.1", 7497, clientId=0)
print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))


from ibapi.contract import Contract
contract = Contract()
contract.symbol = "XAUUSD"
contract.secType = "CMDTY"
contract.exchange = "SMART"
contract.currency = "USD"

app.reqContractDetails(4444, contract)
app.run()

if __name__ == '__main__':
    pass
