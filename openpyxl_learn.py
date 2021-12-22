from openpyxl import Workbook


wb = Workbook() # 创建一个Excel，默认会创建一个'Sheet'

# 以下二选一
work_sheet = wb.active  # 获取初始的默认sheet
work_sheet = wb.create_sheet(index=0, title='XXXX')

# 写入数据
for entry in datas:
    work_sheet.append(entry)
    
# 保存文件
wb.save(file_name)
