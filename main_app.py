import tkinter as tk
from widgets import BudgetWidgets
from functions import BudgetFunctions

class BudgetTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("iBudget")
        self.master.geometry("400x400")

        # Variables
        self.budget = tk.DoubleVar()
        self.remaining_budget = tk.DoubleVar()
        self.product_name = tk.StringVar()
        self.product_price = tk.DoubleVar()

        # UI Widgets
        self.ui_widgets = BudgetWidgets(master, self)
        self.ui_widgets.budget_widgets()
        self.ui_widgets.product_entry_widgets()
        self.ui_widgets.product_list_widgets()
        self.ui_widgets.list_operation_widgets()
        self.ui_widgets.remaining_budget_widgets()
        self.ui_widgets.save_to_excel_widget()

        # Functions
        self.budget_functions = BudgetFunctions(self)  
    def set_budget(self):
        self.budget_functions.set_budget()

    def add_product(self):
        self.budget_functions.add_product()

    def update_list(self):
        self.budget_functions.update_list()

    def delete_item(self):
        self.budget_functions.delete_item()

    def save_to_excel(self):
        self.budget_functions.save_to_excel()

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTrackerApp(root)
    root.mainloop()
