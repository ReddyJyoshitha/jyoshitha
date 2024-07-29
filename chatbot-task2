import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import random
import tkinter as tk
from tkinter import scrolledtext
class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("400x500")
        
        self.chat_log = scrolledtext.ScrolledText(root, state='disabled', wrap='word')
        self.chat_log.pack(pady=10, padx=10, fill='both', expand=True)
        
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(fill='x')
        
        self.entry_text = tk.Entry(self.entry_frame)
        self.entry_text.pack(side='left', fill='x', expand=True, padx=10, pady=10)
        self.entry_text.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side='right', padx=10, pady=10)

    def send_message(self, event=None):
        user_input = self.entry_text.get()
        self.entry_text.delete(0, tk.END)
        
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, "You: " + user_input + "\n")
        self.chat_log.config(state='disabled')
        
        intent = get_intent(user_input)
        response = get_response(intent)
        
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, "Bot: " + response + "\n")
        self.chat_log.config(state='disabled')
        
        self.chat_log.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
