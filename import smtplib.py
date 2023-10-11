import smtplib
myemail="praveenkumarreddy061@gmail.com"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=myemail,password="trmxkjlhszelkejp")
ls=["neelurupraveenkumarreddy@gmail.com","kumarreddypraveen04@gmail.com","centrestudy66@gmail.com"]
for i in ls:
    connection.sendmail(from_addr=myemail,to_addrs=i,msg=f"hii {i}, \n I am praveen")
connection.close()