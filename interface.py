from tkinter import *
from PIL import Image, ImageTk
import requests
import pandas as pd
from dateutil.parser import ParserError
from connection import link
from tkinter import messagebox
import webbrowser
def compare():
    comparewindow=Toplevel()
    comparewindow.title('Compare')



    def compare_currencies():
        currency1 = entry_currency1.get()
        
        currency2 = entry_currency2.get()
        
        bool1=False
        bool2=False
        comparison_message=""
        

        if not currency1 or not currency2:
            messagebox.showinfo('Error', 'Please enter two different currency names for comparison.')
        elif currency1 == currency2:
            messagebox.showinfo('Error', 'Please enter two different currency names for comparison.')
        else:
            try:
                for index,row in df.iterrows():
                    #for all information in cursor, look for the information that the user clicked on and put in in the boxes
                    
                    if currency1==(row['name']):
                        #using the rows to recieve info
                        currency1name=row['name']
                        currency1_id=row['id']
                        currency1_symbol=row['symbol']
                        price_value = row['quote'].get('NOK', {}).get('price', 'N/A')
                        currency1_pricevar = f"{float(price_value):.6f} NOK"
                        bool1=True
                
                for index,row in df.iterrows():
                    #for all information in cursor, look for the information that the user clicked on and put in in the boxes
                    
                    if currency2==(row['name']):
                        #using the rows to recieve info
                        currency2name=row['name']
                        currency2_id=row['id']
                        currency2_symbol=row['symbol']
                        price_value2 = row['quote'].get('NOK', {}).get('price', 'N/A')
                        currency2_pricevar = f"{float(price_value2):.6f} NOK"
                        bool2=True
            
            
                        
                
                
                if bool1 and bool2:
                
                    comparison_message = (
                        f'Comparison between {currency1} and {currency2}:\n\n'
                        f'{currency1}:\n'
                        f'Name: {currency1name}\n'
                        f'ID: {currency1_id}\n'
                        f'Symbol: {currency1_symbol}\n'
                        f'Price: {currency1_pricevar}\n\n'
                        f'{currency2}:\n'
                        f'Name: {currency2name}\n'
                        f'ID: {currency2_id}\n'
                        f'Symbol: {currency2_symbol}\n'
                        f'Price: {currency2_pricevar}'
                    )
                    messagebox.showinfo('Currency Comparison', comparison_message)
                elif bool1==False and bool2==True:
                    messagebox.showinfo('Error','Currency nr 1 do not exist \n Make sure your currency exists and that you have \n written it correctly')

                     
                elif bool1==True and bool2==False:
                    messagebox.showinfo('Error','Currency nr 2 do not exist \n Make sure your currency exists and that you have \n written it correctly')

                
                else:
                     messagebox.showinfo('Error','Both of the cryptocurrencies do not exist \n Make sure your currency exists and that you have \n written it correctly')


                
            except KeyError:
                messagebox.showinfo('Error', 'Invalid currency name. Please enter valid currency names.')
        entry_currency1.delete(0, 'end')
        entry_currency2.delete(0, 'end')
    # Create the main window

    # Create and place widgets in comparewindow
    label_currency1 = Label(comparewindow, text='Currency 1:')
    label_currency1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    entry_currency1 = Entry(comparewindow)
    entry_currency1.grid(row=0, column=1, padx=10, pady=10)

    label_currency2 = Label(comparewindow, text='Currency 2:')
    label_currency2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    entry_currency2 = Entry(comparewindow)
    entry_currency2.grid(row=1, column=1, padx=10, pady=10)

    btn_compare = Button(comparewindow, text='Compare', command=compare_currencies)
    btn_compare.grid(row=2, column=0, columnspan=2, pady=10)

    # Start the Tkinter event loop for comparewindow
    comparewindow.mainloop()




def view():
    viewwindow=Toplevel()
    viewwindow.title('View')
    
    
    
    

    def windowevent(event):
    
        
        if df is not None and lst_names.curselection():
            chosen=lst_names.get(lst_names.curselection())
            print (chosen)
        
            for index,row in df.iterrows():
                #for all information in cursor, look for the information that the user clicked on and put in in the boxes
                print (row['name'])
                print (chosen)
                if chosen==(row['name']):
                    #using the rows to recieve info
                    name.set(row['name'])
                    id.set(row['id'])
                    symbol.set(row['symbol'])
                    price_value = row['quote'].get('NOK', {}).get('price', 'N/A')
                    pricevar = f"{float(price_value):.6f} NOK"

        
                    price.set(pricevar)

    def reset(event=None):
        names = []

        for row in df['name']:
            names += [row]
        list_names.set(tuple(names))
        name.set('')
        id.set('')
        symbol.set('')
        price.set('')



    def searchdef(event):
        check=False
        if df is not None:
            chosen=search.get()
        
        
            for index,row in df.iterrows():
                #for all information in cursor, look for the information that the user clicked on and put in in the boxes
                
                if chosen==(row['name']):
                    foundlistvar=StringVar()
                    foundlist=[]
                    #using the rows to recieve info
                    name.set(row['name'])
                    id.set(row['id'])
                    symbol.set(row['symbol'])
                    price_value = row['quote'].get('NOK', {}).get('price', 'N/A')
                    pricevar = f"{float(price_value):.6f} NOK"
                    price.set(pricevar)
                    check=True
                    foundlist.append(row['name'])
                    lst_names=Listbox(viewwindow,width=25,height=10,listvariable=foundlistvar)
                    list_names.set(tuple(foundlist))
                    

        if check==False:
            message=f"The cryptocurrency {chosen} doesnt exist!\n Remember to spell correctly and beware of \n capital and special letters!!"
            messagebox.showinfo('Not Found',message)


    names=[]   
    
    for row in df['name']:
        names+=[row]
    list_names=StringVar()       
    lst_names=Listbox(viewwindow,width=25,height=10,listvariable=list_names)
    lst_names.grid(row=1,column=1,rowspan=2,pady=5,sticky=W)
    list_names.set(tuple(names))
    scrollbar = Scrollbar(viewwindow, orient="vertical", command=lst_names.yview)
    scrollbar.grid(row=1, column=2, rowspan=2, sticky="ns")

    # Configure the Listbox to use the scrollbar
    lst_names.configure(yscrollcommand=scrollbar.set)
    

    


    #stringvars
    


    name=StringVar()
    ent_pc=Entry(viewwindow,width=25,textvariable=name,state='readonly')
    ent_pc.grid(row=3,column=1,sticky=W)

    id=StringVar()
    ent_pc=Entry(viewwindow,width=25,textvariable=id,state='readonly')
    ent_pc.grid(row=4,column=1,sticky=W)

    price=StringVar()
    ent_location=Entry(viewwindow,width=25,textvariable=price,state='readonly')
    ent_location.grid(row=6,column=1,sticky=W)

    symbol=StringVar()
    ent_dato=Entry(viewwindow,width=20,textvariable=symbol,state='readonly')
    ent_dato.grid(row=5,column=1,sticky=W)

    #labels

    lbl_name=Label(viewwindow,text='Name: ')
    lbl_name.grid(row=3,column=0,sticky=W)
    #labels
    lbl_id=Label(viewwindow,text='ID: ')
    lbl_id.grid(row=4,column=0,sticky=W)

    lbl_symbol=Label(viewwindow,text='Symbol: ')
    lbl_symbol.grid(row=5,column=0,sticky=W)

    lbl_price=Label(viewwindow,text='Price: ')
    lbl_price.grid(row=6,column=0,sticky=W)

    lbl_location=Label(viewwindow,text='Currencies: ')
    lbl_location.grid(row=1,column=0,sticky=W)

    lbl_location=Label(viewwindow,text='Search: ')
    lbl_location.grid(row=8,column=0,sticky=W)


    #important as the event parameter

    lst_names.bind('<<ListboxSelect>>',windowevent)
    viewwindow.bind('<Return>', searchdef)
    
    search=StringVar()
    searchbar=Entry(viewwindow,width=25,textvariable=search)
    searchbar.grid(row=8,column=1,sticky=E)

    enter=Button(viewwindow, text ="Search",bg='green', command = searchdef)
    restart=Button (viewwindow, text ="Reset",bg='orange', command = reset)
    enter.grid(row=8,column=5,sticky=E,padx=5,pady=25)
    restart.grid(row=8,column=6,sticky=E,padx=5,pady=25)

    
    btn_avslut2=Button(viewwindow,text='Quit',bg='red',command=viewwindow.destroy)
    btn_avslut2.grid(row=8,column=7,padx=5,pady=25,sticky=E)




def about():
    aboutuswindow=Toplevel()
    aboutuswindow.title('About')
    title_label = Label(aboutuswindow, text="Welcome to my application!", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    about_us_text = """
    This application is designed to showcase and compare cryptocurrencies.
    It was created as a project for me to learn more about APIs. In this 
    application, i am working with the API of CoinMarketCap.
    I have also added some functions, in order for me to learn more about
    the world of programming.

    Version: 1.0
    Released: N/A

    Thank you for using my application!
    """


    label = Label(aboutuswindow, text=about_us_text, font=("Helvetica",13), padx=10, pady=10)
    label.pack()


def AI():
    comparewindow=Toplevel()
    comparewindow.title('ChatBot')
    about_us_text = """
    This function will be included in the next update!
    """


    label = Label(comparewindow, text=about_us_text,font=("Helvetica", 16, "bold"), padx=10, pady=10)
    label.pack()


def visit():
    webbrowser.open('https://github.com/lak1811')


root = Tk()
root.title("Menu")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Compare", command=compare)

filemenu.add_command(label="Show", command=view)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="View Currencies", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about)
helpmenu.add_command(label="Chat with us!", command=AI)
menubar.add_cascade(label="Help", menu=helpmenu)

visitmenu = Menu(menubar, tearoff=0)
visitmenu.add_command(label="Look at my other projects!", command=visit)
menubar.add_cascade(label="Visit", menu=visitmenu)
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'  

    # Define parameters and headers
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'NOK'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '282390ec-34c2-4ffd-8010-12d856686b67',
}

df=link(url,parameters,headers)

print (df)

img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.config(menu=menubar,background="#87CEEB")
root.mainloop()
