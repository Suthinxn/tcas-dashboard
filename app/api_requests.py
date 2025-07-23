# import requests

# url="https://my-tcas.s3.ap-southeast-1.amazonaws.com/mytcas/courses.json?ts=19817575305"

# # ส่ง GET request ไปยัง API
# response = requests.get(url)

# print("Status Code:", response.status_code)


# # วิศวะกรรมคอมพิวเตอร์ และ วิศวกรรมปัญญาประดิษฐ์

# if response.status_code == 200:
#     datas = response.json()
#     # print(data[0])
#     # print(type(data[0]))
#     # print(len(data))
    
#     # for key, value in data[0].items():
        
#     #     print(f"{key} : {value}")
#     i = 1
#     for data in datas:
#         if data["faculty_name_th"] == "คณะวิศวกรรมศาสตร์":
#             # print(data["group_field_th"])
#             if "ปัญญาประดิษฐ์" in data["program_name_th"]:
#                 print(f"{i} : {data['program_name_th']}")
#                 i += 1
            
# else:
#     print("ไม่สามารถดึงข้อมูลได้")

# # [
# # "_id",
# # "university_type_id",
# # "university_type_name_th",
# # "university_id",
# # "university_name_th",
# # "university_name_en",
# # "campus_id",
# # "campus_name_th",
# # "campus_name_en",
# # "faculty_id",
# # "faculty_name_th",
# # "faculty_name_en",
# # "group_field_id",
# # "group_field_th",
# # "field_id",
# # "field_name_th",
# # "field_name_en",
# # "program_running_number",
# # "program_name_th",
# # "program_name_en",
# # "program_type_id",
# # "program_type_name_th",
# # "program_id",
# # "number_acceptance_mko2",
# # "program_partners_id",
# # "program_partners_inter_name",
# # "country_partners_name",
# # "major_acceptance_number",
# # "cost",
# # "graduate_rate",
# # "employment_rate",
# # "median_salary",
# # "created_at",
# # "updated_at",
# # ]