import requests

url="https://my-tcas.s3.ap-southeast-1.amazonaws.com/mytcas/courses.json?ts=19817575305"

# ส่ง GET request ไปยัง API
response = requests.get(url)

print("Status Code:", response.status_code)


# วิศวะกรรมคอมพิวเตอร์ และ วิศวกรรมปัญญาประดิษฐ์

if response.status_code == 200:
    data = response.json()
    print(data[0])
    print(len(data))
    # for user in data:
        # print(f"ชื่อ: {user['name']}, อีเมล: {user['email']}")
else:
    print("ไม่สามารถดึงข้อมูลได้")


