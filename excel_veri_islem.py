import pandas as pd
import os

class omım_ekle:
    def __init__(self, data, omim):
        self.data=data
        self.omim=omim
    @property
    def hasta_adı(self):
        (n,m)=os.path.splitext(self.data)
        return "{}-omim.xlsx".format(n)
    def omim_ekleme(self):
        h=pd.read_excel(self.data)
        o=pd.read_excel(self.omim)
        h['Fenotip']=list
        og=o['Gene']
        of=o['Phenotypes']
        a=zip(og,of)
        dic={x:y for x,y in a}
        i=0
        for gen in h['Ref.Gene']: 
            if gen in dic.keys():
                h.Fenotip.iloc[i]=dic[gen]
            else:
                h.Fenotip.iloc[i]='yok'
            i+=1
        return h.to_excel(self.hasta_adı,sheet_name='Sheet',engine='xlsxwriter')