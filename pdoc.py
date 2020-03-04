# pip install python-docx
# pip install docxtpl <- Better for making new files from a template
import random
import time
import csv
import pandas as pd
from docxtpl import DocxTemplate

csvfn = "cnw.csv"

def mkw(n):
    tpl = DocxTemplate("template.docx") # In same directory
    df = pd.read_csv(csvfn)
    df_to_doct = df.to_dict()
    print(df)
    x = df.to_dict(orient='records')
    context = x
    
    tpl.render(context[n])
    tpl.save("%s.docx" %str(n))
    
    wait = time.sleep(random.randint(1,2))

# Main #

df2 = len(pd.read_csv(csvfn)) - 1
print (df2)

for i in range(1,df2):
    print("Making file: ",f"{i}," ,"..Please Wait...")
    mkw(i)
print("Done! - Now check your files")

