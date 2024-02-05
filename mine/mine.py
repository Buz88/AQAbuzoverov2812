import csv
import tkinter as tk
from tkinter import filedialog, messagebox

def compare_csv(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        csv_reader1 = csv.reader(f1)
        csv_reader2 = csv.reader(f2)

        rows1 = list(csv_reader1)
        rows2 = list(csv_reader2)

        # Сравниваем количество строк
        if len(rows1) != len(rows2):
            messagebox.showinfo("Различия", "Разное количество строк в файлах")
            return

        # Сравниваем каждую строку
        differences = []
        for i in range(len(rows1)):
            if rows1[i] != rows2[i]:
                differences.append((i + 1, rows1[i], rows2[i]))

        if differences:
            result_message = "Обнаружены различия в следующих строках:\n\n"
            for diff in differences:
                result_message += f"Строка {diff[0]}:\nФайл 1: {diff[1]}\nФайл 2: {diff[2]}\n\n"
            messagebox.showinfo("Различия", result_message)
        else:
            messagebox.showinfo("Различия", "Файлы идентичны")

def browse_file(entry):
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def main():
    root = tk.Tk()
    root.title("Сравнение CSV файлов")

    file1_label = tk.Label(root, text="Файл 1:")
    file1_label.grid(row=0, column=0, padx=5, pady=5)

    file1_entry = tk.Entry(root, width=40)
    file1_entry.grid(row=0, column=1, padx=5, pady=5)

    file1_browse_button = tk.Button(root, text="Обзор", command=lambda: browse_file(file1_entry))
    file1_browse_button.grid(row=0, column=2, padx=5, pady=5)

    file2_label = tk.Label(root, text="Файл 2:")
    file2_label.grid(row=1, column=0, padx=5, pady=5)

    file2_entry = tk.Entry(root, width=40)
    file2_entry.grid(row=1, column=1, padx=5, pady=5)

    file2_browse_button = tk.Button(root, text="Обзор", command=lambda: browse_file(file2_entry))
    file2_browse_button.grid(row=1, column=2, padx=5, pady=5)

    compare_button = tk.Button(root, text="Сравнить", command=lambda: compare_csv(file1_entry.get(), file2_entry.get()))
    compare_button.grid(row=2, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()