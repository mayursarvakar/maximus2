import pandas as pd
import json
import ast

class sub_id():
    def sub_id_func(self,Data):

        lA=[]
        for i in Data.columns:
            # print(i)
            l="{'label': '"+str(i) +"'," +  "'value':" +"'"+str(i)  + "'},"
            # # 'label': 'Actionable query', 'value': 'Actionable query'}
            #
            lA.append(l)



        lA=''.join(lA)
        sub_list = list(ast.literal_eval(lA))

        return sub_list


sdf=pd.read_csv('tample.csv')
print(sdf.columns)
sdf.drop(['Unnamed: 0'],inplace=True,axis=1)
ab=sub_id().sub_id_func(sdf)
print(ab)





