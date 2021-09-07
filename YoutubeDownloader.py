from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
from youtube_dl import *


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    loc = str(Folder_Name)
    location.delete(0, END)
    location.insert(0, Folder_Name)


def check(*event):
    ydl_opts = {}
    resolution = []
    url = lin.get()
    valid = checkurl(url)
    if valid:
        with YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            formats = meta.get('formats', meta)
            vid_title = meta.get('title', meta)
        vid_labl['text'] = vid_title
        for f in formats:
            resolution.append(f['format'])
        modality['values'] = resolution
    else:
        messagebox.showerror("ERROR", "Please insert a true URL")


def download_video():
    url = lin.get()
    res = qua.get()
    lo = loc.get()
    try:
        res = int(res[:res.find('-')].strip())
        ydl_opts = {'format': f'{res}', 'outtmpl': lo + r'\%(title)s.%(ext)s', 'progress_hooks': [finish]}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        pass


def checkurl(link):
    extractors = gen_extractors()
    for e in extractors:
        if e.suitable(link) and e.IE_NAME != 'generic':
            return True
    return False


def finish(d):
    p = d['_percent_str']
    p = p.replace('%', '')
    progress['value'] = float(p)
    root.update_idletasks()


root = Tk()
qua = StringVar()
lin = StringVar()
loc = StringVar()
Link = Label(root, text="Link: ")
Path = Label(root, text="Path: ")
Quality = Label(root, text="Quality: ")
adress = Entry(root, width=50, textvariable=lin)
location = Entry(root, width=50, textvariable=loc)
modality = ttk.Combobox(root, width=45, textvariable=qua)
download = Button(root, width=8, height=1, text="Download")
browse = Button(root, width=8, height=1, text="Browse", command=openLocation)
vid_labl = Label(root, width=20, height=2)
progress = progressBar = ttk.Progressbar(root, style='text.Horizontal.TProgressbar', length=200, maximum=100, value=0)
root.title("Youtube downloader")
root.geometry("450x250")
root.resizable(width=False, height=False)
root.configure(background='Purple')
root.iconbitmap('icon.ico')
Link.place(x=10, y=20)
Link.configure(background='Purple', foreground='#0ee704')
lin.trace('w', check)
adress.place(x=45, y=21)
Path.place(x=10, y=100)
Path.configure(background='Purple', foreground='#0ee704')
location.place(x=45, y=101)
Quality.place(x=10, y=180)
Quality.configure(background='Purple', foreground='#0ee704')
modality.place(x=60, y=181)
download.place(x=363, y=180)
download.configure(background='Blue', foreground='White', command=download_video)
browse.place(x=363, y=99)
browse.configure(background='Blue', foreground='White')
vid_labl.place(x=20, y=210)
vid_labl.configure(background='Purple', foreground='#0ee704')
progress.place(x=235, y=213)
root.mainloop()
