# pip install python-docx
# pip install docxtpl

import time
from docxtpl import DocxTemplate

def mkw(n):
    tpl = DocxTemplate("template.docx")
    context = {1:{"title": "moo1", "company_name": "Dr Pi Red", "date": "2020-03-03"},
                 2:{"title": "moo2", "company_name": "Dr Pi Blue", "date": "2020-03-03"},
                   3:{"title": "moo3", "company_name": "Dr Pi Grey", "date": "2020-03-03"}

               }
    
    tpl.render(context[n])
    tpl.save("%s.docx" %str(n))

for i in range(1,4):
    mkw(i)
    
# https://stackoverflow.com/questions/39233973/get-all-keys-of-a-nested-dictionary
