from tkinter import *
from tkinter import messagebox
import json
no_webites=0
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_write.insert(0,password)
    #------------------------------search across json file----------------------#
def search():
    with open("userdetails.json") as file:
        s_data=json.load(file)
        try:
            messagebox.showinfo(title=f"{website_write.get()} details",message=f" Email: {s_data[website_write.get()]['email']}\n Password: {s_data[website_write.get()]['password']}")
        except:
            messagebox.showwarning(title="Error",message="No data found on that wesite.")
    # ---------------------------- SAVE PASSWORD ------------------------------- #
def details():
    global no_webites
    no_webites+=1
    ok=messagebox.askokcancel(title="Website info",message=f"tese are the details you entered \n email:{email_write} \n password:{password_write} \n press ok to save and cancel to discard")
    new_data={
        website_write.get():{
            "email":email_write.get(),
            "password":password_write.get()
        }
    }
    if ok:
        try:
            file=open("userdetails.json","r")
            data=json.load(file)
            data.update(new_data)
            file.close()
        except:
            file=open("userdetails.json","w")
            json.dump(new_data,file,indent=4)
            file.close()
        else:
            file=open("userdetails.json","w")
            json.dump(data,file,indent=4)
            file.close()
        finally:
            website_write.delete(0,END)
            email_write.delete(0,END)
            password_write.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password manager")
window.config(padx=20,pady=20)
canvas=Canvas(height=200,width=200)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=1)
website=Label(text="Website:",font=("Arial","18"))
website.grid(column=0,row=2)
website_write=Entry(width=35)
website_write.focus()
website_write.grid(row=2,column=1,columnspan=2)
website_search=Button(text="search",font=("Roboto","10","bold"),command=search)
website_search.grid(column=2,row=2)
email=Label(text="Email/Username:",font=("Arial","18"))
email.grid(column=0,row=3)
email_write=Entry(width=35)
email_write.focus()
email_write.grid(row=3,column=1,columnspan=2)
password=Label(text="Password:",font=("Arial","18"))
password.grid(column=0,row=4)
password_write=Entry(width=21)
password_write.grid(row=4,column=1)
gen_pass=Button(text="Generate password",font=("Roboto","9"),command=gen_pass)
gen_pass.grid(column=2,row=4)
add=Button(text="Add",font=("Roboto","10"),width=36,command=details)
add.grid(column=1,row=5,columnspan=2)







window.mainloop()