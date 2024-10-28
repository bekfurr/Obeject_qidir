import tkinter as tk
from tkinter import messagebox

def qidirish():
    a = list(map(str, entry_massiv.get().split()))
    m = entry_qidirilayotgan_object.get()
    count = 0  # Objectning takrorlanish sonini hisoblash
    for i in range(len(a)):
        if m == a[i]:
            if count == 0:
                index_message = f"Object topildi! Index: {i}"
            count += 1
    if count > 0:
        messagebox.showinfo("Natija", f"{index_message}\nObject {count} marta foydalanilgan ")
    else:
        messagebox.showinfo("Natija", "Object topilmadi")

root = tk.Tk()
root.title("Massivda son qidirish")
root.geometry("500x200")

label_massiv = tk.Label(root, text="Massivni kiriting (probel bilan ajratib):")
label_massiv.pack()

entry_massiv = tk.Entry(root, width=85)
entry_massiv.pack()

label_qidirilayotgan_object = tk.Label(root, text="Qidirilayotgan Objectni kiriting:")
label_qidirilayotgan_object.pack()

entry_qidirilayotgan_object = tk.Entry(root, width=50)
entry_qidirilayotgan_object.pack()

button_qidirish = tk.Button(root, text="Qidirish", command=qidirish)
button_qidirish.pack(pady=10)

root.mainloop()

