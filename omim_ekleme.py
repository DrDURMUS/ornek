import pandas as pd
import os


class omım_ekle:
    def __init__(self, data, omim):
        self.data = data
        self.omim = omim

    @property
    def output(self):
        (i, j) = os.path.splitext(self.data)
        return "{}-omim.xlsx".format(i)

    def omim_ekleme(self):
        h = pd.read_csv(self.data, header=0, engine='c', low_memory=False)
        o = pd.read_excel(self.omim)
        h['Fenotip'] = list
        og = o['Gene']
        of = o['Phenotypes']
        a = zip(og, of)
        dic = {x: y for x, y in a}

        def ara(gen):
            if gen in dic.keys():
                return dic[gen]
            else:
                return 'yok'

        h['Fenotip'] = h.apply(lambda x: ara(x['Ref.Gene']), axis=1)

        return h.to_excel(self.output, sheet_name='Sheet', engine='xlsxwriter', na_rep='NaN', index=False), print(
            "Omim fenotipleri tabloya eklendi.")

