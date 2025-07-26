import requests
from openpyxl import Workbook


url = "https://my-tcas.s3.ap-southeast-1.amazonaws.com/mytcas/courses.json?ts=19817575305"

response = requests.get(url)
print("Status Code:", response.status_code)

if response.status_code == 200:
    datas = response.json()

    keys = set()
    for item in datas:
        keys.update(item.keys())
    keys = list(keys)

    wb = Workbook()
    ws = wb.active
    ws.append(keys)  # Write header

    for item in datas:
        row = [item.get(k, "") for k in keys]
        ws.append(row)

    wb.save("courses.xlsx")
    print("Data saved to courses.xlsx")
else:
    print("ไม่สามารถดึงข้อมูลได้")