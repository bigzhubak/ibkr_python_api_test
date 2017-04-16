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

    def tickPrice(self, reqId, tickType, price, attrib):
        super().tickPrice(reqId, tickType, price, attrib)
        print("Tick Price. Ticker Id:", reqId, "tickType:", tickType, "Price:",
              price, "CanAutoExecute:", attrib.canAutoExecute,
              "PastLimit", attrib.pastLimit)

    def tickSnapshotEnd(self, reqId):
        super().tickSnapshotEnd(reqId)
        print("TickSnapshotEnd:", reqId)


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

app.reqMktData(1, contract, "", False, False, [])
app.run()

if __name__ == '__main__':
    pass
