import customtkinter as TK
import PIL as pillow
import upload

TK.set_appearance_mode("system")
TK.set_default_color_theme("blue")

App: TK.CTk = TK.CTk()
App.geometry("800x400")
App.title("StrawPage Image Command Generator")

App.grid_rowconfigure(0, weight=1)
App.grid_columnconfigure(0, weight=1)

def UploadToStrawpage(url, imageData) -> None:
    upload.ToStrawpage(url, imageData)

UrlLabel: TK.CTkLabel = TK.CTkLabel(App, text="StrawPage URL:")
UrlLabel.pack(pady=10, padx=10)
URLTextField: TK.CTkEntry = TK.CTkEntry(App, width=400, placeholder_text="Enter StrawPage URL here")
URLTextField.pack(pady=10, padx=10)

ImagePathLabel: TK.CTkLabel = TK.CTkLabel(App, text="Selected Image: None")
ImagePathLabel.pack(pady=10, padx=10)

global Image, ImageTk, ImageLabel
Image: pillow.Image = None
ImageTk: TK.CTkImage = None
ImageLabel: TK.CTkLabel = None

def RemoveImage() -> None:
    global Image, ImageTk, ImageLabel
    Image = None
    ImageTk = None
    if ImageLabel != None:
        ImageLabel.destroy()

def SelectImage() -> None:
    global Image, ImageTk, ImageLabel
    from tkinter import filedialog
    ImagePath: str = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.gif *.jpeg *.bmp *.tiff *.webp")], title="Select Image")
    if ImagePath != "" and ImagePath != None:
        ImagePathLabel.configure(text=f"Selected Image: {ImagePath}")
        UploadButton.configure(state="normal")

        # load image with pillow and display with tk
        RemoveImage()
        Image = pillow.Image.open(ImagePath)
        # image can only be a max of 400x400, so keep the aspect
        # keep the aspect ratio
        maxSize = max(Image.size)
        # make it so the largest size is 400
        if maxSize > 400:
            ratio = 400 / maxSize
            Image = Image.resize((int(Image.size[0] * ratio), int(Image.size[1] * ratio)))

        ImageTk = TK.CTkImage(light_image=Image, dark_image=Image,
                                  size=(400, 400))

        ImageLabel = TK.CTkLabel(App, image=ImageTk, text="")
        ImageLabel.pack(pady=10, padx=10)

def UploadImage() -> None:
    global Image
    if Image != None:
        print(Image)
        UploadToStrawpage(URLTextField.get(), Image)

UploadButton: TK.CTkButton = TK.CTkButton(App, text="Generate Command", command=UploadImage, state="disabled")
UploadButton.pack(pady=10, padx=10)
        
SelectImageButton: TK.CTkButton = TK.CTkButton(App, text="Select Image", command=SelectImage)
SelectImageButton.pack(pady=10, padx=10)

App.mainloop()