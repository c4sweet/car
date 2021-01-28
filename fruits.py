import xlsxwriter
import pandas as pd

dataframe = pd.DataFrame({'Data' : [20,30,45,12,33,9]})

writer = pd.ExcelWriter('simple_data.xlsx', engine='xlswriter')

dataframe.to_excel(writer,sheet_name='หน้าที่1')

writer.save()

11