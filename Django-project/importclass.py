import pandas as pd
from userprofile.models import HTML

def import_excel_to_db(file_path):
    # 讀取 Excel 文件
    df = pd.read_excel(file_path)

    # 逐行寫入資料庫
    for _, row in df.iterrows():
        HTML.objects.create(
            class_id=row['class_id'],
            class_name=row['class_name'],       # 根據 Excel 的欄位名稱
            class_content=row['class_content'],    # 根據 Excel 的欄位名稱
            html_code=row['html_code']    # 根據 Excel 的欄位名稱
        )

    print("資料匯入成功！")

file_path = 'userprofile/HTML.xlsx'
import_excel_to_db(file_path)
