import tkinter as tk
from tkinterdnd2 import DND_FILES  # https://pypi.org/project/tkinterdnd2/
from typing import Optional, Callable


class DnDFileLabel(tk.Label):
    def __init__(self, *args, on_drag_enter: Optional[Callable] = None, on_drag_leave: Optional[Callable] = None,
                 on_drop: Optional[Callable] = None, **kwargs):
        super().__init__(*args, **kwargs)

        self.drop_target_register(DND_FILES)

        if on_drag_enter:
            self.dnd_bind('<<DropEnter>>', on_drag_enter)
        if on_drag_leave:
            self.dnd_bind('<<DropLeave>>', on_drag_leave)
        if on_drop:
            self.dnd_bind('<<Drop>>', on_drop)