"""Tkinter user interface for the Caesar cipher."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from .cipher import decrypt, encrypt


class CaesarCipherApp:
    """Desktop application for encrypting and decrypting text."""

    DEFAULT_SHIFT = "3"
    WINDOW_SIZE = "650x550"

    def __init__(self, root: tk.Tk | None = None) -> None:
        self.root = root or tk.Tk()
        self.root.title("Caesar Cipher")
        self.root.geometry(self.WINDOW_SIZE)
        self.root.resizable(False, False)

        self.shift_var = tk.StringVar(value=self.DEFAULT_SHIFT)
        self.input_text: tk.Text
        self.output_text: tk.Text
        self._build_widgets()

    def run(self) -> None:
        """Start the Tkinter event loop."""
        self.root.mainloop()

    def _build_widgets(self) -> None:
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(
            main_frame,
            text="Caesar Cipher",
            font=("Arial", 22, "bold"),
        ).pack(pady=(0, 5))
        ttk.Label(
            main_frame,
            text="Encrypt and decrypt messages using a Caesar cipher.",
        ).pack(pady=(0, 20))

        self._build_text_area(main_frame, "Input Text:", "input")
        self._build_shift_selector(main_frame)
        self._build_action_buttons(main_frame)
        self._build_text_area(main_frame, "Output:", "output")

        ttk.Button(
            main_frame,
            text="Copy Output",
            command=self.copy_output,
        ).pack()

    def _build_text_area(
        self,
        parent: ttk.Frame,
        label: str,
        name: str,
    ) -> None:
        ttk.Label(
            parent,
            text=label,
            font=("Arial", 11, "bold"),
        ).pack(anchor="w")

        text_area = tk.Text(parent, height=8, width=70, wrap="word")
        text_area.pack(pady=(5, 15 if name == "input" else 10))

        if name == "input":
            self.input_text = text_area
        else:
            self.output_text = text_area

    def _build_shift_selector(self, parent: ttk.Frame) -> None:
        shift_frame = ttk.Frame(parent)
        shift_frame.pack(fill="x", pady=(0, 15))

        ttk.Label(
            shift_frame,
            text="Shift:",
            font=("Arial", 11, "bold"),
        ).pack(side="left")
        ttk.Spinbox(
            shift_frame,
            from_=1,
            to=25,
            textvariable=self.shift_var,
            width=5,
        ).pack(side="left", padx=10)

    def _build_action_buttons(self, parent: ttk.Frame) -> None:
        button_frame = ttk.Frame(parent)
        button_frame.pack(pady=(0, 15))

        ttk.Button(
            button_frame,
            text="Encrypt",
            command=lambda: self.process_text(encrypt),
        ).grid(row=0, column=0, padx=5)
        ttk.Button(
            button_frame,
            text="Decrypt",
            command=lambda: self.process_text(decrypt),
        ).grid(row=0, column=1, padx=5)
        ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_text,
        ).grid(row=0, column=2, padx=5)

    def process_text(self, operation) -> None:
        """Run an encryption/decryption operation from the form."""
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning(
                "Missing Text",
                "Please enter some text first.",
                parent=self.root,
            )
            return

        try:
            shift = int(self.shift_var.get())
            result = operation(text, shift)
        except (TypeError, ValueError) as error:
            messagebox.showerror("Invalid Shift", str(error), parent=self.root)
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

    def clear_text(self) -> None:
        """Clear both text areas."""
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def copy_output(self) -> None:
        """Copy output text to the system clipboard."""
        result = self.output_text.get("1.0", tk.END).strip()
        if not result:
            messagebox.showwarning(
                "Nothing to Copy",
                "There is no output to copy.",
                parent=self.root,
            )
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(result)
        messagebox.showinfo(
            "Copied",
            "Output copied to clipboard.",
            parent=self.root,
        )