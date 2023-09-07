import tempfile
from tkinter import *
from tkinter import messagebox
import random,os,smtplib


if not os.path.exists('bills'):
    os.mkdir("bills")

root = Tk()
# ?windows
root.title("Retail Billing ")
root.geometry("1366x768")
root.iconbitmap("icon.ico")
# heading
headingLabel = Label(root, text='Retail Billing System', font=(' times new roman',30,'bold'),
                     bg="grey20",fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,)

# functionality
# searchbutton
def search_biils():
    for i in os.listdir("bills/"):
        if i.split('.')[0] == billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('ERROR','Invalid Bill Number')

            # print function
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('ERROR',"CANNOT PRINT EMPETY BILL", )
    else:
        file=tempfile.mkdtemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
            # clear button

def clear():


    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    bodylotionEntry.delete(0, END)

    daalEntry.delete(0, END)
    riceEntry.delete(0, END)
    sugarEntry.delete(0, END)
    wheatEntry.delete(0, END)
    teaEntry.delete(0, END)
    oilEntry.delete(0, END)

    cocacolaEntry.delete(0, END)
    maazaEntry.delete(0, END)
    dewEntry.delete(0, END)
    spriteEntry.delete(0,END)
    frootiEntry.delete(0, END)
    pepsiEntry.delete(0, END)


    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)

    daalEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    teaEntry.insert(0, 0)
    oilEntry.insert(0, 0)

    cocacolaEntry.insert(0, 0)
    maazaEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)

    cosmeticstaxEntry.delete(0,0)
    grocerypriceEntry.delete(0,0)
    grocerytaxEntry.delete(0,0)
    cosmeticstaxEntry.delete(0,0)
    drinkpriceEntry.delete(0,0)
    drinktaxEntry.delete(0,0)

    billnumberEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    textarea.delete(1.0,END)


            # email button

def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smpt.gmail.com',587)
            ob.starttls()
            ob.login(senderIdEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            # reciever_address=recieverIdEntry.get()
            ob.sendmail(senderIdEntry.get(),recieverIdEntry.get(),message)
            ob.quit()
            messagebox.showinfo('SUCCESS',"Bill Is Sucessfully SENT !", parent=root1)
            root1.destroy()

        except:
            messagebox.showerror("ERROR","CAN'T SEND MAIL \n PLEASE TRY AGAIN",parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('ERROR',"NOTHING TO SEND IN EMAIL")
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('SEND GMAIL')
        root1.config(bg='grey20')
        root1.resizable(0,0)


        senderFrame=LabelFrame(root1,text="SENDER's Email ",font=('arial',16,'bold'),bd=6,bg="grey20",fg="white")
        senderFrame.grid(row=0,column=0)

        senderIdLabel= Label(senderFrame,text="Gmail Id :-",font=('arial', 16, 'bold'),bd=6,bg="gray20",fg="white")
        senderIdLabel.grid(row=0, column=0, padx=10,pady=8)
        senderIdEntry=Entry(senderFrame,font=('arial', 16, 'bold'),bd=2,width=23,relief=RIDGE)
        senderIdEntry.grid(row=0,column=1, padx=10,pady=8)


        passwordLabel = Label(senderFrame, text="Password :-", font=('arial', 16, 'bold'),bd=6,bg="grey20",fg="white")
        passwordLabel.grid(row=1, column=0 , padx=10,pady=8)
        passwordEntry= Entry(senderFrame,font=('arial', 16, 'bold'),bd=2,width=23,relief=RIDGE,show="#")
        passwordEntry.grid(row=1,column=1 , padx=10,pady=8)


        recieverFrame = LabelFrame(root1, text="RECIEVER's Mail ", font=('arial', 16, 'bold'),bd=6, bg="grey20", fg="white")
        recieverFrame.grid(row=1, column=0)

        recieverIdLabel = Label(recieverFrame, text="Gmail Id :-", font=('arial', 16, 'bold'), bd=6, bg="gray20", fg="white")
        recieverIdLabel.grid(row=0, column=0, padx=10, pady=8)
        recieverIdEntry = Entry(recieverFrame, font=('arial', 16, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverIdEntry.grid(row=0, column=1, padx=10, pady=8)


        messageLabel = Label(recieverFrame, text="Message :-", font=('arial', 16, 'bold'), bd=6, bg="gray20", fg="white")
        messageLabel.grid(row=1, column=0, padx=10, pady=8)
        email_textarea=Text(recieverFrame,font=('arial',8,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('='," ").replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text="SEND",font=('arial',16,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20,)

        root1.mainloop()



billnumber=random.randint(500,1000)
def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror("ERROR","Please Fill Costumer Details")
    elif cosmeticspriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkpriceEntry.get()=='':
        messagebox.showerror("ERROR","Please Make Some Purchases ")
    elif cosmeticspriceEntry.get()=='0Rs' and grocerypriceEntry.get()=='0Rs' and drinkpriceEntry.get()=='0Rs':
        messagebox.showerror("ERROR", "Please Make Some Purchases ")
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,"\t\t\t**Welcome Here**\n")
        textarea.insert(END,f'\nBill number: {billnumber}')
        textarea.insert(END, f'\nCostumer name: {nameEntry.get()}')
        textarea.insert(END, f'\nCostumer phone number: {phoneEntry.get()}')
        textarea.insert(END,'\n===========================================================')
        textarea.insert(END,'\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n===========================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END, f' \nBath soap : \t\t\t{bathsoapEntry.get()}\t\t\t {soapprice}rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END, f' \nFace cream : \t\t\t{facecreamEntry.get()}\t\t\t {facecreamprice}rs')
        if facewashEntry.get()!='0':
            textarea.insert(END, f' \nFace wash : \t\t\t{facewashEntry.get()}\t\t\t {facewashprice}rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END, f' \nHair spray : \t\t\t{hairsprayEntry.get()}\t\t\t {hairsprayprice}rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END, f' \nHair gel : \t\t\t{hairgelEntry.get()}\t\t\t {hairgelprice}rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END, f' \nBody lotion : \t\t\t{bodylotionEntry.get()}\t\t\t {bodylotionprice}rs')


        if riceEntry.get()!='0':
            textarea.insert(END, f' \nrice : \t\t\t{riceEntry.get()}\t\t\t {riceprice}rs')
        if oilEntry.get()!='0':
            textarea.insert(END, f' \noil : \t\t\t{oilEntry.get()}\t\t\t {oilprice}rs')
        if daalEntry.get()!='0':
            textarea.insert(END, f' \ndaal : \t\t\t{daalEntry.get()}\t\t\t {daalprice}rs')
        if sugarEntry.get()!='0':
            textarea.insert(END, f' \nsugar : \t\t\t{sugarEntry.get()}\t\t\t {sugarprice}rs')
        if wheatEntry.get()!='0':
            textarea.insert(END, f' \nwheat : \t\t\t{wheatEntry.get()}\t\t\t {wheatprice}rs')
        if teaEntry.get()!='0':
            textarea.insert(END, f' \nTea  : \t\t\t{teaEntry.get()}\t\t\t {teaprice}rs')


        if maazaEntry.get()!='0':
            textarea.insert(END, f' \nMaaza : \t\t\t{maazaEntry.get()}\t\t\t {maazaprice}rs')
        if pepsiEntry.get()!='0':
            textarea.insert(END, f' \nPepsi : \t\t\t{pepsiEntry.get()}\t\t\t {pepsiprice}rs')
        if spriteEntry.get()!='0':
            textarea.insert(END, f' \nSprite : \t\t\t{spriteEntry.get()}\t\t\t {spriteprice}rs')
        if dewEntry.get()!='0':
            textarea.insert(END, f' \nDew : \t\t\t{dewEntry.get()}\t\t\t {dewprice}rs')
        if frootiEntry.get()!='0':
            textarea.insert(END, f' \nfrooti : \t\t\t{frootiEntry.get()}\t\t\t {frootiprice}rs')
        if cocacolaEntry.get()!='0':
            textarea.insert(END, f' \nCoca cola  : \t\t\t{cocacolaEntry.get()}\t\t\t {cocacolaprice}rs')

        textarea.insert(END, '\n===========================================================')

#         taxarea
        if cosmeticstaxEntry.get() != '0.0':
            textarea.insert(END, f' \ncosmetics tax  : \t\t\t{cosmeticstaxEntry.get()}')
        if grocerytaxEntry.get() != '0.0':
            textarea.insert(END, f' \ncosmetics tax  : \t\t\t{grocerytaxEntry.get()}')
        if drinktaxEntry.get() != '0.0':
            textarea.insert(END, f' \ncosmetics tax  : \t\t\t{drinktaxEntry.get()}')
        textarea.insert(END,f'\n\n TOTAL BILL :\t\t\t\t\t {totalbill}')
    textarea.insert(END, '\n===========================================================')
    save_bill()


def save_bill():
    global billnumber
    result=messagebox.askyesno('CONFIRM',"Do You Want TO Save")
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Sucsess',f'Bill number :{billnumber} is saved successfully')
        billnumber =random.randint(500,1000)
# ?totaling
def total ():
    global totalbill
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    # totaling cosmetics
    soapprice= int(bathsoapEntry.get())*20
    facecreamprice = int(facecreamEntry.get()) * 100
    facewashprice = int(facewashEntry.get()) * 70
    hairsprayprice = int(hairsprayEntry.get()) * 50
    hairgelprice = int(hairgelEntry.get()) * 90
    bodylotionprice = int(bodylotionEntry.get()) * 250

    totalcosmeticsprice = soapprice+facewashprice+facecreamprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticspriceEntry.delete(0,END)
    cosmeticspriceEntry.insert(0,f'{totalcosmeticsprice}Rs')
    cosmeticstax=totalcosmeticsprice*0.18
    cosmeticstaxEntry.delete(0,END)
    cosmeticstaxEntry.insert(0,cosmeticstax)

    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice
#     totaling groccery
    riceprice= int(riceEntry.get())*80
    oilprice = int(oilEntry.get()) * 100
    daalprice = int(daalEntry.get()) * 180
    wheatprice = int(wheatEntry.get()) * 30
    sugarprice = int(sugarEntry.get()) * 40
    teaprice = int(teaEntry.get()) * 400

    totalgroceryprice = riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice}Rs')
    grocerytax=totalgroceryprice*0.18
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,grocerytax)

    # ? totaling of drinks
    global maazaprice,pepsiprice,spriteprice,dewprice,frootiprice,cocacolaprice
    maazaprice= int(maazaEntry.get())*40
    pepsiprice = int(pepsiEntry.get()) * 40
    spriteprice = int(spriteEntry.get()) * 30
    dewprice = int(dewEntry.get()) * 40
    frootiprice = int(frootiEntry.get()) * 40
    cocacolaprice = int(cocacolaEntry.get()) * 40

    totaldrinksprice = maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cocacolaprice
    drinkpriceEntry.delete(0,END)
    drinkpriceEntry.insert(0,f'{totaldrinksprice}Rs')
    drinktax=totaldrinksprice*0.18
    drinktaxEntry.delete(0,END)
    drinktaxEntry.insert(0,drinktax)

    totalbill=totalcosmeticsprice+totaldrinksprice+totalgroceryprice+cosmeticstax+grocerytax+drinktax

# ?gui part

# ?costumers details

costumer_details_frame = LabelFrame(root, text='Costumer Details' ,font=(' times new roman',15,'bold')
                                    ,fg="gold",bd=8 , relief=GROOVE, bg="grey20")
costumer_details_frame.pack(fill=X)
# name and details
nameLabel = Label(costumer_details_frame, text='Name',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
nameLabel.grid(row=0, column=0,padx=20)

nameEntry = Entry(costumer_details_frame,font=('arial',15),bd=7, width=18,)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel = Label(costumer_details_frame, text='Phone Number',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
phoneLabel.grid(row=0, column=2,padx=20,pady=2)

phoneEntry = Entry(costumer_details_frame,font=('arial',15),bd=7, width=18,)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel = Label(costumer_details_frame, text='Bill Number',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
billnumberLabel.grid(row=0, column=4,padx=20,pady=2)

billnumberEntry = Entry(costumer_details_frame,font=('arial',15),bd=7, width=18,)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton= Button(costumer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10, command=search_biils)
searchButton.grid(row=0,column=6,padx=20,pady=8)

# store products details frames

productFrame=Frame(root)
productFrame.pack()
# products frame...
cosmeticsFrame=LabelFrame(productFrame,text='Cosmetics',font=('times new roman',15,'bold')
                                    ,fg="gold",bd=8 , relief=GROOVE, bg="grey20")
cosmeticsFrame.grid(row=0,column=0)

bathsoapLable=Label(cosmeticsFrame,text='Bath Soap',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
bathsoapLable.grid(row=0,column=0,pady=9 , padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9 , padx=10)
bathsoapEntry.insert(0,0)


facecreamLable=Label(cosmeticsFrame,text='Face Cream',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
facecreamLable.grid(row=2,column=0,pady=9 , padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=2,column=1,pady=9 , padx=10)
facecreamEntry.insert(0,0)


facewashLable=Label(cosmeticsFrame,text='Face Wash',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
facewashLable.grid(row=3,column=0,pady=9 , padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=3,column=1,pady=9 , padx=10)
facewashEntry.insert(0,0)

hairsprayLable=Label(cosmeticsFrame,text='Hair Spray',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
hairsprayLable.grid(row=4,column=0,pady=9 , padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=4,column=1,pady=9 , padx=10)
hairsprayEntry.insert(0,0)

hairgelLable=Label(cosmeticsFrame,text='Hair Gel',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
hairgelLable.grid(row=5,column=0,pady=9 , padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=5,column=1,pady=9 , padx=10)
hairgelEntry.insert(0,0)

bodylotionLable=Label(cosmeticsFrame,text='Body Lotion ',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
bodylotionLable.grid(row=6,column=0,pady=9 , padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=6,column=1,pady=9 , padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productFrame,text='Grocery',font=('times new roman',15,'bold')
                                    ,fg="gold",bd=8 , relief=GROOVE, bg="grey20")
groceryFrame.grid(row=0,column=1)

riceLable=Label(groceryFrame,text='Rice',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
riceLable.grid(row=1,column=0,pady=9 , padx=10,sticky='w')

riceEntry=Entry(groceryFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=1,column=1,pady=9 , padx=10)
riceEntry.insert(0,0)

oilLable=Label(groceryFrame,text='Oil',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
oilLable.grid(row=2,column=0,pady=9 , padx=10,sticky='w')

oilEntry=Entry(groceryFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=2,column=1,pady=9 , padx=10)
oilEntry.insert(0,0)

daalLable=Label(groceryFrame,text='Daal',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
daalLable.grid(row=3,column=0,pady=9 , padx=10,sticky='w')

daalEntry=Entry(groceryFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=3,column=1,pady=9 , padx=10)
daalEntry.insert(0,0)


wheatLable=Label(groceryFrame,text='Wheat',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
wheatLable.grid(row=4,column=0,pady=9 , padx=10,sticky='w')

wheatEntry=Entry(groceryFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=4,column=1,pady=9 , padx=10)
wheatEntry.insert(0,0)

sugarLable=Label(groceryFrame,text='Sugar',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
sugarLable.grid(row=5,column=0,pady=9 , padx=10,sticky='w')

sugarEntry=Entry(groceryFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=5,column=1,pady=9 , padx=10)
sugarEntry.insert(0,0)

teaLable=Label(groceryFrame,text='Tea',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
teaLable.grid(row=6,column=0,pady=9 , padx=10,sticky='w')

teaEntry=Entry(groceryFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=6,column=1,pady=9 , padx=10)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productFrame,text='Cold Drinks',font=('times new roman',15,'bold')
                                    ,fg="gold",bd=8 , relief=GROOVE, bg="grey20")
drinksFrame.grid(row=0,column=2)


maazaLable=Label(drinksFrame,text='Maaza',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
maazaLable.grid(row=1,column=0,pady=9 , padx=10,sticky='w')

maazaEntry=Entry(drinksFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=1,column=1,pady=9 , padx=10)
maazaEntry.insert(0,0)
pepsiLable=Label(drinksFrame,text='Pepsi',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
pepsiLable.grid(row=2,column=0,pady=9 , padx=10,sticky='w')

pepsiEntry=Entry(drinksFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=2,column=1,pady=9 , padx=10)
pepsiEntry.insert(0,0)

spriteLable=Label(drinksFrame,text='Sprite',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
spriteLable.grid(row=3,column=0,pady=9 , padx=10,sticky='w')

spriteEntry=Entry(drinksFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=3,column=1,pady=9 , padx=10)
spriteEntry.insert(0,0)


dewLable=Label(drinksFrame,text='Dew',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
dewLable.grid(row=4,column=0,pady=9 , padx=10,sticky='w')

dewEntry=Entry(drinksFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=4,column=1,pady=9 , padx=10)
dewEntry.insert(0,0)

frootiLable=Label(drinksFrame,text='frooti',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
frootiLable.grid(row=5,column=0,pady=9 , padx=10,sticky='w')

frootiEntry=Entry(drinksFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=5,column=1,pady=9 , padx=10)
frootiEntry.insert(0,0)

cocacolaLable=Label(drinksFrame,text='Coca Cola',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
cocacolaLable.grid(row=6,column=0,pady=9 , padx=10,sticky='w')

cocacolaEntry=Entry(drinksFrame ,font=(' times new roman',15,'bold'),width=10,bd=5)
cocacolaEntry.grid(row=6,column=1,pady=9 , padx=10)
cocacolaEntry.insert(0,0)

# bill area /recipt area

billFrame=Frame(productFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3)

billarealable=Label(billFrame,text='Label Area',font=(' times new roman',15,'bold'),
                    bd=7 ,relief=GROOVE)
billarealable.pack(fill=X)
scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billFrame,height=19 ,width=60,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# bill area

billmenuFrame=LabelFrame(root,text='Bill Area',font=(' times new roman',15,'bold')
                  ,fg="white",bg="grey20" )
billmenuFrame.pack(padx=20,fill=X)

cosmeticspriceLable=Label(billmenuFrame,text='Cosmetics Price',font=(' times new roman',13,'bold')
                  ,fg="white",bg="grey20" )
cosmeticspriceLable.grid(row=0,column=0,pady=9 , padx=10,sticky='w')

cosmeticspriceEntry=Entry(billmenuFrame ,font=(' times new roman',13,'bold'),width=10,bd=5)
cosmeticspriceEntry.grid(row=0,column=1, padx=10)


grocerypriceLable=Label(billmenuFrame,text='Grocery Price ',font=(' times new roman',13,'bold')
                  ,fg="white",bg="grey20" )
grocerypriceLable.grid(row=1,column=0,pady=9 , padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame ,font=(' times new roman',13,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1, padx=10)

drinkpriceLable=Label(billmenuFrame,text='Drink Price ',font=(' times new roman',13,'bold')
                  ,fg="white",bg="grey20" )
drinkpriceLable.grid(row=2,column=0,pady=9 , padx=10,sticky='w')

drinkpriceEntry=Entry(billmenuFrame ,font=(' times new roman',13,'bold'),width=10,bd=5)
drinkpriceEntry.grid(row=2,column=1, padx=10)

# taxx
cosmeticstaxLable=Label(billmenuFrame,text='Cosmetics Tax ',font=(' times new roman',13,'bold')
                  ,fg="white",bg="grey20" )
cosmeticstaxLable.grid(row=0,column=3,pady=9 , padx=10,sticky='w')

cosmeticstaxEntry=Entry(billmenuFrame ,font=(' times new roman',13,'bold'),width=10,bd=5)
cosmeticstaxEntry.grid(row=0,column=4, padx=10)


grocerytaxLable=Label(billmenuFrame,text='Grocery Tax ',font=(' times new roman',13,'bold')
                  ,fg="white",bg="grey20" )
grocerytaxLable.grid(row=1,column=3,pady=9 , padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame ,font=(' times new roman',13,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=4, padx=10)

drinktaxLable=Label(billmenuFrame,text='Drink Tax ',font=(' times new roman',13,'bold')
                  ,fg="white",bg="grey20" )
drinktaxLable.grid(row=2,column=3,pady=9 , padx=10,sticky='w')

drinktaxEntry=Entry(billmenuFrame ,font=(' times new roman',13,'bold'),width=10,bd=5)
drinktaxEntry.grid(row=2,column=4, padx=10)


buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE,bg="gray20")
buttonFrame.grid(row=0,column=5,rowspan=3,padx=30)
totalbutton=Button(buttonFrame,text='Total',font=('arialo',16,'bold'),bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=5, )

billbutton=Button(buttonFrame,text='Bill',font=('arialo',16,'bold'),bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonFrame,text='Email',font=('arialo',16,'bold'),bd=5,width=8,pady=10,command=send_email)
emailbutton.grid(row=0,column=2,pady=20,padx=5)


printbutton=Button(buttonFrame,text='Print',font=('arialo',16,'bold'),bd=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonFrame,text='Clear',font=('arialo',16,'bold'),bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=20,padx=5)



root.mainloop()



# this is billing software
# MADE WITH THE HELP OF (youtube ,google)
# developers name :- Shanu,Saiam,Ritesh,Neeraj,Vishal Kumar