from tkinter import *
from tkinter.ttk import *
import load

root = Tk()
root.title("Load")

swd = root.winfo_screenwidth()
sht = root.winfo_screenheight()
halfswd = int(swd/2)
halfsht = int(sht/2)
root.geometry(f"300x120+{halfswd-150}+{halfsht-200}")
root.resizable(False, False)
root.attributes('-topmost', 1)

url = StringVar()

def download(): 
    load.main(url=url.get())
    print("Finished.")
def download_2(event): 
    load.main(url=url.get())
    print("Finished")

signin = Frame(root)
signin.pack(padx=50, fill='x', expand=True)

url_label = Label(signin, text="Copy link:")
url_label.pack(fill='x', expand=True)

url_entry = Entry(signin, textvariable=url)
url_entry.pack(fill='x', expand=True)
url_entry.focus()

# Download button
download_btn = Button(signin, text="Login", command=download)
download_btn.pack(fill='x', expand=True, pady=10)
root.bind('<Return>', download_2)

root.mainloop()