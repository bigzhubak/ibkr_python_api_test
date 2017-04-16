#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
# types
from ibapi.common import *
from ibapi.order_condition import *
from ibapi.contract import *
from ibapi.order import *
from ibapi.order_state import *
from ibapi.execution import Execution
from ibapi.execution import ExecutionFilter
from ibapi.commission_report import CommissionReport
from ibapi.scanner import ScannerSubscription
from ibapi.ticktype import *

from ibapi.account_summary_tags import *


import datetime

class MyWrapper(EWrapper):
    def historicalData(self, reqId: TickerId, date: str, open: float, high: float,
                       low: float, close: float, volume: int, barCount: int,
                       WAP: float, hasGaps: int):
        super().historicalData(reqId, date, open, high, low, close, volume,
                               barCount, WAP, hasGaps)
        print("HistoricalData. ", reqId, " Date:", date, "Open:", open,
              "High:", high, "Low:", low, "Close:", close, "Volume:", volume,
              "Count:", barCount, "WAP:", WAP, "HasGaps:", hasGaps)
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

queryTime = datetime.datetime.today().strftime("%Y%m%d %H:%M:%S")

# String queryTime = DateTime.Now.AddMonths(-6).ToString("yyyyMMdd HH:mm:ss")
app.reqHistoricalData(1, contract, queryTime, "1 M", "1 day", "MIDPOINT", 1, 1, [])

app.run()

if __name__ == '__main__':
    pass
