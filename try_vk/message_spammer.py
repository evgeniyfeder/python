import age_predict
import xlrd

rb = xlrd.open_workbook("group.xls", formatting_info=True)
sheet = rb.sheet_by_index(0)

for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)

    if row[4] == '*':
        q = age_predict.send_query('messages.send', {"user_id" : str(int(row[5])), "message" : "Проверка"})

