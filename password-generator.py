import string
import  random

if __name__ == '__main__':

    def password_generator():

        while(1):
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation

            #username, website, password
            username = input("enter the username")
            website = input("enter the website")
            plen = int(input("enter password length \n "))

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
                password.write(f" {username}, {mypassword} , {website} \n")
                print(f" Details are"
                      f"{username}, {mypassword} , {website} \n")

            answer = input("Do you Wish to continue, Type Y for yes, N for No")

            if answer == "Y" or answer == "y":
                continue

            else:
                break


password_generator()