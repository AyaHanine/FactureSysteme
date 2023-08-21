#import tkinter 
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib


#generer les numeros de facture :
NumFacture = random.randint(500,1000)

#les fonctions :

if not os.path.exists('Factures'):
    os.mkdir('Factures')

#total function :
def total():
    global shampooPrice,savonPrice,GeldouchePrice,MakeupPrice,SoinVisagePrice,VernisPrice
    global LegumesPrice,FruitsPrice,PatesPrice,OilPrice,EpicePrice,ViandePrice
    global WaterPrice,SodaPrice,AlcoolPrice,JusPrice,MilkPrice,SiropPrice
    global cosmeticTaxes,alimentsTaxes,drinksTaxes
    global TotalC,TotalD,TotalA

    shampooPrice = int(ShampooInput.get()) * 70
    savonPrice = int(SavonInput.get()) * 15
    GeldouchePrice = int(GelDoucheInput.get()) * 45
    MakeupPrice = int(MakeupInput.get()) * 70
    SoinVisagePrice = int(SoinVisageInput.get()) * 50
    VernisPrice = int(VernisInput.get()) * 10


    TotalC = shampooPrice + savonPrice + GeldouchePrice + MakeupPrice + SoinVisagePrice + VernisPrice
    cosmeticTaxes = TotalC * 0.02
    CosmeticsTaxesInput.delete(0, END)
    CosmeticsTaxesInput.insert(0, str(cosmeticTaxes)+ ' DH')

    CosmeticsPriceInput.delete(0,END)
    CosmeticsPriceInput.insert(0, str(TotalC) + ' DH')

    LegumesPrice = int(LegumesInput.get()) *7
    FruitsPrice = int(FruitsInput.get()) * 8
    PatesPrice = int(PatesInput.get()) * 12
    OilPrice = int(OilInput.get()) * 13
    EpicePrice = int(EpiceInput.get()) *5
    ViandePrice = int(ViandeInput.get()) * 12

    TotalA = LegumesPrice+FruitsPrice+PatesPrice+OilPrice+EpicePrice+ViandePrice
    alimentsTaxes = TotalA * 0.03
    AlimentTaxesInput.delete(0, END)
    AlimentTaxesInput.insert(0, str(alimentsTaxes)+' DH')

    AlimentPriceInput.delete(0, END)
    AlimentPriceInput.insert(0,str(TotalA)+' DH')

    WaterPrice=int(WaterInput.get())*10
    SodaPrice=int(SodaInput.get())*6
    AlcoolPrice=int(AlcoolInput.get())*70
    JusPrice=int(JusInput.get())*15
    MilkPrice=int(MilkInput.get())*30
    SiropPrice=int(SiropInput.get())*27

    TotalD = WaterPrice+SodaPrice+AlcoolPrice+JusPrice+MilkPrice+SiropPrice

    drinksTaxes = TotalD * 0.01
    DrinkTaxesInput.delete(0, END)
    DrinkTaxesInput.insert(0, str(drinksTaxes)+ ' DH')

    DrinkPriceInput.delete(0, END)
    DrinkPriceInput.insert(0,str(TotalD)+' DH')

def save():
    global NumFacture
    result=messagebox.askyesno('Confirm','Sauvegarder la facture ?')
    if result:
        #1.0 debut de la textArea et End jusqu'a la fin
        bill_content=textArea.get(1.0,END)
        file=open(f'Factures/ {NumFacture}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'La facture {NumFacture} est enregistrée')
        NumFacture = random.randint(500,1000)


def Bill():

    textArea.delete(1.0,END)

    if nameInput.get() =='' or phoneInput.get() =='':
        messagebox.showerror('Error','Customer Details are required !')
    elif CosmeticsPriceInput.get() =='' and AlimentPriceInput.get()=='' and DrinkPriceInput.get()=='':
        messagebox.showerror('Error','No products are seletcted')
    elif CosmeticsPriceInput.get() =='0 DH' or AlimentPriceInput.get()=='O DH' or DrinkPriceInput.get()=='O DH':
        messagebox.showerror('Error','No products are selected')
    else:
        textArea.insert(END,'\t\t\t ** Welcome  '+str(nameInput.get())+' **\n')
        textArea.insert(END,f'\nNuméro de facture : {NumFacture} \n')
        NumFactureInput.delete(0,END)
        NumFactureInput.insert(0,NumFacture)
        textArea.insert(END,f'Nom du Client: {nameInput.get()} \n')
        textArea.insert(END, f'Numéro de telephone: {phoneInput.get()} \n')
        textArea.insert(END, '\n================================================================\n')
        textArea.insert(END, 'Produit \t\t\t  Quantité \t\t\t  Prix')
        textArea.insert(END, '\n================================================================\n')

        if ShampooInput.get()!='0':
            textArea.insert(END,f'Shampoing \t\t\t  {ShampooInput.get()} \t\t\t  {shampooPrice}\tDH \n')
        if SavonInput.get()!='0':
            textArea.insert(END,f'Savon \t\t\t  {SavonInput.get()} \t\t\t  {savonPrice}\tDH \n')
        if GelDoucheInput.get() != '0':
            textArea.insert(END, f'Gel douche \t\t\t  {GelDoucheInput.get()} \t\t\t  {GeldouchePrice}\tDH \n')
        if MakeupInput.get()!='0':
            textArea.insert(END,f'Makeup \t\t\t  {MakeupInput.get()} \t\t\t  {MakeupPrice}\tDH \n')
        if SoinVisageInput.get()!='0':
            textArea.insert(END,f'Soin visage \t\t\t  {SoinVisageInput.get()} \t\t\t  {SoinVisagePrice}\tDH \n')
        if VernisInput.get()!='0':
            textArea.insert(END,f'Vernis \t\t\t  {VernisInput.get()} \t\t\t  {VernisPrice}\tDH \n')
        if LegumesInput.get()!='0':
            textArea.insert(END,f'Legumes \t\t\t  {LegumesInput.get()} \t\t\t  {LegumesPrice}\tDH \n')
        if FruitsInput.get()!='0':
            textArea.insert(END,f'Fruits \t\t\t  {FruitsInput.get()} \t\t\t  {FruitsPrice}\tDH \n')
        if PatesInput.get()!='0':
            textArea.insert(END,f'Pates \t\t\t  {PatesInput.get()} \t\t\t  {PatesPrice}\tDH \n')
        if OilInput.get()!='0':
            textArea.insert(END,f'Huile \t\t\t  {OilInput.get()} \t\t\t  {OilPrice}\tDH \n')
        if EpiceInput.get()!='0':
            textArea.insert(END,f'Epices \t\t\t  {EpiceInput.get()} \t\t\t  {EpicePrice}\tDH \n')
        if ViandeInput.get()!='0':
            textArea.insert(END,f'Viande \t\t\t  {ViandeInput.get()} \t\t\t  {ViandePrice}\tDH \n')
        if WaterInput.get()!='0':
            textArea.insert(END,f'Eau \t\t\t  {WaterInput.get()} \t\t\t  {WaterPrice}\tDH \n')
        if SodaInput.get()!='0':
            textArea.insert(END,f'Soda \t\t\t  {SodaInput.get()} \t\t\t  {SodaPrice}\tDH \n')
        if AlcoolInput.get()!='0':
            textArea.insert(END,f'Alcool \t\t\t  {AlcoolInput.get()} \t\t\t  {AlcoolPrice}\tDH \n')
        if JusInput.get()!='0':
            textArea.insert(END,f'Jus \t\t\t  {JusInput.get()} \t\t\t  {JusPrice}\tDH \n')
        if MilkInput.get()!='0':
            textArea.insert(END,f'Lait \t\t\t  {MilkInput.get()} \t\t\t  {MilkPrice}\tDH \n')
        if SiropInput.get()!='0':
            textArea.insert(END,f'Sirop \t\t\t  {SiropInput.get()} \t\t\t  {SiropPrice}\tDH \n')


        textArea.insert(END, '\n================================================================\n')


        if CosmeticsTaxesInput.get() != "0":
            textArea.insert(END, f'Cosmetiques Taxes \t\t\t\t\t\t  {cosmeticTaxes}\tDH \n')
        if AlimentTaxesInput.get()!="0":
            textArea.insert(END, f'Aliments Taxes \t\t\t\t\t\t  {alimentsTaxes}\tDH \n')
        if DrinkTaxesInput.get()!="0":
            textArea.insert(END, f'Boissons Taxes \t\t\t\t\t\t  {drinksTaxes}\tDH \n')


        textArea.insert(END, f'Prix total \t\t\t\t\t\t  {TotalC+TotalD+TotalA}\tDH \n')
        save()

def clear():
    nameInput.delete(0, END)
    phoneInput.delete(0, END)
    NumFactureInput.delete(0, END)

    ShampooInput.delete(0, END)
    ShampooInput.insert(0, 0)

    GelDoucheInput.delete(0, END)
    GelDoucheInput.insert(0, 0)

    SavonInput.delete(0, END)
    SavonInput.insert(0, 0)

    MakeupInput.delete(0, END)
    MakeupInput.insert(0, 0)

    VernisInput.delete(0, END)
    VernisInput.insert(0, 0)

    SoinVisageInput.delete(0, END)
    SoinVisageInput.insert(0, 0)

    LegumesInput.delete(0, END)
    LegumesInput.insert(0, 0)

    FruitsInput.delete(0, END)
    FruitsInput.insert(0, 0)

    PatesInput.delete(0, END)
    PatesInput.insert(0, 0)

    OilInput.delete(0, END)
    OilInput.insert(0, 0)

    EpiceInput.delete(0, END)
    EpiceInput.insert(0, 0)

    ViandeInput.delete(0, END)
    ViandeInput.insert(0, 0)

    SiropInput.delete(0, END)
    SiropInput.insert(0, 0)

    AlcoolInput.delete(0, END)
    AlcoolInput.insert(0, 0)

    MilkInput.delete(0, END)
    MilkInput.insert(0, 0)

    JusInput.delete(0, END)
    JusInput.insert(0, 0)

    SodaInput.delete(0, END)
    SodaInput.insert(0, 0)

    WaterInput.delete(0, END)
    WaterInput.insert(0, 0)

    CosmeticsPriceInput.delete(0, END)
    CosmeticsTaxesInput.delete(0, END)
    AlimentPriceInput.delete(0,END )
    AlimentTaxesInput.delete(0, END)
    DrinkTaxesInput.delete(0, END)
    DrinkPriceInput.delete(0, END)
    textArea.delete(1.0, END)


def search():
    for i in os.listdir('Factures/'):
        if i.split('.')[0].strip() == NumFactureInput.get():
            f=open(f'Factures/{i}','r')
            textArea.delete('1.0',END)
            for data in f :
                textArea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error','facture introuvable')


def print():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','La facture est vide')
    else:
        #create a temporary file:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textArea.get(1.0,END))
        # imprimer le fichier:
        os.startfile(file,'print')


def email():

    def send():
        try:
            #rbmt zvuh bssy hkov
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(gmailInput.get(),pwdInput.get())
            message = email_text.get(1.0,END)
            receiver_address = gmailRInput.get()
            ob.sendmail(gmailInput.get(),receiver_address,message)
            ob.quit()
            messagebox.showinfo('Success','facture envoyée')
        except:
            messagebox.showerror('Error','Un probleme est survenu ! réessayer')
    if textArea.get(1.0,END) =='\n':
       messagebox.showerror('Error','La facture est vide')
    else:
        email=Toplevel()
        email.title('Send Email')
        email.iconbitmap('EmailIcon.ico')
        email.config(bg='gray20')
        email.resizable(0,0)
        email.grab_set()

        senderFrame=LabelFrame(email,text='EMETTEUR',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        gmailLabel=Label(senderFrame,text="Email",font=('arial',14,'bold'))
        gmailLabel.grid(row=0,column=0,padx=10,pady=8)

        gmailInput=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        gmailInput.grid(row=0,column=1,padx=10,pady=8)


        pwdLabel = Label(senderFrame, text="Mot de passe", font=('arial', 14, 'bold'))
        pwdLabel.grid(row=1, column=0, padx=10, pady=8)

        pwdInput = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        pwdInput.grid(row=1, column=1, padx=10, pady=8)


        receiverFrame = LabelFrame(email, text='RECEPTEUR', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        receiverFrame.grid(row=1, column=0, padx=40, pady=20)


        gmailRLabel = Label(receiverFrame, text="Email", font=('arial', 14, 'bold'))
        gmailRLabel.grid(row=0, column=0, padx=10, pady=8)

        gmailRInput = Entry(receiverFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        gmailRInput.grid(row=0, column=1, padx=10, pady=8)


        messageLabel = Label(receiverFrame, text="Message", font=('arial', 14, 'bold'))
        messageLabel.grid(row=1, column=0, padx=10, pady=8)
        email_text=Text(receiverFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_text.grid(row=2,column=0,columnspan=2)
        email_text.delete(1.0,END)
        email_text.insert(END,textArea.get(1.0,END).replace('=','').replace('\t\t\t','\t\t'))

        SendBtn=Button(email,text='Envoyer',font=('arial',16,'bold'),width=15,command=send)
        SendBtn.grid(row=2,column=0,pady=20)



        email.mainloop()


#tk class helps create our window.
root=Tk()

#change our window title :
root.title('Systeme de Facturation')
#change our window size : (widthxheight)
root.geometry('1380x748')
#Add the icon :
root.iconbitmap('BillIcon.ico')

#Create the heading label
#we should add where we must see the label (root) and the text with styling (font size type(italic,bold..)) and choose the color with bg

headingLabel = Label(root,text="Systeme de Facturation",font=('times new roman',30,'bold'),bg='gray20',fg='gold',relief=GROOVE,bd=8
                     )
#to add it on the top
headingLabel.pack(fill=X,pady=10)

#add the second label :
# informations du client
customer_details_frame=LabelFrame(root,text='Informations du client',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame,text='Nom:',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameInput = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameInput.grid(row=0,column=1,padx=8)

phoneLabel = Label(customer_details_frame,text='Numero de telephone:',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20)

phoneInput = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneInput.grid(row=0,column=3,padx=8)

NumFactureLabel = Label(customer_details_frame,text='Numero de la Facture',font=('times new roman',15,'bold'),bg='gray20',fg='white')
NumFactureLabel.grid(row=0,column=4,padx=20)

NumFactureInput = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
NumFactureInput.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12),bd=7,command=search)
searchButton.grid(row=0,column=6,padx=20,pady=8)

#ADD THE THIRD LABEL :
#create the frame which contains 4 other frames : frames are visible only if we add smthng inside of it

productsFrame = Frame(root)
productsFrame.pack(pady=10)

cosmeticsFrame=LabelFrame(productsFrame,text="Produits Cosmetiques",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

ShampooLabel=Label(cosmeticsFrame,text='Shampoing',font=('times new roman',15,'bold'),bg='gray20',fg='white')
ShampooLabel.grid(row=0,column=0,padx=20,pady=9)
ShampooInput=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
ShampooInput.grid(row=0,column=1,padx=8,pady=9)
ShampooInput.insert(0,0)

SavonLabel=Label(cosmeticsFrame,text='Savon',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SavonLabel.grid(row=1,column=0,padx=20)
SavonInput=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
SavonInput.grid(row=1,column=1,padx=10,pady=9)
SavonInput.insert(0,0)

GelDoucheLabel=Label(cosmeticsFrame,text='Gel douche',font=('times new roman',15,'bold'),bg='gray20',fg='white')
GelDoucheLabel.grid(row=2,column=0,padx=20,pady=9)
GelDoucheInput=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
GelDoucheInput.grid(row=2,column=1,padx=10,pady=9)
GelDoucheInput.insert(0,0)

MakeupLabel=Label(cosmeticsFrame,text='Maquillage',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MakeupLabel.grid(row=3,column=0,padx=20,pady=9)
MakeupInput=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
MakeupInput.grid(row=3,column=1,padx=10,pady=9)
MakeupInput.insert(0,0)

SoinVisageLabel=Label(cosmeticsFrame,text='Soin Visage',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SoinVisageLabel.grid(row=4,column=0,padx=20,pady=9)
SoinVisageInput=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
SoinVisageInput.grid(row=4,column=1,padx=10,pady=9)
SoinVisageInput.insert(0,0)

VernisLabel=Label(cosmeticsFrame,text='Vernis',font=('times new roman',15,'bold'),bg='gray20',fg='white')
VernisLabel.grid(row=5,column=0,padx=20,pady=9)
VernisInput=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
VernisInput.grid(row=5,column=1,padx=10,pady=9)
VernisInput.insert(0,0)



AlimentsFrame=LabelFrame(productsFrame,text="Produits Alimentaires",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
AlimentsFrame.grid(row=0,column=1)

LegumesLabel=Label(AlimentsFrame,text='Legumes',font=('times new roman',15,'bold'),bg='gray20',fg='white')
LegumesLabel.grid(row=0,column=0,padx=20,pady=9)
LegumesInput=Entry(AlimentsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
LegumesInput.grid(row=0,column=1,padx=10,pady=9)
LegumesInput.insert(0,0)

FruitsLabel=Label(AlimentsFrame,text='Fruits',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FruitsLabel.grid(row=1,column=0,padx=20,pady=9)
FruitsInput=Entry(AlimentsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
FruitsInput.grid(row=1,column=1,padx=10,pady=9)
FruitsInput.insert(0,0)

PatesLabel=Label(AlimentsFrame,text='Pates',font=('times new roman',15,'bold'),bg='gray20',fg='white')
PatesLabel.grid(row=2,column=0,padx=20,pady=9)
PatesInput=Entry(AlimentsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
PatesInput.grid(row=2,column=1,padx=10,pady=9)
PatesInput.insert(0,0)

OilLabel=Label(AlimentsFrame,text='Huile',font=('times new roman',15,'bold'),bg='gray20',fg='white')
OilLabel.grid(row=3,column=0,padx=20,pady=9)
OilInput=Entry(AlimentsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
OilInput.grid(row=3,column=1,padx=10,pady=9)
OilInput.insert(0,0)

EpiceLabel=Label(AlimentsFrame,text='Epices',font=('times new roman',15,'bold'),bg='gray20',fg='white')
EpiceLabel.grid(row=4,column=0,padx=20,pady=9)
EpiceInput=Entry(AlimentsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
EpiceInput.grid(row=4,column=1,padx=10,pady=9)
EpiceInput.insert(0,0)

ViandeLabel=Label(AlimentsFrame,text='Viandes',font=('times new roman',15,'bold'),bg='gray20',fg='white')
ViandeLabel.grid(row=5,column=0,padx=20,pady=9)
ViandeInput=Entry(AlimentsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
ViandeInput.grid(row=5,column=1,padx=10,pady=9)
ViandeInput.insert(0,0)

DrinksFrame=LabelFrame(productsFrame,text="Boissons",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
DrinksFrame.grid(row=0,column=2)

WaterLabel=Label(DrinksFrame,text='Eau',font=('times new roman',15,'bold'),bg='gray20',fg='white')
WaterLabel.grid(row=0,column=0,padx=20,pady=9)
WaterInput=Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
WaterInput.grid(row=0,column=1,padx=10,pady=9)
WaterInput.insert(0,0)


SodaLabel=Label(DrinksFrame,text='Soda',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SodaLabel.grid(row=1,column=0,padx=20,pady=9)
SodaInput=Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
SodaInput.grid(row=1,column=1,padx=10,pady=9)
SodaInput.insert(0,0)


AlcoolLabel=Label(DrinksFrame,text='Alcool',font=('times new roman',15,'bold'),bg='gray20',fg='white')
AlcoolLabel.grid(row=2,column=0,padx=20,pady=9)
AlcoolInput=Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
AlcoolInput.grid(row=2,column=1,padx=10,pady=9)
AlcoolInput.insert(0,0)


JusLabel=Label(DrinksFrame,text='Jus',font=('times new roman',15,'bold'),bg='gray20',fg='white')
JusLabel.grid(row=3,column=0,padx=20,pady=9)
JusInput=Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
JusInput.grid(row=3,column=1,padx=10,pady=9)
JusInput.insert(0,0)


MilkLabel=Label(DrinksFrame,text='Lait',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MilkLabel.grid(row=4,column=0,padx=20,pady=9)
MilkInput=Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
MilkInput.grid(row=4,column=1,padx=10,pady=9)
MilkInput.insert(0,0)


SiropLabel=Label(DrinksFrame,text='Sirop',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SiropLabel.grid(row=5,column=0,padx=20,pady=9)
SiropInput=Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
SiropInput.grid(row=5,column=1,padx=10,pady=9)
SiropInput.insert(0,0)


BillFrame=Frame(productsFrame,bd=8,relief=GROOVE)
BillFrame.grid(row=0,column=3,padx=10)

BillAreaLabel = Label(BillFrame,text='Facture',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
BillAreaLabel.pack(fill=X)
scrollbar=Scrollbar(BillFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
#connect the scroll bar with the text area
textArea = Text(BillFrame,height=18,width=64,yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.config(command=textArea.yview)

#add the fourth frame :
BillmenuFrame=LabelFrame(root,text="Menu",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
BillmenuFrame.pack()

CosmeticsPrice=Label(BillmenuFrame,text='Cosmetiques Total',font=('times new roman',15,'bold'),bg='gray20',fg='white')
CosmeticsPrice.grid(row=0,column=0,padx=20,pady=9)
CosmeticsPriceInput=Entry(BillmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
CosmeticsPriceInput.grid(row=0,column=1,padx=10,pady=9)

AlimentPrice=Label(BillmenuFrame,text='Aliments Total',font=('times new roman',15,'bold'),bg='gray20',fg='white')
AlimentPrice.grid(row=1,column=0,padx=20,pady=9)
AlimentPriceInput=Entry(BillmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
AlimentPriceInput.grid(row=1,column=1,padx=10,pady=9)

DrinksPrice=Label(BillmenuFrame,text='Boissons Total',font=('times new roman',15,'bold'),bg='gray20',fg='white')
DrinksPrice.grid(row=2,column=0,padx=20,pady=9)
DrinkPriceInput=Entry(BillmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
DrinkPriceInput.grid(row=2,column=1,padx=10,pady=9)

CosmeticsTaxes=Label(BillmenuFrame,text='Cosmetiques Taxes',font=('times new roman',15,'bold'),bg='gray20',fg='white')
CosmeticsTaxes.grid(row=0,column=2,padx=20,pady=9)
CosmeticsTaxesInput=Entry(BillmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
CosmeticsTaxesInput.grid(row=0,column=3,padx=10,pady=9)

AlimentTaxes=Label(BillmenuFrame,text='Aliments Taxes',font=('times new roman',15,'bold'),bg='gray20',fg='white')
AlimentTaxes.grid(row=1,column=2,padx=20,pady=9)
AlimentTaxesInput=Entry(BillmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
AlimentTaxesInput.grid(row=1,column=3,padx=10,pady=9)

DrinksTaxes=Label(BillmenuFrame,text='Boissons Taxes',font=('times new roman',15,'bold'),bg='gray20',fg='white')
DrinksTaxes.grid(row=2,column=2,padx=20,pady=9)
DrinkTaxesInput=Entry(BillmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
DrinkTaxesInput.grid(row=2,column=3,padx=10,pady=9)

ButtonFrame=Frame(BillmenuFrame,bd=8,relief=GROOVE)
ButtonFrame.grid(row=0,column=4,rowspan=3)

TotalButton=Button(ButtonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
TotalButton.grid(row=0,column=0,pady=20,padx=5)

BillButton=Button(ButtonFrame,text='Facture',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10 ,command=Bill)
BillButton.grid(row=0,column=1,pady=20,padx=5)

EmailButton=Button(ButtonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=email)
EmailButton.grid(row=0,column=2,pady=20,padx=5)

PrintButton=Button(ButtonFrame,text='Imprimer',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print)
PrintButton.grid(row=0,column=3,pady=20,padx=5)

ClearButton=Button(ButtonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
ClearButton.grid(row=0,column=4,pady=20,padx=5)




#to display the label at the top:
headingLabel.pack()



# display our window
root.mainloop()