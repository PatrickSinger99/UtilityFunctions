import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.bind_all("<Button-1>", self.clear_focus, add="+")  # `add='+'` keeps existing bindings intact

    def clear_focus(self, event):
        """Clear focus if clicked widget is not an input"""
        non_focusable = (tk.Frame, tk.Label, tk.Canvas, tk.Toplevel)  # Add types as needed
        widget = event.widget

        # Only clear focus if clicked widget is one of the non-focusable types
        if isinstance(widget, non_focusable):
            self.focus_set()
