# functions.py
from tkinter import messagebox
import pandas as pd

class BudgetFunctions:
    def __init__(self, app):
        self.app = app

    def set_budget(self):
        try:
            self.app.remaining_budget.set(self.app.budget.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid budget value. Please enter a valid number.")

    def add_product(self):
        try:
            product_name = self.app.product_name.get()
            product_price = self.app.product_price.get()

            if product_price > self.app.remaining_budget.get():
                messagebox.showerror("Error", "Product price exceeds remaining budget!")
            else:
                self.app.product_tree.insert('', 'end', values=(product_name, f"₱{product_price}"))
                self.app.remaining_budget.set(self.app.remaining_budget.get() - product_price)
        except ValueError:
            messagebox.showerror("Error", "Invalid product price. Please enter a valid number.")

    def update_list(self):
        selected_item = self.app.product_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item from the list to update.")
            return

        try:
            product_name = self.app.product_name.get()
            product_price = self.app.product_price.get()

            if product_price > self.app.remaining_budget.get():
                messagebox.showerror("Error", "Product price exceeds remaining budget!")
            else:
                self.app.product_tree.item(selected_item, values=(product_name, f"₱{product_price}"))
                messagebox.showinfo("Success", "List updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid product price. Please enter a valid number.")

    def delete_item(self):
        selected_item = self.app.product_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item from the list to delete.")
            return

        values = self.app.product_tree.item(selected_item, 'values')
        price = float(values[1].replace('₱', ''))
        self.app.remaining_budget.set(self.app.remaining_budget.get() + price)
        self.app.product_tree.delete(selected_item)
        messagebox.showinfo("Success", "Item deleted successfully.")

    def save_to_excel(self):
        try:
            data = {'Product Name': [], 'Product Price': []}

            for item in self.app.product_tree.get_children():
                values = self.app.product_tree.item(item, 'values')
                data['Product Name'].append(values[0])
                data['Product Price'].append(float(values[1].replace('₱', '')))

            df = pd.DataFrame(data)
            df.to_excel('budget_tracker_data.xlsx', index=False)
            messagebox.showinfo("Success", "Data saved to budget_tracker_data.xlsx")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
