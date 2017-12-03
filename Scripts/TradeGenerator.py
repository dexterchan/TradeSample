from Model.Entity import *
import numpy as np
import time
import uuid
import pandas as pd
from datetime import datetime



class TradeGenerator():
    def __init__(self):
        self.equityList=[]
        self.corpBondList=[]
        self.govBondList=[]
        self.customerList=[]
        self.tradeList=[]

        self.prepareEquity()
        self.prepareCorpBond()
        self.prepareGovBond()
        self.prepareCustList()

        self.stddev=1

        np.random.seed(np.int(time.time()))
        pass

    def biasDecision(self, bias, numOfOption,factor=1):
        if(bias>=0):
            decision=np.random.randint(0,np.int(numOfOption+np.floor(numOfOption*factor)))

            if(decision>=numOfOption):
                decision=bias
        else:
            decision=np.random.randint(0,np.int(numOfOption))

        return decision

    def createTrade(self, custName,sec):
        t = Trade()
        t.tradeId=str(uuid.uuid4())
        t.cust=custName
        t.secid=sec.name
        t.quantity = np.random.randint(1000000,10000000)
        t.price = np.random.randint(90,120)
        t.orgType = sec.type

        return t

    def prepareTradeList(self,numOfTradesPerCust):
        for c in self.customerList:
            govcorpbias = np.random.randint(0,1)
            eqBondbias = np.random.randint(0,1)

            lastGovBond=-1
            lastCorp = -1

            for round in range(0,numOfTradesPerCust):
                choosegovcorp = self.biasDecision(govcorpbias,2,2)
                if(choosegovcorp==0):
                    decision=self.biasDecision(lastGovBond,len(self.govBondList),2)
                    t =self.createTrade(c.name,self.govBondList[decision])
                    lastGovBond = decision
                else:
                    chooseEqBond = self.biasDecision(eqBondbias,2,5)
                    decision=self.biasDecision(lastCorp,len(CompanyNameList),5)
                    if(chooseEqBond ==0):
                        #choose equity
                        t = self.createTrade(c.name, self.equityList[decision])
                    else:
                        t = self.createTrade(c.name,self.corpBondList[decision])
                    lastCorp = decision

                self.tradeList.append(t)

        return self.tradeList


    def prepareCustList(self):
        i=0
        for name in clientName:
            client = Customer()
            client.name=name
            client.id=i
            self.customerList.append(client)
            i=i+1
        pass

    def prepareEquity(self):
        i=0
        for name,type in zip(CompanyNameList,CompanyTypeList):
            s = Security()
            s.id=i
            s.name=name
            s.type=type
            s.secType = SecType.equity
            self.equityList.append(s)
            i=i+1
        pass

    def prepareCorpBond(self):
        i=0
        for name,type in zip(CompanyNameList,CompanyTypeList):
            s = Security()
            s.id=i
            s.name=name
            s.type=type
            s.secType = SecType.corpBond
            self.corpBondList.append(s)
            i=i+1
        pass

    def prepareGovBond(self):
        i=0
        for name in GovNameList:
            s=Security()
            s.id=i
            s.name=name
            s.type="Gov"
            s.secType = SecType.GovBond
            self.govBondList.append(s)
            i=i+1
        pass

    def tradeListConvert2DataFrame(self, tradeList):
        df = pd.DataFrame()
        for t in tradeList:
            tDict = dict(t.__dict__)

            new_df = pd.DataFrame.from_dict([tDict])
            df=df.append(new_df, ignore_index=True)

        return df




