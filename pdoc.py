# pip install python-docx
# pip install docxtpl <- Better for making new files from a template

import random
import time

from docxtpl import DocxTemplate

def mkw(n):
    tpl = DocxTemplate("template.docx") # In same directory
    context = {1:{"title":"Alfie","company_name":"Dr Pi Red","date": "2020-03-03"},
               2:{"title":"Derek","company_name":"Dr Pi Blue","date": "2020-03-03"},
               3:{"title":"Norman","company_name":"Dr Pi Blue","date": "2020-03-03"},
               4:{"title":"Clive","company_name":"Dr Pi Green","date": "2020-03-03"}
               }  
    tpl.render(context[n])
    tpl.save("%s.docx" %str(n))
    wait = time.sleep(random.randint(1,2))

# Main #

for i in range(1,5):
    print("Making file: ",f"{i}," ,"..Please Wait...")
    mkw(i)
print("Done! - Now check your files")

