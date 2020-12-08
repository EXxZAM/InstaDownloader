from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import instaloader # pip install instaloader
import threading
import os


root = Tk()
root.title('Instagram Downloader')
root.geometry('400x200')
root.resizable(0,0)
root.config(bg='#121212')


def downloadPost():
    link = postLink_Entry.get()
    
    def download():
        if 'https://www.instagram.com/p/' in link:
            try:
                location = filedialog.askdirectory()
                os.chdir(location)
                URL = link.replace('https://www.instagram.com/p/', '')
                URL = URL.replace('/','')
                L = instaloader.Instaloader()
                post = instaloader.Post.from_shortcode(L.context, URL)
                L.download_post(post, target=URL)
                messagebox.showinfo('Info', 'Download Compeleted!')
            except:
                messagebox.showerror('Error', 'URL IS INCORRECT')
        else:
            messagebox.showerror('Error', 'URL NOT FOUND')
    
    threading.Thread(target=download).start()



postLink_label = Label(root, text='Post URL:', bg='#121212', fg='white', font=('Arial', 13))
postLink_Entry = Entry(root, width=30)


downloadPost_btn = Button(root, text='Download Post', bg='#121212', fg='white', borderwidth=3, font=('Arial', 11), width=30, command=downloadPost)
exit_btn = Button(root, text='Exit App', bg='#121212', fg='white', borderwidth=3, font=('Arial', 11), width=30, command=root.destroy)

postLink_label.grid(row=0, column=0, padx=10, pady=10)
postLink_Entry.grid(row=0, column=1)

downloadPost_btn.place(relx=0.5, rely=0.4, anchor='c')
exit_btn.place(relx=0.5, rely=0.6, anchor='c')



root.mainloop()