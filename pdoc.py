# pip install python-docx
# pip install docxtpl

from docxtpl import DocxTemplate

tpl = DocxTemplate("template.docx")

context2 = {
    "title": "Person 2",
    "company_name": "Dr Pi Ltd",
    "date": "2020-03-03",  
}


tpl.render(context2)

for i in range (5):
    tpl.save("t"+str(i)+".docx")
