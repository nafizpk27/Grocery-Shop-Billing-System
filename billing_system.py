from tkinter import *
from tkinter import Label

import random

class Bill_App:
    def __init__(self, root):  # Fixed method name
        self.root = root 
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(1280, 700)
        self.root.minsize(1280, 700)
        self.root.title("Grocery Billing System")

        #===============================Variable===============================#

        self.cus_name =StringVar()
        self.c_phone = StringVar()
        #For Generating random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to Variable
        self.c_bill_no.set(str(x))


        self.bread = IntVar()
        self.candy = IntVar()
        self.hamburger = IntVar()
        self.hotdog = IntVar()
        self.sandwich = IntVar()
        self.rice = IntVar()
        self.salt = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.gatorade = IntVar()
        self.coke = IntVar()
        self.juice = IntVar()
        self.waffer = IntVar()
        self.biscuits = IntVar()
        self.total_food = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()

        #============My Add=============#
        self.total = StringVar()
        self.bill_area = StringVar()
        self.clear = StringVar
        self.exit = StringVar()
        #===============================#


        #===============================================

        bg_color = "green"
        fg_color = "white"
        lbl_color = "white"

        #Total of App
        title = Label(self.root, text="Grocery Billing System",  bd = 12, relief =GROOVE, fg=fg_color, bg=bg_color, font=("times new roman", 30, "bold"), pady=3).pack(fill=X)
        title.pack(fill=X)

        #====================Customer Frame======================#
        F1 = LabelFrame(text="Customer Details", font=("times new roman", 12, "bold"), fg="gold", bg=bg_color, relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        #====================Customer Name=======================#
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color, font=("times new roman", 12, "bold"))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        #====================Customer Phone=====================#
        cphone_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold")).gird(row=0, column=2, padx=20)
        cphone_lbl.grid(row=0, column=2, padx=20)
        cphone_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphone_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        #====================Customer Bill No===================#
        cbill_lbl = Label(F1, text= "Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        #====================Food Frame=========================#
        F2= LabelFrame(self.root, text='Food', bd=10, relief=GROOVE, bg=bg_color, fg="gold", font= ("times new roman", 13, "bold"))
        F2.place(x=5, y=180, width=325, height=380)

        #====================Frame Content======================#
        bath_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Bread")
        bath_lbl.grid(row=0, column=0, padx=10, pady=20)
        bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.bread)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        #===================Candy===============================#
        face_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Candy")
        face_lbl.grid(row=1, column=0, padx=10, pady=20)
        face_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.candy)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)

        #===================Hamburger===========================#
        wash_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Hamburger")
        wash_lbl.grid(row=2, column=0, padx=10, pady=20)
        wash_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.hamburger)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

        #====================Hotdog=============================#
        hair_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Hotdog")
        hair_lbl.grid(row=3, column=0, padx=10, pady=20)
        hair_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.hotdog)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

        #====================Sandwich============================#
        lot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sandwich")
        lot_lbl.grid(row=4, column=0, padx=10, pady=20)
        lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.sandwich)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

        #====================Grocery Frame=======================#
        F2 = LabelFrame(self.root, text='Grocery', bd=10, relief=GROOVE, bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
        F2.place(x=330, y=180, width=325, height=380)

        #====================Frame Content=======================#
        rice_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rice")
        rice_lbl.grid(row=0, column=0, padx=10, pady=20)
        rice_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.rice)
        rice_en.grid(row=0, column=1, ipady=5, ipadx=5)       

        #=====================Food Oil===========================#
        oil_lbl = Label(F2, font= ("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Food Oil")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.food_oil)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        #=====================Salt===============================#
        daal_lbl = Label(F2, font= ("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Salt")
        daal_lbl.grid(row=2, column=0, padx=10, pady=20)
        daal_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.salt)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        #=====================Wheat===============================#
        wheat_lbl = Label(F2, font= ("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Wheat")
        wheat_lbl.grid(row=3, column=0, padx=10, pady=20)
        wheat_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.wheat)
        wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

        #=====================Sugar===============================#
        sugar_lbl = Label(F2, font= ("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sugar")
        sugar_lbl.grid(row=4, column=0, padx=10, pady=20)
        sugar_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.sugar)
        sugar_en.grid(row=4, column=1, ipady=5, ipadx=5)

        #==============================Other Stuff===============================#
        F2 = LabelFrame(self.root, text='Others', bd=10, relief=GROOVE, bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
        F2.place(x=655, y=180, width=325, height=380)

        #=====================Frame Content========================#
        maza_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Gatorade")
        maza_lbl.grid(row=0, column=0, padx=10, pady=20)
        maza_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.gatorade)
        maza_en.grid(row=0, column=1, ipady=5, ipadx=5)

        #=====================Coke=================================#
        cock_lbl = Label(F2, font= ("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coke")
        cock_lbl.grid(row=1, column=0, padx=10, pady=20)
        cock_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.coke)
        cock_en.grid(row=1, column=1, ipady=5, ipadx=5) 

        #=====================Juice================================#
        frooti_lbl = Label(F2, font= ("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Juice")
        frooti_lbl.grid(row=2, column=0, padx=10, pady=20)
        frooti_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.juice)
        frooti_en.grid(row=2, column=1, ipady=5, ipadx=5)

        #=====================Waffer===============================#
        cold_lbl = Label(F2, font= ("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Waffer")
        oil_lbl.grid(row=3, column=0, padx=10, pady=20)
        cold_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.waffer)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

        #=====================Biscuits=============================#
        bis_lbl = Label(F2, font= ("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Biscuits")
        bis_lbl.grid(row=4, column=0, padx=10, pady=20)
        bis_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.biscuits)
        bis_en.grid(row=4, column=1, ipady=5, ipadx=5)


        #=====================Bill Area============================#
        F3 = Label(self.root, bd=10, relief=GROOVE)
        F3.place(x=960, y=180, width=325, height=380)

        #=====================Title================================#
        bill_title = Label(F3, text="Bill List", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        #=====================Scroll===============================#
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        #=====================Buttons Frame========================#
        F4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold", font=("times new roman", 13, "bold"))
        F4.place(x=0, y=560, relwidth=1, relheight=145)

        #=====================Total Food===========================#
        cosm_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg= bg_color, text="Total Food")
        cosm_lbl.grid(row=0, column=0, padx=10, pady=0)
        cosm_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_food)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        #=====================Total Grocery=========================#
        gro_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg= bg_color, text="Total Grocery")
        gro_lbl.grid(row=1, column=0, padx=10, pady=5)
        gro_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_grocery)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5)

        #=====================Others Total==========================#
        oth_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg= bg_color, text="Others Total")
        oth_lbl.grid(row=2, column=0, padx=10, pady=5)
        oth_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_other)
        oth_en.grid(row=2, column=1, ipady=2, ipadx=5)

        #======================Food Tax=============================#
        cosmt_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg= bg_color, text="Food Tax")
        cosmt_lbl.grid(row=0, column=2, padx=30, pady=0)
        cosmt_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_cos)
        cosmt_en.grid(row=0, column=3, ipady=2, ipadx=5)

        #=====================Grocery Tax===========================#
        grot_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg= bg_color, text="Grocery Tax")
        grot_lbl.grid(row=1, column=2, padx=30, pady=5)
        grot_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_groc)
        grot_en.grid(row=1, column=3, ipady=2, ipadx=5)

        #=====================Others Tax=========================#
        otht_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg= bg_color, text="Others Tax")
        otht_lbl.grid(row=2, column=2, padx=10, pady=5)
        otht_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_other)
        otht_en.grid(row=2, column=3, ipady=2, ipadx=5)

        #=====================Total==============================#
        total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE, command=self.total)
        total_btn.grid(row=1, column=4, ipadx=20, padx=30)


        #=====================Bill==============================#
        genbill_btn = Button(F4, text="Genarate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=20,)


        #=====================Celar Button======================#
        clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE, command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=20, padx=30)


        #=====================Exit Button=======================#
        exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE, command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20,)


        #Fuction to get total price
    def total(self):
        #==============Total food Price=====================#
        self.total_food_prices = (
            (self.bread.get() *1) +
            (self.candy.get() *3) +
            (self.hamburger.get() *8) +
            (self.hotdog.get() *6) +
            (self.sandwich.get() *4)

        )
        self.total_food.set("$" + str(self.total_food_prices))
        self.tax_cos.set("$" + str(round(self.total_food_prices * 0.05)))
        #==============Total Grocery Price===================#
        self.total_grocery_prices = (
            (self.wheat.get() *1) +
            (self.food_oil.get() *5) +
            (self.salt.get() *1) +
            (self.rice.get() *3) +
            (self.sugar.get() *2)
        )
        self.total_grocery.set("$" + str(self.total_grocery_prices))
        self.tax_groc.set("$" + str(round(self.total_grocery_prices * 0.05)))
        #==============Total Other Price===================#
        self.total_other_prices = (
            (self.gatorade.get() *4) +
            (self.juice.get() *2) +
            (self.coke.get() *2) +
            (self.waffer.get() *2) +
            (self.biscuits.get() *2)
        )
        self.total_other.set("$" + str(self.total_other_prices))
        self.tax_other.set("$" + str(round(self.total_other_prices * 0.05)))


    #==============Function For Text Area==============#
    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "      Welcome To Store's Retail\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===============================================")
        self.txt.insert(END, "\nProduct        Qty         Price")
        self.txt.insert(END, "\n===============================================")
        


        #Function to clear the bill area

    def clear(self):
        self.txt.delete('1.0', END)

        #Add Product name, qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.bread.get() != 0:
            self.txt.insert(END, f"\nBread        {self.bread.get()}        {self.bread.get() *1}")
        if self.candy.get() != 0:
            self.txt.insert(END, f"\nCandy        {self.candy.get()}        {self.candy.get() *3}") 
        if self.hamburger.get() != 0:
            self.txt.insert(END, f"\nHamburger        {self.hamburger.get()}        {self.hamburger.get() *8}")
        if self.hotdog.get() != 0:
            self.txt.insert(END, f"\nHotdog        {self.hotdog.get()}        {self.hotdog.get() *6}")
        if self.sandwich.get() != 0:
            self.txt.insert(END, f"\nSandwich       {self.sandwich.get()}        {self.sandwich.get() *4}") 
        if self.wheat.get() != 0:
            self.txt.insert(END, f"\nWheat        {self.wheat.get()}        {self.wheat.get() *1}") 
        if self.food_oil.get() != 0:
            self.txt.insert(END, f"\nFood Oil        {self.food_oil.get()}        {self.food_oil.get() *5}")
        if self.salt.get() != 0:
            self.txt.insert(END, f"\nSalt        {self.salt.get()}        {self.salt.get() *1}") 
        if self.rice.get() != 0:
            self.txt.insert(END, f"\nRice        {self.rice.get()}        {self.rice.get() *3}") 
        if self.sugar.get() != 0:
            self.txt.insert(END, f"\nSugar        {self.sugar.get()}        {self.sugar.get() *2}")  
        if self.gatorade.get() != 0:
            self.txt.insert(END, f"\nGatorade        {self.gatorade.get()}        {self.gatorade.get() *4}") 
        if self.juice.get() != 0:
            self.txt.insert(END, f"\nJuice        {self.juice.get()}        {self.juice.get() *2}") 
        if self.coke.get() != 0:
            self.txt.insert(END, f"\nCoke        {self.coke.get()}        {self.coke.get() *2}")
        if self.waffer.get() != 0:
            self.txt.insert(END, f"\nWaffer        {self.waffer.get()}        {self.waffer.get() *2}")
        if self.biscuits.get() != 0:
            self.txt.insert(END, f"\nBiscuits        {self.biscuits.get()}        {self.biscuits.get() *2}")
        self.txt.insert(END, "\n=======================================================")
        self.txt.insert(END, f"\n Total : ${self.total_food_prices + self.total_grocery_prices + self.total_other_prices + self.total_food_prices*0.05 + self.total_grocery_prices*0.05 + self.total_other_prices*0.05}")



    def exit(self):
        self.root.destroy()

root = Tk()
object = Bill_App(root)
root.mainloop()            
