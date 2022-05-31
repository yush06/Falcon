from __future__ import division, unicode_literals 
import codecs
from bs4 import BeautifulSoup
import xlsxwriter
import bs4

#fetch and parse the html file
f=codecs.open("rules.html", 'r', 'utf-8')
soup= BeautifulSoup(f.read(),'html.parser')
workbook = xlsxwriter.Workbook('TenantRuleReport.xlsx')

# create list of SheetName 
sheetName=[]
#Extracting All Tags of h2
for x in soup.find_all('h2'):
    sheetName.append(x.string)


list_id=['crossfeed','frd13','bis21','ldgr21','rbtran21','frd15','nmon20','ais20','cis20','ext10','credit25_authpost','debit25_authpost','pis12','DBDECLINE','BBDECLINE','UPIDECLINE','CAMFAILURE','CAMUSERERR','CAMSUCCESS']
res = {}
for key in sheetName:
    for value in list_id:
        res[key] = value
        list_id.remove(value)
        break  

#create sheets
for x, y in res.items():
    row=1
    col=0

    worksheet = workbook.add_worksheet(x)
    worksheet.write('A1', 'Rule Set')
    worksheet.write('B1', 'Rule Name')
    worksheet.write('C1', 'Description')
    worksheet.write('D1', 'Mode')
    worksheet.write('E1', 'Tracking')
    worksheet.write('F1', 'Content')

    Id_Of_UL=""
    z=soup.find('ul', attrs= {'id': y})
    Id_Of_UL = bs4.BeautifulSoup(str(z), 'html.parser')
    RuleDetails=Id_Of_UL.find_all('li')
    
    for RuleDetail in RuleDetails:
        RuleDetailHtml = bs4.BeautifulSoup(str(RuleDetail), 'html.parser')
        RuleSetName=RuleDetail.find('h3')
        if RuleSetName is not None:
            worksheet.write(row,col, str(RuleSetName.string.split(':')[1]))
        else:
            worksheet.write(row,col, str(''))
        col=col+1

        ruleName = RuleDetailHtml.find('h4')
        ruleInformation = RuleDetailHtml.find_all('td')
        if len(ruleInformation) > 0 :
            worksheet.write(row,col, str(ruleName.string.split(':')[1]))
            col=col+1
            worksheet.write(row,col, str(ruleInformation[0].string))
            col=col+1
            worksheet.write(row,col, str(ruleInformation[1].string))
            col=col+1
            worksheet.write(row,col, str(ruleInformation[2].string))
            col=col+1
            worksheet.write(row,col, str(ruleInformation[3]).replace('<td>','').replace('</td>','').replace('<br/>','\n'))


        col=0
        row=row+1


workbook.close()   
