import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Janakiraman123!@#",database="education_loan")
mycursor=mydb.cursor()
class accountdetails:
    def __init__(self, username,Account_number):
        self.username = username
        self.Account_number = Account_number
    def user_details_checking(username,Account_number,bank_name):
        mycursor.execute("select * from user_details where account_number like %s",(Account_number,))
        data=mycursor.fetchall()
        if username==data[0][1] and Account_number==data[0][2] and bank_name==data[0][3]:
            return data[0][0]
def college_details(self):
    global name
    name=input("ENTER YOUR NAME AS PER CERTIFICATE:")
    college_name=input('ENTER YOUR COLLEGE NAME:')
    degree=input("ENTER YOUR DEGREE :")
    CGPA=input("ENTER YOUR CGPA:")
    mycursor.execute("insert into college_details(name,college_name,degree,CGPA)values(%s,%s,%s,%s);",(name,college_name,degree,CGPA,))
    mydb.commit()
    return 1
def loan_details(self):
    mycursor.execute("select * from college_details where name like %s",(name,))
    data=mycursor.fetchall()
    cgpa=data[0][4]
    cgpa=int(cgpa)
    mycursor.execute("select * from loan_details;")
    mydata=mycursor.fetchall()
    for i in mydata:
        if cgpa>=int(i[5]):
            print(i)
username=str(input("ENTER YOUR NAME :"))
Account_number=str(input("ENTER YOUR ACCOUNT NUMBER :"))
bank_name=input("ENTER YOUR BANK NAME :")
IFSC_CODE=input("ENTER IFSC CODE :")
password=input("ENTER YOUR PASSWORD :")
checked_data=accountdetails(username,Account_number)
data=checked_data.user_details_checking
if data:
    checking=input('ENTER YES IF ALREADY APPLIED FOR LOAN ELSE NO :')
    checking=checking.lower()
    if checking =="yes":
        print("True")
    else:
        if college_details(username):
            if loan_details(name):
                print(True)                
else:
    print('ENTER VALID ACCOUNT NUMBER')

