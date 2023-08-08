from tkinter import *
from pytube import YouTube
import yt_downloader as ytd

main_window = Tk()
main_window.geometry("500x300")
main_window.resizable(0,0)
main_window.title("YouTube Downloader")

title_icon = PhotoImage(file = "icon\\youtube.png")

main_window.iconphoto(False, title_icon)

Label(main_window,
      text="Enter the Youtube Link Below",
      font = "arial 20 bold"
      ).pack()

link = StringVar()

Label (main_window,
       text="Lay the link here",
       font = "arial 15 bold").place(x = 160, y = 60)

link_enter = Entry(main_window,
                   width=70,
                   textvariable=link,
                   justify=CENTER).place(x = 32, y = 90)

def downloader():
    global link
    link = str(link.get())
    ytd.downloader(link)
    Label(main_window, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

"""
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(main_window, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
"""


Button(main_window,
       text="Download",
       font = "arial 15 bold",
       bg = "pale violet red",
       padx = 2,
       command=downloader).place(x = 180, y = 150)

#downloaded()


main_window.mainloop()