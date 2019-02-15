import pandas as pd
df=pd.DataFrame({'data':[10,20,30,20,15,30,45,]})
writer=pd.ExcelWriter('pandas_chart.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')
workbook=writer.book
worksheet=writer.sheets['Sheet1']
chart=workbook.add_chart({'type':'column'})
chart.add_series({'values':'=Sheet1!$B$2:$B$8'})
worksheet.insert_chart('D2',chart)
writer.save()
