# URL: https://www.geeksforgeeks.org/python/how-to-get-geolocation-in-python/
# importing geopy library
from geopy.geocoders import Nominatim
import pandas as pd
import time

data = pd.read_excel("data/filtered_ai_com_courses.xlsx")

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# สร้างคอลัมน์ใหม่ถ้ายังไม่มี
if 'latitude' not in data.columns:
    data['latitude'] = None
if 'longitude' not in data.columns:
    data['longitude'] = None

# วิธีที่ 1: ใช้ loop แบบเดิมแต่แก้ไขปัญหา
print("กำลังดึงข้อมูลพิกัด...")
for idx, location in enumerate(data["university_name_th"]):
    try:
        # เพิ่ม "Thailand" เพื่อความแม่นยำ
        search_query = f"{location}, Thailand"
        getLoc = loc.geocode(search_query)
        
        if getLoc:
            print(f"{idx+1}/{len(data)}: {location}")
            print(f"  Address: {getLoc.address}")
            print(f"  Coordinates: {getLoc.latitude}, {getLoc.longitude}")
            
            # กำหนดค่าให้แต่ละแถว (ไม่ใช่ทั้งคอลัมน์)
            data.loc[idx, 'latitude'] = getLoc.latitude
            data.loc[idx, 'longitude'] = getLoc.longitude
        else:
            print(f"{idx+1}/{len(data)}: ไม่พบข้อมูลสำหรับ {location}")
            data.loc[idx, 'latitude'] = None
            data.loc[idx, 'longitude'] = None
            
        # หน่วงเวลาเพื่อไม่ให้ถูก rate limit
        time.sleep(1)
        
    except Exception as e:
        print(f"Error processing {location}: {e}")
        data.loc[idx, 'latitude'] = None
        data.loc[idx, 'longitude'] = None

# ตรวจสอบผลลัพธ์
print("\nสรุปผลลัพธ์:")
print(f"จำนวนข้อมูลทั้งหมด: {len(data)}")
print(f"จำนวนที่มีพิกัด: {data['latitude'].notna().sum()}")
print(f"จำนวนที่ไม่มีพิกัด: {data['latitude'].isna().sum()}")

# แสดงตัวอย่างข้อมูล
print("\nตัวอย่างข้อมูลที่ได้:")
print(data[['university_name_th', 'latitude', 'longitude']].head(10))

# บันทึกไฟล์
data.to_csv('data/filtered_ai_com_courses.csv', index=False)
data.to_excel('data/filtered_ai_com_courses.xlsx', index=False)
print("\nบันทึกไฟล์เรียบร้อยแล้ว!")