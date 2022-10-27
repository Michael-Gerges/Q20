# https://github.com/dappbeast/20q 

import numpy as np
import pandas as pd 

df = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), r"data\big.csv"))

def elimenate_based_on_a_user_answer():
    lst = []
    for question in df.columns[1:]:
        lst.append(abs((len(df)//2 ) - sum(df[question])))
    lst = np.array(lst)
    the_most_info_laden_q = df.columns[np.argmin(lst) +1] 
    print(the_most_info_laden_q)
    user_answer = int(input('Answer? (1/0) '))
    cont =  df[ df[the_most_info_laden_q] != user_answer ].index
    df.drop(cont, inplace = True)   
    #print("possibilities now are: ",list(df[df.columns[0]]))

while len(df)>1:
    try:
        elimenate_based_on_a_user_answer()
    except:
        print("liar liar pants on fire")
        quit()
