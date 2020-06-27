import pandas as pd
def lower_case(value):
    return value.lower()
data=pd.DataFrame([["A",1],
                    ["B",2],
                    ["C",3]],columns=["letter","position"])

new_column=data['letter'].apply(lower_case)
print(new_column)
data['letter']=new_column