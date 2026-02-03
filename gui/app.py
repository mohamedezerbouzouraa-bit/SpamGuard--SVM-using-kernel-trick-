import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#partie inteface
def launch_gui(model, vectorizer):
    def predict_spam():
        message = text_box.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Input Error", "Please enter a message")
            return
        prediction = model.predict(vectorizer.transform([message]))[0]
        result = "Spam" if prediction == 1 else "Not Spam"
        messagebox.showinfo("Prediction Result", result)
    root = tk.Tk()
    root.title("Spam Detector")
    root.geometry("900x500")
    root.resizable(False, False)
    bg_image = Image.open("assets/insat.png").resize((900, 500))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    title = tk.Label(root, text="Spam Detection System",
                     font=("Helvetica", 22, "bold"),
                     bg="black", fg="white")
    title.place(relx=0.5, y=30, anchor="center")
    text_box = tk.Text(root, height=5, width=45, font=("Helvetica", 14))
    text_box.place(relx=0.5, rely=0.5, anchor="center")
    btn = tk.Button(root, text="Predict",
                    font=("Helvetica", 16, "bold"),
                    bg="#1a73e8", fg="white",
                    command=predict_spam)
    btn.place(relx=0.5, rely=0.65, anchor="center")

    root.mainloop()
