def convert_tk_col_to_rgb(tk_color, tk_controller):  # tk_controller = tk.Tk()
    return tuple(c // 256 for c in tk_controller.winfo_rgb(color=tk_color))  # Needs the controller unfortunately
