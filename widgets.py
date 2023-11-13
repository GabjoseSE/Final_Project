import tkinter as tk
from tkinter import ttk

class BudgetWidgets:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def budget_widgets(self):
        tk.Label(self.master, text="Enter Budget:", fg='blue').grid(row=0, column=0, sticky=tk.W)
        tk.Entry(self.master, textvariable=self.app.budget, width=15).grid(row=0, column=1)
        tk.Button(self.master, text="Set Budget", bg="green", fg="white", command=self.app.set_budget).grid(row=0, column=2)

    def product_entry_widgets(self):
        tk.Label(self.master, text="Product Name:", fg='blue').grid(row=1, column=0, sticky=tk.W)
        tk.Entry(self.master, textvariable=self.app.product_name, width=15).grid(row=1, column=1)
        tk.Label(self.master, text="Product Price:", fg='blue').grid(row=2, column=0, sticky=tk.W)
        tk.Entry(self.master, textvariable=self.app.product_price, width=15).grid(row=2, column=1)
        tk.Button(self.master, text="Add Product", command=self.app.add_product).grid(row=2, column=2)

    def product_list_widgets(self):
        self.app.product_tree = ttk.Treeview(self.master, columns=('Product Name', 'Product Price'), show='headings')
        self.app.product_tree.heading('Product Name', text='Product Name')
        self.app.product_tree.heading('Product Price', text='Product Price')
        self.app.product_tree.grid(row=3, column=0, columnspan=3, sticky='nsew')

    def list_operation_widgets(self):
        tk.Button(self.master, text="Update List ",fg="white", bg="#c5af00", command=self.app.update_list).grid(row=4, column=1, columnspan=3)
        tk.Button(self.master, text="Delete Item",fg="white", bg="#c9382c", command=self.app.delete_item).grid(row=4, column=2, columnspan=3)

    def remaining_budget_widgets(self):
        tk.Label(self.master, text="Remaining Budget:", fg='blue').grid(row=5, column=0, sticky=tk.W)
        tk.Label(self.master, textvariable=self.app.remaining_budget, fg='black', font="arial").grid(row=5, column=1)

    def save_to_excel_widget(self):
        tk.Button(self.master, text="Save to Excel ", fg="White", bg="#425a2a", command=self.app.save_to_excel).grid(row=4, column=0, columnspan=3)
    
    def clear_entry(self):
        tk.Button(self.master, text="Clear Entry").grid(row= 4, column=3, columnspan=3)
