class solution5:
    def gasstation(self,gas,cost):
        gas=[1,2,3,4,5]
        cost=[3,4,5,1,2]
        station={}
        while(gas!=0):
            for i in range(gas):
                if gas[i]>cost:
                    gas[i],cost=cost,gas[i]
                    gas++
                    cost-1
                else:
                    return -1
