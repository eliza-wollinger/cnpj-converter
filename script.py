import re
import random
import string

def convert_cnpj_to_new_format(cnpj: str) -> str:

    cnpj_numeric = re.sub(r'\D', '', cnpj)
    
    if len(cnpj_numeric) != 14:
        raise ValueError("Invalid CNPJ: must contain 14 numeric digits")

    new_root = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    new_branch = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    verification_digits = cnpj_numeric[-2:]
    new_cnpj = f"{new_root[:2]}.{new_root[2:5]}.{new_root[5:8]}/{new_branch}-{verification_digits}"
    
    return new_cnpj

# Example usage
old_cnpj = "11.222.333/0001-81"
new_cnpj = convert_cnpj_to_new_format(old_cnpj)
print(new_cnpj)  # Example output: AB.12C.D34/EF56-81
