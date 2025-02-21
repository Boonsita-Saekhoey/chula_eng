import tkinter as tk
import random

# Thai consonants and their pronunciations
thai_consonants = {
    "ก": "kaw kai",
    "ข": "khaw khai",
    "ฃ": "khaw khuat",
    "ค": "khaw khwai",
    "ฅ": "khaw khon",
    "ฆ": "khaw rakhang",
    "ง": "ngaw ngu",
    "จ": "jaw jan",
    "ฉ": "chaw ching",
    "ช": "chaw chang",
    "ซ": "saw so",
    "ฌ": "chaw choe",
    "ญ": "yaw ying",
    "ฎ": "daw chada",
    "ฏ": "dtaw patak",
    "ฐ": "thaw than",
    "ฑ": "thaw montho",
    "ฒ": "thaw phu-thao",
    "ณ": "naw nen",
    "ด": "daw dek",
    "ต": "dtaw tao",
    "ถ": "thaw thung",
    "ท": "thaw thahan",
    "ธ": "thaw thong",
    "น": "naw nu",
    "บ": "baw bai-mai",
    "ป": "paw pla",
    "ผ": "phaw phueng",
    "ฝ": "faw fa",
    "พ": "phaw phan",
    "ฟ": "faw fan",
    "ภ": "phaw sam-phao",
    "ม": "maw ma",
    "ย": "yaw yak",
    "ร": "raw rua",
    "ล": "law ling",
    "ว": "waw waen",
    "ศ": "saw sala",
    "ษ": "saw rue-si",
    "ส": "saw suea",
    "ห": "haw hip",
    "ฬ": "law chu-la",
    "อ": "aw ang",
    "ฮ": "haw nok-huk"
}

# Function to show a new random Thai consonant
def new_card():
    global current_consonant
    current_consonant = random.choice(list(thai_consonants.keys()))
    consonant_label.config(text=current_consonant)
    answer_label.config(text="?")

# Function to reveal the pronunciation
def show_answer():
    answer_label.config(text=thai_consonants[current_consonant])

# GUI setup
root = tk.Tk()
root.title("Thai Consonant Flashcards")
root.geometry("300x200")

consonant_label = tk.Label(root, text="", font=("Arial", 50))
consonant_label.pack(pady=20)

answer_label = tk.Label(root, text="?", font=("Arial", 20))
answer_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

next_button = tk.Button(button_frame, text="New Card", command=new_card)
next_button.grid(row=0, column=0, padx=10)

answer_button = tk.Button(button_frame, text="Show Answer", command=show_answer)
answer_button.grid(row=0, column=1, padx=10)

# Start the game with a card
new_card()

root.mainloop()