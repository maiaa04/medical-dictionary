import tkinter as tk
import customtkinter as customtk
import medical_dict as med
from PIL import Image


class MedicalDictionaryApp(customtk.CTk):

    def __init__(self):
        super().__init__()
        customtk.set_default_color_theme("green-theme.json")
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color = ('#e8ffe8', '#1c1f1a'))

        dictionary = med.load_dictionary('definitions_python_project.csv')

        self.title("Medical Dictionary")
        self.geometry("900x600")
        self.resizable(False, False)

        main_frame = customtk.CTkScrollableFrame(master=self, width=900, height=590)
        main_frame.grid(row=0, column=0, padx=0, pady=0)
        main_frame.grid_columnconfigure(0, weight=1)

        # image/logo
        logo = customtk.CTkImage(light_image=Image.open('medical_dict_light.png'),
                                 dark_image=Image.open('medical_dict_dark.png'),
                                 size=(180, 180))
        label1 = customtk.CTkLabel(master=main_frame, image=logo, text='')
        label1.grid(row=0, column=0, padx=0, pady=5)

        # input textbox - Enter the desired term
        input_textbox = customtk.CTkTextbox(main_frame, width=200, height=50, fg_color='transparent', font=('Open Sans', 18))
        input_textbox.grid(row=1, column=0, padx=0, pady=5)
        input_textbox.insert('0.0', 'Enter desired term:')
        input_textbox.configure(state='disabled')
        input_textbox.tag_config("center", justify='center')
        input_textbox.tag_add("center", 1.0, "end")

        # input entry
        input_entry = customtk.CTkEntry(
            main_frame, placeholder_text="e.g.: labour", width=200, height=50)
        input_entry.grid(row=2, column=0, padx=0, pady=5)

        # output textbox
        output_textbox = customtk.CTkTextbox(
            main_frame, width=800, height=300, font=('Open Sans', 16), wrap='word')
        output_textbox.grid(row=4, column=0, padx=0, pady=5)

        # save button
        save_button = customtk.CTkButton(main_frame, width=200, height=30, corner_radius=10, border_width=3,
                                         text="Search", command=lambda: self.save_button_callback(output_textbox, input_entry))
        save_button.grid(row=3, column=0, padx=0, pady=5)

    def save_button_callback(self, textbox_output: customtk.CTkTextbox, entry_input: customtk.CTkEntry):
        textbox_output.configure(state='normal')
        textbox_output.delete('0.0', tk.END)
        term = entry_input.get().capitalize()
        dictionary = med.load_dictionary('definitions_python_project.csv')
        other_terms = med.search(dictionary, term)
        if len(other_terms) == 0:
            textbox_output.insert(
                '0.0', 'No definition with given term found.')
        else:
            for other_term in reversed(other_terms):
                definition = dictionary[other_term]
                textbox_output.insert(
                    '0.0', other_term+' - '+definition+'\n\n')
        textbox_output.configure(state='disabled')


app = MedicalDictionaryApp()
app.mainloop()
