import random, datetime

def extract_numbers(personal_code):   
    personal_code = str(personal_code)
    
    check_control_number = personal_code[10]
    check_control_number = int(check_control_number)
    
    check_previous_numbers = personal_code[:10]
    check_previous_numbers = int(check_previous_numbers)
    
    return check_control_number, check_previous_numbers

def count_control_number(number_to_count_from): 
    number_to_count_from = str(number_to_count_from)
    control_counter = 1
    control_number = 0 
    
    remainder = get_remainder(number_to_count_from, control_counter)    
    if remainder == 10:
        control_counter = 3
        remainder = get_remainder(number_to_count_from, control_counter)
        if remainder == 10:
            return control_number
        else:
            control_number = remainder
            return control_number
    else:
        control_number = remainder
        return control_number
        
def get_remainder(number_to_count_from, control_counter):   
    amount = 0
    for number in number_to_count_from:
        number = int(number)
        number = number * control_counter
        if control_counter != 9:
            control_counter += 1
        else:
            control_counter = 1
        amount = amount + number
        
    remainder = amount % 11
    return remainder  

def get_gender(gender):
    gender = gender.lower()
    wrong_input = f"Blogai įvedėte lytį"
    if gender == "moteris" or gender == "vyras":
        return gender
    else:
        return wrong_input    

def get_birth_date(day_of_birth):
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(day_of_birth, format)
        return day_of_birth
    except ValueError as e:
        raise e
    
def generate_personal_code(gender, day_of_birth):
    incorrect_day_of_birth = f"Neteisingas įvestos datos formatas"
    gender = get_gender(gender)
    if gender == "moteris" or gender == "vyras":
        try:
            day_of_birth = get_birth_date(day_of_birth)
        except ValueError as e:
            return incorrect_day_of_birth
        
        day_of_birth = str(day_of_birth)
        year_of_birth = day_of_birth[:4]
        certain_year = day_of_birth[2:4]
        month_of_birth = day_of_birth[5:7]
        day_of_birth = day_of_birth[8:10]
        six_digits_day_of_birth = f"{certain_year}{month_of_birth}{day_of_birth}"

        age = extract_age(year_of_birth)
        first_number = generate_first_number(gender, age)

        queue = day_of_birth_queue()

        first_ten_digits = f"{first_number}{six_digits_day_of_birth}{queue}"

        control_number = count_control_number(first_ten_digits)

        new_personal_code = f"{first_ten_digits}{control_number}"
        return new_personal_code
    else:
        return gender
    
def day_of_birth_queue():
    queue = random.randint(1, 999)
    if queue < 10:
        queue = str(queue)
        queue = f"00{queue}"
    elif queue > 9 and queue < 100:
        queue = str(queue)
        queue = f"0{queue}"
    else:
        queue
    return queue
    
def generate_first_number(gender, age):

    gender = gender.lower()
    first_number = 0
    if gender == "vyras":
        if age == 1800:
            first_number = 1
        elif age == 1900:
            first_number = 3
        else:
            first_number = 5
    else:
        if age == 1800:
            first_number = 2
        elif age == 1900:
            first_number = 4
        else:
            first_number = 6
    
    first_number = str(first_number)
    return first_number
    
def extract_age(year_of_birth):
    age = year_of_birth[:2]
    age = f"{age}00"
    age = int(age)
    return age
    
def check_personal_code(personal_code):
    personal_code_is_valid = f"Asmens kodas teisingas"
    personal_code_is_not_valid = f"Asmens kodas neteisingas"
    pc_too_short = f"Įvestas asmens kodas yra per trumpas (trūksta skaitmenų)"
    pc_too_long = f"Įvestas asmens kodas yra per ilgas (per daug skaitmenų)"
    
    pc_length = len(personal_code)
    if pc_length > 11:
        return pc_too_long
    elif pc_length < 11:
        return pc_too_short
    else:
        get_numbers = extract_numbers(personal_code)

        for number in get_numbers:
            if number > 9:
                control_number = count_control_number(number)          
            else:
                control_code = number

        if control_code == control_number:
            return personal_code_is_valid
        else:
            return personal_code_is_not_valid