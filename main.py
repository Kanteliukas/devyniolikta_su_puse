import tkinter
from tkinter import Tk, Label, Entry, Button, E
from generator_validator import check_personal_code
from generator_validator import generate_personal_code

task_window = Tk()

def validate_personal_id():
    personal_id_entry = validate_id_field.get()
    is_valid = check_personal_code(personal_id_entry)
    validation_result_row["text"] = is_valid

def generate_personal_id():
    gender = generate_id_gender_field.get()
    day_of_birth = generate_id_birth_field.get()
    generated_id = generate_personal_code(
        gender,
        day_of_birth
    )
    generation_result_row["text"] = generated_id

validate_id_label = Label(task_window, text="Įveskite asmens kodą")
validate_id_field = Entry(task_window)
validation_result_row = Label(task_window, text="")
validate_button = Button(task_window, text="Tikrinti", command=validate_personal_id)

generate_id_gender_label = Label(task_window, text="Įveskite lytį (moteris/vyras)")
generate_id_gender_field = Entry(task_window)
generate_id_birth_label = Label(task_window, text="Įveskite gimimo datą formatu YYYY-MM-DD")
generate_id_birth_field = Entry(task_window)
generation_result_row = Label(task_window, text="")
tkinter.Radiobutton()

generate_button = Button(task_window, text="Generuoti", command=generate_personal_id)

validate_id_label.grid(row=0, column=0, sticky=E)
validate_id_field.grid(row=0, column=1)
validate_button.grid(row=0, column=2)
validation_result_row.grid(row=1, columnspan=3)
generate_id_gender_label.grid(row=2, column=0, sticky=E)
generate_id_gender_field.grid(row=2, column=1)
generate_id_birth_label.grid(row=3, column=0, sticky=E)
generate_id_birth_field.grid(row=3, column=1)
generate_button.grid(row=4, columnspan=3)
generation_result_row.grid(row=5, columnspan=3)

task_window.mainloop()


# if __name__ == '__main__':
#    print_hi('PyCharm')
