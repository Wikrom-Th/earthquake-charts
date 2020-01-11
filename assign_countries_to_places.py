# rename the known pan-asia regions into countries 
import csv

# function to check if the string is a substring (not case-sensitive) of another string
def chk_substr_not_case_sens(str_to_check, main_str):
    check_len = len(str_to_check)
    main_len = len(main_str)

    if check_len > main_len:
        return False
    elif check_len == main_len:
        if str_to_check.lower() == main_str.lower():
            return True
        else:
            return False
    else:
        # TODO: check substring when check_len < main_len (this one always returns false, but that's not always the case) 
        return False

# with open('./eq_data/other_eqs.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     count = 0
#     for row in reader: