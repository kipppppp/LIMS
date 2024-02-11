import mysql.connector
import customtkinter as ctk


def db_connect():
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="admin",
      database="testdb"
    )
    return db


class GUI:
    def __init__(self):
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.geometry("500x600")
        self.app.title("Inventory Management")

        self.tab = ctk.CTkTabview(self.app)
        self.tab.pack()

        self.tab_add_customer = self.tab.add("Add Customer")
        self.tab_add_reagent = self.tab.add("Add Reagent")

        self.customer_submit_frame = None
        self.create_customer_fields()
        self.create_reagent_fields()

    def create_customer_fields(self):
        """Draws all of the customer data entry labels and fields"""
        cur_row = 1
        # Customer entry boxes
        self.fname_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="First Name", border_color='grey')
        self.fname_entry.grid(row=cur_row, column=1)
        cur_row += 1

        self.lname_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="Last Name", border_color='grey')
        self.lname_entry.grid(row=cur_row, column=1)
        cur_row += 1

        self.org_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="Organization", border_color='grey')
        self.org_entry.grid(row=cur_row, column=1)
        cur_row += 1

        self.email_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="Email", border_color='grey')
        self.email_entry.grid(row=cur_row, column=1)
        cur_row += 1

        self.phone_entry = ctk.CTkEntry(self.tab_add_customer, placeholder_text="000-000-0000", border_color='grey')
        self.phone_entry.grid(row=cur_row, column=1)
        cur_row += 1

        self.notes_entry = ctk.CTkTextbox(self.tab_add_customer, height=90, border_color='grey')
        self.notes_entry.grid(row=cur_row, column=1)
        cur_row += 1

        # Customer Labels
        cur_row = 0
        self.required_label = ctk.CTkLabel(self.tab_add_customer, text="* Required fields")
        self.required_label.grid(row=cur_row, column=0, columnspan=2)
        cur_row += 1

        self.fname_label = ctk.CTkLabel(self.tab_add_customer, text="*First Name")
        self.fname_label.grid(row=cur_row, column=0, padx=10, pady=10, sticky='e')
        cur_row += 1

        self.lname_label = ctk.CTkLabel(self.tab_add_customer, text="*Last Name")
        self.lname_label.grid(row=cur_row, column=0, padx=10, pady=10, sticky='e')
        cur_row += 1

        self.org_label = ctk.CTkLabel(self.tab_add_customer, text="*Organization")
        self.org_label.grid(row=cur_row, column=0, padx=10, pady=10, sticky='e')
        cur_row += 1

        self.email_label = ctk.CTkLabel(self.tab_add_customer, text="*Email")
        self.email_label.grid(row=cur_row, column=0, padx=10, pady=10, sticky='e')
        cur_row += 1

        self.phone_label = ctk.CTkLabel(self.tab_add_customer, text="Phone")
        self.phone_label.grid(row=cur_row, column=0, padx=10, pady=10, sticky='e')
        cur_row += 1

        self.notes_label = ctk.CTkLabel(self.tab_add_customer, text="Notes")
        self.notes_label.grid(row=cur_row, column=0, padx=10, pady=10, sticky='ne')
        cur_row += 1

        self.submit_customer_btn = ctk.CTkButton(self.tab_add_customer, text="Submit Customer Record", command=self.add_customer)
        self.submit_customer_btn.grid(row=cur_row, column=0, columnspan=2, padx=10, pady=10)

    def create_reagent_fields(self):
        """Draws all of the reagent data entry labels and fields"""
        # Reagent entry boxes
        self.reagent_name_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="Acetonitrile", border_color='grey')
        self.reagent_name_entry.grid(row=0, column=1)

        self.standard_entry = ctk.CTkComboBox(self.tab_add_reagent, values=["Yes", "No"], border_color='grey')
        self.standard_entry.grid(row=1, column=1)

        self.supplier_name_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="Honeywell", border_color='grey')
        self.supplier_name_entry.grid(row=2, column=1)

        self.grade_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="HPLC", border_color='grey')
        self.grade_entry.grid(row=3, column=1)

        self.concentration_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="98% Purity", border_color='grey')
        self.concentration_entry.grid(row=4, column=1)

        self.received_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="yyyy-mm-dd", border_color='grey')
        self.received_entry.grid(row=5, column=1)

        self.expiry_entry = ctk.CTkEntry(self.tab_add_reagent, placeholder_text="yyyy-mm-dd", border_color='grey')
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

    def create_customer_submit_frame(self, cust_info, required_error=False, email_error=False, phone_error=False):
        """Creates a frame that informs the user of data entry errors, or displays an added record"""
        self.customer_submit_frame = ctk.CTkFrame(master=self.tab_add_customer, height=60)
        self.customer_submit_frame.grid(row=8, column=0, columnspan=2)
        cur_row = 0
        if required_error:
            self.required_check_label = ctk.CTkLabel(self.customer_submit_frame, text="Please complete *required fields", text_color='red')
            self.required_check_label.grid(row=cur_row, column=0, columnspan=2)
            cur_row += 1
        if email_error:
            self.email_check_label = ctk.CTkLabel(self.customer_submit_frame, text="Please enter a valid email", text_color='red')
            self.email_check_label.grid(row=cur_row, column=0, columnspan=2)
            cur_row += 1
        if phone_error:
            self.phone_check_label = ctk.CTkLabel(self.customer_submit_frame, text="Phone format must be: 000-000-0000", text_color='red')
            self.phone_check_label.grid(row=cur_row, column=0, columnspan=2)

        if cust_info is not None:
            self.added_customer_label = ctk.CTkLabel(self.customer_submit_frame, text=f"The following record was added to the database:\n{cust_info[0]} {cust_info[1]}, {cust_info[2]}, {cust_info[3]}")
            self.added_customer_label.grid(row=cur_row, column=0, columnspan=2)

    def add_customer(self):
        """Validates the form and attempts database addition"""
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        org = self.org_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        note = self.notes_entry.get("1.0", "end-1c")

        # Data validation
        validation_fail = False
        required_error = False
        email_error = False
        phone_error = False

        if fname == '':
            self.fname_entry.configure(border_color='red')
            validation_fail = True
            required_error = True
        else:
            self.fname_entry.configure(border_color='grey')

        if lname == '':
            self.lname_entry.configure(border_color='red')
            validation_fail = True
            required_error = True
        else:
            self.lname_entry.configure(border_color='grey')

        if org == '':
            self.org_entry.configure(border_color='red')
            validation_fail = True
            required_error = True
        else:
            self.org_entry.configure(border_color='grey')

        if "@" not in email or email == '':
            self.email_entry.configure(border_color='red')
            validation_fail = True
            email_error = True
        else:
            self.email_entry.configure(border_color='grey')

        if phone == '':
            pass
        elif len(phone) != 12 or phone[3] != '-' or phone[7] != '-':
            self.phone_entry.configure(border_color='red')
            validation_fail = True
            phone_error = True
        else:
            self.phone_entry.configure(border_color='grey')

        if validation_fail:
            if self.customer_submit_frame is not None:
                self.customer_submit_frame.destroy()
            self.create_customer_submit_frame(None, required_error, email_error, phone_error)
            return

        # Connect to db
        db = db_connect()
        mycursor = db.cursor()

        add = """INSERT INTO customers(fname, lname, org, email, phone, note) VALUES(%s, %s, %s, %s, %s, %s)"""
        info = (fname, lname, org, email, phone, note)
        mycursor.execute(add, info)
        db.commit()

        # Disconnect from db
        mycursor.close()
        db.close()

        # Refresh the window
        if self.customer_submit_frame is not None:
            self.customer_submit_frame.destroy()
        self.create_customer_fields()

        # Display added record
        self.create_customer_submit_frame([fname, lname, org, email])


GUI()
