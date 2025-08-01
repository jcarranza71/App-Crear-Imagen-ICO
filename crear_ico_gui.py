import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os, sys

BG_COLOR      = "#F3F7F7"
BTN_COLOR     = "#20B2AA"
BTN_COLOR_HOV = "#159187"
BTN_TEXT      = "white"
LABEL_COLOR   = "#374151"
FONT_TITLE    = ("Segoe UI", 16, "bold")
FONT_NORMAL   = ("Segoe UI", 11)
FONT_SMALL    = ("Segoe UI", 9)

class IconConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Convertidor de Imágenes a Icono (.ico)")
        master.configure(bg=BG_COLOR)
        master.resizable(False, False)
        self.center_window(400, 540)
        self.imagen_path = None
        self.img_preview = None

        # Título
        tk.Label(master, text="Convertidor a Ícono (.ico)", font=FONT_TITLE, bg=BG_COLOR, fg="#0C6168").pack(pady=(14, 4))

        # Botón para seleccionar imagen
        self.btn_select_img = tk.Button(master, text="Seleccionar imagen", font=FONT_NORMAL, bg=BTN_COLOR, fg=BTN_TEXT,
                                        activebackground=BTN_COLOR_HOV, activeforeground=BTN_TEXT, cursor="hand2",
                                        relief="flat", command=self.seleccionar_imagen)
        self.btn_select_img.pack(pady=5, ipadx=8, ipady=2)
        self.btn_select_img.bind("<Enter>", lambda e: self.btn_select_img.config(bg=BTN_COLOR_HOV))
        self.btn_select_img.bind("<Leave>", lambda e: self.btn_select_img.config(bg=BTN_COLOR))

        # Canvas de previsualización
        self.frame_canvas = tk.Frame(master, bg=BG_COLOR, bd=2, relief="groove")
        self.frame_canvas.pack(pady=10)
        self.canvas = tk.Canvas(self.frame_canvas, width=180, height=180, bg="#F7F9FA", bd=0, highlightthickness=0)
        self.canvas.pack()

        # Etiqueta de ruta
        self.lbl_img = tk.Label(master, text="", font=FONT_SMALL, fg=LABEL_COLOR, bg=BG_COLOR)
        self.lbl_img.pack()

        # Campo para tamaño
        frm_size = tk.Frame(master, bg=BG_COLOR)
        frm_size.pack(pady=8)
        tk.Label(frm_size, text="Tamaño del icono:", font=FONT_NORMAL, bg=BG_COLOR, fg=LABEL_COLOR).pack(side=tk.LEFT)
        self.size_var = tk.IntVar(value=200)
        self.entry_size = tk.Entry(frm_size, textvariable=self.size_var, width=5, font=FONT_NORMAL, justify="center")
        self.entry_size.pack(side=tk.LEFT, padx=(5, 0))

        # Campo para nombre de fichero de salida
        frm_out = tk.Frame(master, bg=BG_COLOR)
        frm_out.pack(pady=8)
        tk.Label(frm_out, text="Nombre del archivo de salida:", font=FONT_NORMAL, bg=BG_COLOR, fg=LABEL_COLOR).pack(side=tk.LEFT)
        self.output_name_var = tk.StringVar()
        self.entry_output = tk.Entry(frm_out, textvariable=self.output_name_var, width=22, font=FONT_NORMAL)
        self.entry_output.pack(side=tk.LEFT, padx=(5, 0))

        # Botón para elegir ubicación y nombre del archivo Y convertir
        self.btn_saveas = tk.Button(master, text="Guardar como...", font=FONT_NORMAL, bg=BTN_COLOR, fg=BTN_TEXT,
                                   activebackground=BTN_COLOR_HOV, activeforeground=BTN_TEXT, cursor="hand2",
                                   relief="flat", command=self.guardar_y_convertir)
        self.btn_saveas.pack(pady=16, ipadx=10, ipady=3)
        self.btn_saveas.bind("<Enter>", lambda e: self.btn_saveas.config(bg=BTN_COLOR_HOV))
        self.btn_saveas.bind("<Leave>", lambda e: self.btn_saveas.config(bg=BTN_COLOR))

        # Botón para cerrar la aplicación
        self.btn_close = tk.Button(master, text="Cerrar", font=FONT_NORMAL, bg="#E3746D", fg="white",
                                   activebackground="#A64740", activeforeground="white", cursor="hand2",
                                   relief="flat", command=master.destroy)
        self.btn_close.pack(pady=(10, 18), ipadx=14, ipady=3)
        self.btn_close.bind("<Enter>", lambda e: self.btn_close.config(bg="#A64740"))
        self.btn_close.bind("<Leave>", lambda e: self.btn_close.config(bg="#E3746D"))

    def center_window(self, width, height):
        self.master.update_idletasks()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def seleccionar_imagen(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if filepath:
            self.imagen_path = filepath
            self.lbl_img.config(text=os.path.basename(filepath))
            self.mostrar_previsualizacion(filepath)
            # Poner nombre de salida por defecto
            base = os.path.splitext(os.path.basename(filepath))[0]
            self.output_name_var.set(base + ".ico")

    def mostrar_previsualizacion(self, filepath):
        self.canvas.delete("all")
        img = Image.open(filepath)
        img.thumbnail((170, 170))
        self.img_preview = ImageTk.PhotoImage(img)
        self.canvas.create_image(90, 90, image=self.img_preview)

    def guardar_y_convertir(self):
        if not self.imagen_path:
            messagebox.showerror("Error", "¡Debes seleccionar una imagen primero!")
            return
        default_name = self.output_name_var.get() or "icono.ico"
        initial_dir = os.path.dirname(sys.argv[0])
        filetypes = [("Icono Windows", "*.ico")]
        path = filedialog.asksaveasfilename(
            initialdir=initial_dir,
            initialfile=default_name,
            defaultextension=".ico",
            filetypes=filetypes
        )
        if path:
            try:
                size = int(self.size_var.get())
                img = Image.open(self.imagen_path)
                img = img.resize((size, size), Image.LANCZOS)
                img.save(path, format="ICO")
                messagebox.showinfo("Éxito", f"¡Icono creado con éxito!\n{path}")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = IconConverterApp(root)
    root.mainloop()
