import openpyxl as xl
from openpyxl.chart import Reference,BarChart

wb=xl.load_workbook('transactions.xlsx')
sheet=wb['Sheet1']#case sensitive
for row in range(2,sheet.max_row+1):
    cell=sheet.cell(row,3)
    cell.value=cell.value*0.9
values=Reference(sheet,max_row=sheet.max_row,
                 min_row=2,min_col=3,max_col=3)
chart=BarChart()
chart.add_data(values)
sheet.add_chart(chart,'E2')
wb.save('Modified.xlsx')