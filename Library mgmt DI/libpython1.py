
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mgmt1  

# Initialize the main application window
root = tk.Tk()
root.title("Library Management System")
root.geometry("800x600")
root.configure(bg='black')  # Background color-#050b24

title_label = tk.Label(root, text="LIBRARY MANAGEMENT SYSTEM", font=("Courier New", 24,"bold"), bg='#f0f0f0')
title_label.pack(pady=60)

# Define the function to add books
def add_book_form():
    add_book_window = tk.Toplevel(root)
    add_book_window.title("Add Book")
    add_book_window.geometry("400x300")
    add_book_window.configure(bg='#393e55')  # Background color

    tk.Label(add_book_window, text="Title", font=("Courier New", 12), bg='#b0c8a0').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    title_entry = tk.Entry(add_book_window, font=("Courier New", 12))
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_book_window, text="Author", font=("Courier New", 12), bg='#b0c8a0').grid(row=1, column=0, padx=10, pady=10, sticky=W)
    author_entry = tk.Entry(add_book_window, font=("Courier New", 12))
    author_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_book_window, text="Genre", font=("Courier New", 12), bg='#b0c8a0').grid(row=2, column=0, padx=10, pady=10, sticky=W)
    genre_entry = tk.Entry(add_book_window, font=("Courier New", 12))
    genre_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(add_book_window, text="Year", font=("Courier New", 12), bg='#b0c8a0').grid(row=3, column=0, padx=10, pady=10, sticky=W)
    year_entry = tk.Entry(add_book_window, font=("Courier New", 12))
    year_entry.grid(row=3, column=1, padx=10, pady=10)

    def submit_book():
        title = title_entry.get()
        author = author_entry.get()
        genre = genre_entry.get()
        year = int(year_entry.get())
        mgmt1.add_book(title, author, genre, year)
        messagebox.showinfo("Success", "Book added successfully!")
        add_book_window.destroy()

    tk.Button(add_book_window, text="Add Book", font=("Courier New", 12), bg="#586a69", fg="black", command=submit_book).grid(row=4, column=1, padx=10, pady=20, sticky=E)

# Define the function to add members
def add_member_form():
    add_member_window = tk.Toplevel(root)
    add_member_window.title("Add Member")
    add_member_window.geometry("400x300")
    add_member_window.configure(bg='#393e55')  # Background color

    tk.Label(add_member_window, text="Name", font=("Courier New", 12), bg='#b0c8a0').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    name_entry = tk.Entry(add_member_window, font=("Courier New", 12))
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_member_window, text="Email", font=("Courier New", 12), bg='#b0c8a0').grid(row=1, column=0, padx=10, pady=10, sticky=W)
    email_entry = tk.Entry(add_member_window, font=("Courier New", 12))
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_member_window, text="Phone", font=("Courier New", 12), bg='#b0c8a0').grid(row=2, column=0, padx=10, pady=10, sticky=W)
    phone_entry = tk.Entry(add_member_window, font=("Courier New", 12))
    phone_entry.grid(row=2, column=1, padx=10, pady=10)

    # tk.Label(add_member_window, text="Address", font=("Courier New", 12), bg='#b0c8a0').grid(row=3, column=0, padx=10, pady=10, sticky=W)
    # address_entry = tk.Entry(add_member_window, font=("Courier New", 12))
    # address_entry.grid(row=3, column=1, padx=10, pady=10)

    def submit_member():
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        # address = address_entry.get()
        mgmt1.add_member(name, email, phone)
        messagebox.showinfo("Success", "Member added successfully!")
        add_member_window.destroy()

    tk.Button(add_member_window, text="Add Member", font=("Courier New", 12), bg="#586a69", fg="black", command=submit_member).grid(row=4, column=1, padx=10, pady=20, sticky=E)

# Define the function to borrow books
def borrow_book_form():
    borrow_book_window = tk.Toplevel(root)
    borrow_book_window.title("Borrow Book")
    borrow_book_window.geometry("400x200")
    borrow_book_window.configure(bg='#393e55')  # Background color

    tk.Label(borrow_book_window, text="Member ID", font=("Courier New", 12), bg='#b0c8a0').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    member_id_entry = tk.Entry(borrow_book_window, font=("Courier New", 12))
    member_id_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(borrow_book_window, text="Book ID", font=("Courier New", 12), bg='#b0c8a0').grid(row=1, column=0, padx=10, pady=10, sticky=W)
    book_id_entry = tk.Entry(borrow_book_window, font=("Courier New", 12))
    book_id_entry.grid(row=1, column=1, padx=10, pady=10)

    def submit_borrow():
        member_id = int(member_id_entry.get())
        book_id = int(book_id_entry.get())
        mgmt1.borrow_book(member_id, book_id)
        messagebox.showinfo("Success", "Book borrowed successfully!")
        borrow_book_window.destroy()

    tk.Button(borrow_book_window, text="Borrow Book", font=("Courier New", 12), bg="#586a69", fg="black", command=submit_borrow).grid(row=2, column=1, padx=10, pady=20, sticky=E)

# Define the function to return books
def return_book_form():
    return_book_window = tk.Toplevel(root)
    return_book_window.title("Return Book")
    return_book_window.geometry("400x200")
    return_book_window.configure(bg='#393e55')  # Background color

    tk.Label(return_book_window, text="Book ID", font=("Courier New", 12), bg='#b0c8a0').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    book_id_entry = tk.Entry(return_book_window, font=("Courier New", 12))
    book_id_entry.grid(row=0, column=1, padx=10, pady=10)

    def submit_return():
        book_id = int(book_id_entry.get())
        mgmt1.return_book(book_id)
        messagebox.showinfo("Success", "Book returned successfully!")
        return_book_window.destroy()

    tk.Button(return_book_window, text="Return Book", font=("Courier New", 12), bg="#586a69", fg="black", command=submit_return).grid(row=1, column=1, padx=10, pady=20, sticky=E)

# Define the function to display books
def display_books():
    books = mgmt1.get_books()
    display_books_window = tk.Toplevel(root)
    display_books_window.title("List of Books")
    display_books_window.geometry("1000x400")
    display_books_window.configure(bg='#393e55')  # Background color

    tk.Label(display_books_window, text="Books List", font=("Courier New", 16), bg='#90a675').pack(pady=10)

    frame = Frame(display_books_window, bg='#e0f7fa')
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Book ID", font=("Courier New", 12), width=10, bg='#b0c8a0').grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame, text="Title", font=("Courier New", 12), width=20, bg='#b0c8a0').grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame, text="Author", font=("Courier New", 12), width=15, bg='#b0c8a0').grid(row=0, column=2, padx=5, pady=5)
    tk.Label(frame, text="Genre", font=("Courier New", 12), width=15, bg='#b0c8a0').grid(row=0, column=3, padx=5, pady=5)
    tk.Label(frame, text="Year", font=("Courier New", 12), width=10, bg='#b0c8a0').grid(row=0, column=4, padx=5, pady=5)
    tk.Label(frame, text="Availability", font=("Courier New", 12), width=15, bg='#b0c8a0').grid(row=0, column=5, padx=5, pady=5)

    for i, (book_id, title, author, genre, year, availability) in enumerate(books):
        tk.Label(frame, text=book_id, font=("Courier New", 12), width=5, bg='#e0f7fa').grid(row=i+1, column=0, padx=5, pady=5)
        tk.Label(frame, text=title, font=("Courier New", 12), width=20, bg='#e0f7fa').grid(row=i+1, column=1, padx=5, pady=5)
        tk.Label(frame, text=author, font=("Courier New", 12), width=15, bg='#e0f7fa').grid(row=i+1, column=2, padx=5, pady=5)
        tk.Label(frame, text=genre, font=("Courier New", 12), width=10, bg='#e0f7fa').grid(row=i+1, column=3, padx=5, pady=5)
        tk.Label(frame, text=year, font=("Courier New", 12), width=10, bg='#e0f7fa').grid(row=i+1, column=4, padx=5, pady=5)
        tk.Label(frame, text=availability, font=("Courier New", 12), width=10, bg='#e0f7fa').grid(row=i+1, column=5, padx=5, pady=5)

# Define the function to display members
def display_members():
    members = mgmt1.get_members()
    display_members_window = tk.Toplevel(root)
    display_members_window.title("List of Members")
    display_members_window.geometry("800x400")
    display_members_window.configure(bg='#393e55')  # Background color

    tk.Label(display_members_window, text="Members List", font=("Courier New", 16), bg='#90a675').pack(pady=10)

    frame = Frame(display_members_window, bg='#e0f7fa')
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Member ID", font=("Courier New", 12), width=10, bg='#b0c8a0').grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame, text="Name", font=("Courier New", 12), width=20, bg='#b0c8a0').grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame, text="Email", font=("Courier New", 12), width=25, bg='#b0c8a0').grid(row=0, column=2, padx=5, pady=5)
    tk.Label(frame, text="Phone", font=("Courier New", 12), width=15, bg='#b0c8a0').grid(row=0, column=3, padx=5, pady=5)
    #tk.Label(frame, text="Address", font=("Helvetica", 12), width=30, bg='#e0f7fa').grid(row=0, column=4, padx=5, pady=5)

    for i, (member_id, name, email, phone) in enumerate(members):
        tk.Label(frame, text=member_id, font=("Courier New", 12), width=5, bg='#e0f7fa').grid(row=i+1, column=0, padx=5, pady=5)
        tk.Label(frame, text=name, font=("Courier New", 12), width=20, bg='#e0f7fa').grid(row=i+1, column=1, padx=5, pady=5)
        tk.Label(frame, text=email, font=("Courier New", 12), width=25, bg='#e0f7fa').grid(row=i+1, column=2, padx=5, pady=5)
        tk.Label(frame, text=phone, font=("Courier New", 12), width=15, bg='#e0f7fa').grid(row=i+1, column=3, padx=5, pady=5)
        #tk.Label(frame, text=address, font=("Helvetica", 12), width=30, bg='#e0f7fa').grid(row=i+1, column=4, padx=5, pady=5)
def remove_book_form():
    remove_book_window = tk.Toplevel(root)
    remove_book_window.title("Remove Book")
    remove_book_window.geometry("400x200")
    remove_book_window.configure(bg='#393e55')  # Background color

    tk.Label(remove_book_window, text="Book ID", font=("Courier New", 12), bg='#b0c8a0').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    book_id_entry = tk.Entry(remove_book_window, font=("Courier New", 12))
    book_id_entry.grid(row=0, column=1, padx=10, pady=10)

    def submit_remove_book():
        book_id = book_id_entry.get()
        if not book_id:
            messagebox.showerror("Error", "Please enter a Book ID")
            return
        try:
            mgmt1.remove_book(int(book_id))
            messagebox.showinfo("Success", "Book removed successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid Book ID")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        remove_book_window.destroy()

    tk.Button(remove_book_window, text="Remove Book", font=("Courier New", 12), bg="#586a69", fg="black", command=submit_remove_book).grid(row=1, column=1, padx=10, pady=20, sticky=E)

# Define the function to remove members
def remove_member_form():
    remove_member_window = tk.Toplevel(root)
    remove_member_window.title("Remove Member")
    remove_member_window.geometry("400x200")
    remove_member_window.configure(bg='#393e55')  # Background color

    tk.Label(remove_member_window, text="Member ID", font=("Courier New", 12), bg='#b0c8a0').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    member_id_entry = tk.Entry(remove_member_window, font=("Courier New", 12))
    member_id_entry.grid(row=0, column=1, padx=10, pady=10)

    def submit_remove_member():
        member_id = member_id_entry.get()
        if not member_id:
            messagebox.showerror("Error", "Please enter a Member ID")
            return
        try:
            mgmt1.remove_member(int(member_id))
            messagebox.showinfo("Success", "Member removed successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid Member ID")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        remove_member_window.destroy()

    tk.Button(remove_member_window, text="Remove Member", font=("Courier New", 12), bg="#586a69", fg="black", command=submit_remove_member).grid(row=1, column=1, padx=10, pady=20, sticky=E)
# Create a frame to hold buttons in a grid layout
button_frame = tk.Frame(root, bg='#e0f7fa')
button_frame.pack(padx=50, pady=40)


# Add buttons to the frame
tk.Button(button_frame, text="Add Book", font=("Courier New", 14), bg="#80555d", fg="black",width=15, height=2, command=add_book_form).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Add Member", font=("Courier New", 14), bg="#80555d", fg="black",width=15, height=2, command=add_member_form).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Borrow Book", font=("Courier New", 14), bg="#80555d", fg="black",width=15, height=2, command=borrow_book_form).grid(row=1, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Return Book", font=("Courier New", 14), bg="#80555d", fg="black",width=15, height=2, command=return_book_form).grid(row=1, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Display Books", font=("Courier New", 14), bg="#80555d", fg="black",width=15, height=2, command=display_books).grid(row=2, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Display Members", font=("Courier New", 14), bg="#80555d", fg="black",width=15, height=2, command=display_members).grid(row=2, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Remove Book", font=("Courier New", 14), bg="#80555d", fg="black",width=15, height=2, command=remove_book_form).grid(row=3, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Remove Member", font=("Courier New", 14), bg="#80555d", fg="black",width=15, height=2, command=remove_member_form).grid(row=3, column=1, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()
