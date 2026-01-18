import tkinter as tk
from tkinter import messagebox

# Test đơn giản để kiểm tra tkinter
try:
    root = tk.Tk()
    root.title("Test Tkinter")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Nếu bạn thấy cửa sổ này,\ntkinter đang hoạt động tốt!", 
                     font=('Arial', 12), pady=20)
    label.pack()
    
    def show_message():
        messagebox.showinfo("Thành công", "Tkinter hoạt động bình thường!")
    
    button = tk.Button(root, text="Click để test", command=show_message, 
                       font=('Arial', 10), padx=20, pady=10)
    button.pack(pady=20)
    
    print("Cửa sổ test đã mở. Đóng cửa sổ để thoát.")
    root.mainloop()
    print("Test hoàn tất!")
    
except Exception as e:
    print(f"LỖI: {e}")
    import traceback
    traceback.print_exc()
