def vEmail(email):
    domain = ["org","com","eg","edu"]
    try:
        if "@" not in  email and "." not in email:
            raise ValueError("missing '@'  or '.' ")
        parts = email.split("@")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            raise ValueError("Invaild structure of eamil")
        username = parts[0]
        dom = parts[1].split(".")
        if len(dom) != 2 or dom[1] not in domain:
            raise ValueError("Your Domain Not Vaild")
        return True
    except ValueError as e: 
        print("Invaild Email ",e)

def vName(name):
    try:
        for i in name.split():
            if not i.isalpha() or len(i) == 0:
                return False
        else: 
            print(f"Your Name is :  {i} ")
            return True
    except UnboundLocalError:
        print("Please Enter a Vaild Name")       


# if __name__ == "__main__":
#     while True : 
#         name = input("Please enter Your Name :  ")
#         vaildName = vName(name)
#         if vaildName:
#             pass
#         else:
#             print("------------------------------")
#             print("Please Enter a Vaild Name ! ")
#             continue
#         email = input("Please enter your Email:  ")     
#         vaildEmail = vEmail(email)
#         if vaildEmail:
#             break
#         else:
#             print("Please Enter a Vaild Email ! ")
#             print("------------------------------")
                            

#     print(f"Your Name is {name} , And Your Email is {email}")
