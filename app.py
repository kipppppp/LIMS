import mysql.connector
import customtkinter as ctk


def db_connect():
    db = mysql.connector.connect(
      host="localhost",
      user="",
      password="",
      database=""
    )
    return db


class GUI:
    def __init__(self):
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.geometry("500x500")
        self.app.title("Inventory Management")

        self.tab = ctk.CTkTabview(self.app)
        self.tab.pack()

        self.tab_add_customer = self.tab.add("Add Customer")
        self.tab_add_reagent = self.tab.add("Add Reagent")

        # Customer entry boxes
        self.fname_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="First Name")
        self.fname_entry.grid(row=0, column=1)

        self.lname_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="Last Name")
        self.lname_entry.grid(row=1, column=1)

        self.org_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="Organization")
        self.org_entry.grid(row=2, column=1)

        self.email_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="Email")
        self.email_entry.grid(row=3, column=1)

        self.phone_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="000-000-0000")
        self.phone_entry.grid(row=4, column=1)

        self.notes_entry = ctk.CTkTextbox(self.tab_add_customer, height=90)
        self.notes_entry.grid(row=5, column=1)

        # Customer Labels
        self.fname_label = ctk.CTkLabel(self.tab_add_customer, text="First Name")
        self.fname_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        self.lname_label = ctk.CTkLabel(self.tab_add_customer, text="Last Name")
        self.lname_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.org_label = ctk.CTkLabel(self.tab_add_customer, text="Organization")
        self.org_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.email_label = ctk.CTkLabel(self.tab_add_customer, text="Email")
        self.email_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        self.phone_label = ctk.CTkLabel(self.tab_add_customer, text="Phone")
        self.phone_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        self.notes_label = ctk.CTkLabel(self.tab_add_customer, text="Notes")
        self.notes_label.grid(row=5, column=0, padx=10, pady=10, sticky='ne')

        self.submit_customer = ctk.CTkButton(self.tab_add_customer, text="Submit Customer Record", command=self.add_customer)
        self.submit_customer.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        # Reagent entry boxes
        self.reagent_name_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="Acetonitrile")
        self.reagent_name_entry.grid(row=0, column=1)

        self.standard_entry = ctk.CTkComboBox(self.tab_add_reagent, values=["Yes", "No"])
        self.standard_entry.grid(row=1, column=1)

        self.supplier_name_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="Honeywell")
        self.supplier_name_entry.grid(row=2, column=1)

        self.grade_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="HPLC")
        self.grade_entry.grid(row=3, column=1)

        self.concentration_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="98% Purity")
        self.concentration_entry.grid(row=4, column=1)

        self.received_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="yyyy-mm-dd")
        self.received_entry.grid(row=5, column=1)

        self.expiry_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="yyyy-mm-dd")
        self.expiry_entry.grid(row=6, column=1)

        # Reagent Labels
        self.reagent_name_label = ctk.CTkLabel(self.tab_add_reagent, text="Reagent Name")
        self.reagent_name_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        self.standard_label = ctk.CTkLabel(self.tab_add_reagent, text="Standard?")
        self.standard_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.supplier_label = ctk.CTkLabel(self.tab_add_reagent, text="Supplier")
        self.supplier_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.grade_label = ctk.CTkLabel(self.tab_add_reagent, text="Grade")
        self.grade_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        self.concentration_label = ctk.CTkLabel(self.tab_add_reagent, text="Concentration")
        self.concentration_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        self.received_label = ctk.CTkLabel(self.tab_add_reagent, text="Date Received")
        self.received_label.grid(row=5, column=0, padx=10, pady=10, sticky='e')

        self.expiry_label = ctk.CTkLabel(self.tab_add_reagent, text="Expiration")
        self.expiry_label.grid(row=6, column=0, padx=10, pady=10, sticky='e')

        self.submit_reagent = ctk.CTkButton(self.tab_add_reagent, text="Submit Reagent Record")
        self.submit_reagent.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        self.app.mainloop()

    def add_customer(self):
        db = db_connect()
        mycursor = db.cursor()

        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        org = self.org_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        add = """INSERT INTO customers(first_name, last_name, organization, email, phone) VALUES(%s, %s, %s, %s, %s)"""
        info = (fname, lname, org, email, phone)
        mycursor.execute(add, info)
        db.commit()

        mycursor.close()
        db.close()

        self.fname_entry.delete(0, 'end')
        self.lname_entry.delete(0, 'end')
        self.org_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')


GUI()
