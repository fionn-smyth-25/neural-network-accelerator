import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from inference import predict


def select_image():

    filepath = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )

    if filepath:

        digit, confidence = predict(filepath)

        result_label.config(
            text=f"Prediction: {digit}\nConfidence: {confidence:.2f}"
        )

        # Display image
        img = Image.open(filepath)
        img = img.resize((200,200))

        img = ImageTk.PhotoImage(img)

        image_label.config(image=img)
        image_label.image = img


# Create window
window = tk.Tk()

window.title("MNIST Classifier")
window.geometry("400x400")


button = tk.Button(
    window,
    text="Select Image",
    command=select_image
)

button.pack(pady = 20)


image_label = tk.Label(window)
image_label.pack()


result_label = tk.Label(
    window,
    text="Prediction: "
)

result_label.pack(pady=20)


window.mainloop()
