# widgets.py
import tkinter as tk
from tkinter import ttk

class BudgetWidgets:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def create_budget_widgets(self):
        tk.Label(self.master, text="Enter Budget:", fg='blue').grid(row=0, column=0, sticky=tk.W)
        tk.Entry(self.master, textvariable=self.app.budget, width=15).grid(row=0, column=1)
        tk.Button(self.master, text="Set Budget", bg="green", fg="white", command=self.app.set_budget).grid(row=0, column=2)

    def create_product_entry_widgets(self):
        tk.Label(self.master, text="Product Name:", fg='blue').grid(row=1, column=0, sticky=tk.W)
        tk.Entry(self.master, textvariable=self.app.product_name, width=15).grid(row=1, column=1)
        tk.Label(self.master, text="Product Price:", fg='blue').grid(row=2, column=0, sticky=tk.W)
        tk.Entry(self.master, textvariable=self.app.product_price, width=15).grid(row=2, column=1)
        tk.Button(self.master, text="Add Product", command=self.app.add_product).grid(row=2, column=2)

    def create_product_list_widgets(self):
        self.app.product_tree = ttk.Treeview(self.master, columns=('Product Name', 'Product Price'), show='headings')
        self.app.product_tree.heading('Product Name', text='Product Name')
        self.app.product_tree.heading('Product Price', text='Product Price')
        self.app.product_tree.grid(row=3, column=0, columnspan=3, sticky='nsew')

    def create_list_operation_widgets(self):
        tk.Button(self.master, text="Update List ", command=self.app.update_list).grid(row=4, column=1, columnspan=3)
        tk.Button(self.master, text="Delete Item", command=self.app.delete_item).grid(row=4, column=2, columnspan=3)

    def create_remaining_budget_widgets(self):
        tk.Label(self.master, text="Remaining Budget:", fg='blue').grid(row=5, column=0, sticky=tk.W)
        tk.Label(self.master, textvariable=self.app.remaining_budget, fg='green', font="arial").grid(row=5, column=1)

    def create_save_to_excel_widget(self):
        tk.Button(self.master, text="Save to Excel ", command=self.app.save_to_excel).grid(row=4, column=0, columnspan=3)
