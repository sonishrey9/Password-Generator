import string
import  random
from datetime import datetime as d

if __name__ == '__main__':

    def time_and_date():  # function o take time and date input from user

        date = d.now()

        return date.strftime("%d-%m-%Y , %S:%M:%H")

    def password_generator():

        while(1):
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation

            #username, website, password
            username = input("ENTER USERNAME : \n")
            website = input("ENTER WEBSITE : \n")
            plen = int(input("ENTER PASSWORD LENGTH : \n "))

            s = [] # empyty listto feed all values stored in s
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            # Extend function to add all elements in one list    # print(s)

            random.shuffle(s)

            mypassword = "".join(s[0:plen])

            #writing the password generator into csv file
            with open("password.csv", "a+") as password:
                password.write(f" {username}, {mypassword} , {website}, {time_and_date()} \n")
                print(f" Details are \n"
                      f"USERNAME : {username} \n"
                      f"PASSWORD : {mypassword} \n"
                      f"WEBSITE : {website} \n"
                      f"DATE & TIME : {time_and_date()} \n")

            print(f"YOUR PASSWORD IS \n"
                  f"{mypassword}")

            answer = input("Do you Wish to continue, Type Y for yes, N for No")

            if answer == "Y" or answer == "y":
                continue

            else:
                break


password_generator()