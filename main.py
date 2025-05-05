import functions as fn
import marioProblem as mario
import multiplicationTable as mul
import Vaildation as vd


fn.sort_numbers([5, 2, 8, 1, 9])  
print("=======================================================")

fn.count_vowels("htis is my name")
print("=======================================================")

fn.find_i_location("i location")
print("=======================================================")

mario.print_from_list(6)
print("=======================================================")

mario.print_triangle(6)
print("=======================================================")

mul.generate_multiplication_table()
print("=======================================================")

mul.multiplication_table()
print("=======================================================")



while True : 
        name = input("Please enter Your Name :  ")
        vaildName = vd.vName(name)
        if vaildName:
            pass
        else:
            print("------------------------------")
            print("Please Enter a Vaild Name ! ")
            continue
        email = input("Please enter your Email:  ")     
        vaildEmail = vd.vEmail(email)
        if vaildEmail:
            break
        else:
            print("Please Enter a Vaild Email ! ")
            print("------------------------------")
                            

print(f"Your Name is {name} , And Your Email is {email}")
