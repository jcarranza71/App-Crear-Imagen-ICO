
# Convertidor de Imágenes a Ícono (.ico) – GUI

Aplicación gráfica para Windows (Python) que convierte imágenes comunes (PNG, JPG, BMP, etc.) en archivos `.ico` personalizables. ¡Ideal para crear iconos de accesos directos, apps o webs de forma visual y sencilla!

---

## Características

- Interfaz gráfica fácil e intuitiva (Tkinter).
- Soporta PNG, JPG, BMP, GIF...
- Previsualización de la imagen antes de convertir.
- Permite elegir el tamaño del icono.
- Permite personalizar el nombre y la carpeta de guardado.
- Botón “Cerrar” para salir cómodamente.
- No necesitas conocimientos de consola.

---

## Requisitos

- Python 3.7 o superior (Tkinter ya viene incluido).
- [Pillow](https://pypi.org/project/Pillow/)

Instala la dependencia así:

```bash
pip install pillow
```

---

## Uso con Python

1. Ejecuta el script `crear_ico_gui.py`:

    ```bash
    python crear_ico_gui.py
    ```

2. Haz clic en **“Seleccionar imagen”** para elegir la imagen que quieres convertir.
3. (Opcional) Modifica el tamaño o el nombre del archivo de salida.
4. Haz clic en **“Guardar como…”** para elegir dónde guardar el archivo `.ico`.
5. ¡Listo! Se mostrará un mensaje de éxito y tu icono estará creado.

---

## Uso del Ejecutable (.exe)

Si ya tienes el ejecutable generado (`crear_ico_gui.exe`):

1. **Haz doble clic** sobre el archivo `crear_ico_gui.exe` para abrir la aplicación.  
   *(No necesitas instalar Python ni ninguna otra dependencia)*

2. Utiliza la interfaz:
   - Pulsa **“Seleccionar imagen”** para elegir tu imagen (PNG, JPG, BMP, GIF...).
   - (Opcional) Ajusta el tamaño y el nombre del archivo de salida.
   - Pulsa **“Guardar como…”** para elegir la carpeta y el nombre del archivo `.ico`.
   - Pulsa **“Cerrar”** si deseas salir.

3. ¡Tu icono estará listo en la carpeta que elegiste!

---

## Crear tu propio ejecutable (.exe) para Windows

Si quieres crear el ejecutable desde el código fuente, instala [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=app.ico crear_ico_gui.py
```

El ejecutable estará en la carpeta `dist/`.

---

## Autor

**JESÚS ENRIQUE CARRANZA GONZÁLEZ**

¿Ideas, dudas o mejoras? ¡Escribe o haz un fork!
