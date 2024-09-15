# gui -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# untuk menampilkan guinya
window = tk.Tk()

window.configure(bg='white')
window.geometry('300x200')
window.resizable()
window.title('Sapa dia..!')

# variabel dan fungsi
nama_depan = tk.StringVar()
nama_belakang = tk.StringVar()


def klik():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f'halo {NamaDepan.get()} {NamaBelakang.get()}, Ganteng'
    showinfo(title='haloo', message=pesan)


# frame input
InputFrame = ttk.Frame(window)

# penempatan grid, pack, place
InputFrame.pack(padx=10, pady=10, fill='x', expand=True)

# komponen-komponen
# 1. label nama depan
NamaDepanLabel = ttk.Label(InputFrame, text='Nama Depan :')
NamaDepanLabel.pack(padx=10, fill='x', expand=True)

# 2. entry nama depan
NamaDepan = ttk.Entry(InputFrame, textvariable=nama_depan)
NamaDepan.pack(padx=10, fill='x', expand=True)

# 3. label nama belakang
NamaBelakangLebel = ttk.Label(InputFrame, text='Nama Belakang')
NamaBelakangLebel.pack(padx=10, fill='x', expand=True)

# 4. entry nama belakang
NamaBelakang = ttk.Entry(InputFrame, textvariable=nama_belakang)
NamaBelakang.pack(padx=10, fill='x', expand=True)

# 5. tombol
tombol = ttk.Button(InputFrame, text='sapa..!', command=klik)
tombol.pack(fill='x', expand=True, padx='10', pady='10')

window.mainloop()
