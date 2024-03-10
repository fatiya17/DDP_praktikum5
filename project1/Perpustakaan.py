from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root = Tk()
root.configure(bg="grey")

conn = sqlite3.connect("Perpustakaan.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("DROP TABLE IF EXISTS LIBRARY")
    query = """
    CREATE TABLE LIBRARY(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        JUDUL TEXT NOT NULL,
        KATEGORI TEXT NOT NULL,
        NO_RAK TEXT NOT NULL,
        PENULIS TEXT,
        PENERBIT TEXT,
        TAHUN TEXT,
        STOK INT 
    )
    """
    cursor.execute(query)
    conn.commit()

def isFirst(table_name):
    # Membuat query SQL untuk menghitung jumlah tabel dengan nama tertentu
    query = '''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(table_name)
    # Menjalankan query menggunakan kursor
    cursor.execute(query)
    # Melakukan commit untuk menyimpan perubahan ke database
    conn.commit()
    # Mengambil hasil eksekusi query, yaitu jumlah tabel dengan nama tersebut
    # Memeriksa apakah jumlah tabel sama dengan 1
    if cursor.fetchone()[0] == 1:
        return False
    else:
        return True

def select_all():
    # Membuat query SQL untuk mengambil semua data dari tabel LIBRARY
    query = "SELECT ID, JUDUL, KATEGORI, NO_RAK, PENULIS, PENERBIT, TAHUN, STOK FROM LIBRARY"
    # Menjalankan query menggunakan kursor
    cursor.execute(query)
    # Mengambil semua baris hasil eksekusi query
    rows = cursor.fetchall()
    # Memanggil fungsi Update_tvr dengan parameter rows
    Update_tvr(rows)

def Update_tvr(rows):
    tvr.delete(*tvr.get_children())
    for i in rows:
        tvr.insert('', 'end', values=i)

def Update_people():
    if messagebox.askyesno("Harap Konfirmasi", "Apakah Anda Serius Ingin Memperbaharui Data Ini?"):
        query = """
            UPDATE LIBRARY
            SET JUDUL=:JUDUL, KATEGORI=:KATEGORI, NO_RAK=:NO_RAK, PENULIS=:PENULIS, PENERBIT=:PENERBIT, TAHUN=:TAHUN, STOK=:STOK
            WHERE ID=:ID
        """
        params = {
            'ID': v_id.get(),
            'JUDUL': v_judul.get(),
            'KATEGORI': v_kategori.get(),
            'NO_RAK': v_no_rak.get(),  
            'PENULIS': v_penulis.get(),
            'PENERBIT': v_penerbit.get(),
            'TAHUN': v_tahun_penerbit.get(),
            'STOK': v_stok.get()
        }
        cursor.execute(query, params)
        conn.commit()
        clear_field()
        select_all()

    else:
        return True

def add_new():
    query = """
        INSERT INTO LIBRARY
        (JUDUL, KATEGORI, NO_RAK, PENULIS, PENERBIT, TAHUN, STOK)
        VALUES (:JUDUL, :KATEGORI, :NO_RAK, :PENULIS, :PENERBIT, :TAHUN, :STOK)
        """
    params = {
        'JUDUL': v_judul.get(),
        'KATEGORI': v_kategori.get(),
        'NO_RAK': v_no_rak.get(),  
        'PENULIS': v_penulis.get(),
        'PENERBIT': v_penerbit.get(),
        'TAHUN': v_tahun_penerbit.get(),
        'STOK': v_stok.get(),
    }
    cursor.execute(query, params)
    conn.commit()
    select_all()
    clear_field()

def getrow(event):
    rowid = tvr.identify_row(event.y)
    item = tvr.item(rowid)
    v_id.set(item['values'][0])
    v_judul.set(item['values'][1])
    v_kategori.set(item['values'][2])
    v_no_rak.set("00"+str(item['values'][3]))
    v_penulis.set(item['values'][4])
    v_penerbit.set(item['values'][5])
    v_tahun_penerbit.set(item['values'][6])
    v_stok.set(item['values'][7])

def clear_field():
    judul_field.delete(0, 'end')
    penulis_field.delete(0, 'end')
    penerbit_field.delete(0, 'end')
    tahun_penerbit_field.delete(0, 'end')
    kategori_field.set('')
    no_rak_field.set('')
    stok_field.delete(0, 'end')

def search():
    q2 = q.get()
    query = """
    SELECT ID, JUDUL, KATEGORI, NO_RAK, PENULIS, PENERBIT, TAHUN, STOK FROM LIBRARY WHERE JUDUL LIKE {} OR NO_RAK LIKE {}
    """.format("'%"+q2+"%'", "'%"+q2+"%'")
    cursor.execute(query)
    conn.commit()
    rows = cursor.fetchall()
    Update_tvr(rows)

def clear():
    ent.delete(0, 'end')
    clear_field()
    select_all()

def delete_book():
    id = v_id.get()
    if(messagebox.askyesno("Konfirmasi Hapus?", "Apakah anda serius igin menghapus data buku ini?")):
        query = "DELETE FROM LIBRARY WHERE ID = {}".format(id)
        cursor.execute(query)
        conn.commit()
        clear_field()
        select_all()
    else:
        return True

#wrapper
wrapper1 = LabelFrame(root, text="Daftar Buku")
wrapper2 = LabelFrame(root, text="Pencarian")
wrapper3 = LabelFrame(root, text="Formulir Buku")  
#posisi wrapper
wrapper1.pack(fill="both", expand="yes", padx=20, pady=20)
wrapper2.pack(fill="both", padx=20, pady=10)
wrapper3.pack(fill="both", padx=20, pady=20)

#form
v_id = IntVar()
v_judul = StringVar()
v_kategori = StringVar()
v_no_rak = StringVar()
v_penulis = StringVar()
v_penerbit = StringVar()
v_tahun_penerbit = StringVar()
v_stok = IntVar()

judul = Label(wrapper3, text="Judul")
judul_field = Entry(wrapper3, textvariable=v_judul)
judul.grid(row=0, column=0, sticky="w", pady=4)
judul_field.grid(row=0, column=1, columnspan=2, sticky="w", pady=4, padx=10)

kategori = Label(wrapper3, text="Kategori") 
kategori_field = ttk.Combobox(wrapper3, width=17, textvariable=v_kategori)
kategori_field['values'] = (
                    '000 - Umum',
                    '100 - Filsafat dan Psikologi', 
                    '200 - Agama',
                    '300 - Sosial',
                    '400 - Bahasa',
                    '500 - Sains dan Matematika',
                    '600 - Teknologi',
                    '700 - Seni dan Rekreasi',
                    '800 - Literatur dan Sastra',
                    '900 - Sejarah dan Geografi',
                )
kategori.grid(row=1, column=0, sticky="w", pady=4)
kategori_field.grid(row=1, column=1, columnspan=2, sticky="w", pady=4, padx=10)

no_rak = Label(wrapper3, text="No Rak")
no_rak_field = ttk.Combobox(wrapper3, width=17, textvariable=v_no_rak)
no_rak_field['values'] = ('001', '002', '003', '004', '005')
no_rak.grid(row=2, column=0, sticky="w", pady=4)
no_rak_field.grid(row=2, column=1, columnspan=2, sticky="w", pady=4, padx=10)

penulis = Label(wrapper3, text="Penulis")
penulis_field = Entry(wrapper3, textvariable=v_penulis)
penulis.grid(row=3, column=0, sticky="w", pady=4)
penulis_field.grid(row=3, column=1, columnspan=2, sticky="w", pady=4, padx=10)

penerbit = Label(wrapper3, text="Penerbit")
penerbit_field = Entry(wrapper3, textvariable=v_penerbit)
penerbit.grid(row=0, column=3, sticky="w", pady=4, padx=10)
penerbit_field.grid(row=0, column=4, columnspan=2, sticky="w", pady=4)

tahun_penerbit = Label(wrapper3, text="Tahun Penerbit")
tahun_penerbit_field = Entry(wrapper3, textvariable=v_tahun_penerbit)
tahun_penerbit.grid(row=1, column=3, sticky="w", pady=4, padx=10)
tahun_penerbit_field.grid(row=1, column=4, columnspan=2, sticky="w", pady=4)

stok = Label(wrapper3, text="Stok")
stok_field = Entry(wrapper3, textvariable=v_stok)
stok.grid(row=2, column=3, sticky="w", pady=4, padx=10)
stok_field.grid(row=2, column=4, columnspan=2, sticky="w", pady=4)

frame_btn = Frame(wrapper3)
up_btn = Button(frame_btn, text="Update", command=Update_people)
add_btn = Button(frame_btn, text="Tambah Baru", command=add_new)
delete_btn = Button(frame_btn, text="Hapus", command=delete_book)

frame_btn.grid(row=4, column=0, columnspan=5, sticky="w", pady=10)
add_btn.pack(side=LEFT, padx=5)
up_btn.pack(side=LEFT, padx=5)
delete_btn.pack(side=LEFT, padx=5)

#wrapper 2 - pencarian
q =StringVar()
lbl = Label(wrapper2, text="Search")
lbl.pack(side=LEFT, padx=10, pady=15)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=LEFT, padx=6, pady=15)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=LEFT, padx=6, pady=15)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=LEFT, padx=6, pady=15)

#wrapper 1 - Tabel data buku
tvr = ttk.Treeview(wrapper1, columns=(0,1,2,3,4,5,6,7), show="headings", height=6)
style = ttk.Style()
# ["aqua", "step", "clam", "alt", "default", "classic"]
style.theme_use("clam")
tvr.pack(side=RIGHT)
tvr.place(x=0, y=0)

tvr.heading(0, text="Id")
tvr.heading(1, text="Judul")
tvr.heading(2, text="Kategori")
tvr.heading(3, text="No Rak")
tvr.heading(4, text="Penulis")
tvr.heading(5, text="Penerbit")
tvr.heading(6, text="Tahun Penerbit")
tvr.heading(7, text="Stok")

tvr.column(0, stretch=NO, minwidth=0, width=0)
tvr.column(1, width=95, minwidth=135, anchor=CENTER)
tvr.column(2, width=95, minwidth=135, anchor=CENTER)
tvr.column(3, width=95, minwidth=135, anchor=CENTER)
tvr.column(4, width=95, minwidth=135, anchor=CENTER)
tvr.column(5, width=95, minwidth=135, anchor=CENTER)
tvr.column(6, width=95, minwidth=135, anchor=CENTER)
tvr.column(7, width=65, minwidth=105, anchor=CENTER)

tvr.bind('<Double 1>', getrow)

yscrollbar = Scrollbar(wrapper1, orient="vertical", command=tvr.yview)
yscrollbar.pack(side=RIGHT, fill="y")

xscrollbar = Scrollbar(wrapper1, orient="horizontal", command=tvr.xview)
xscrollbar.pack(side=BOTTOM, fill="x")

tvr.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

if __name__ == '__main__':
    root.title("Aplikasi Data Perpustakaan")
    root.geometry("700x500")
    root.resizable(FALSE,FALSE)
    if(isFirst("LIBRARY")):
        create_table()
    else:
        pass
    root.mainloop()

#mnit 40