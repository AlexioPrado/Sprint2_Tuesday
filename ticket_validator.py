def validate_ticket(code):
    if isinstance(code, str):
        pass
    else:
        raise TypeError("Invalid ticket")
    
    if code[0] != "T" or code[1] != "K":
        return False
    elif (len(code) > 8 or len(code) < 8):
        return False

    for value in code[2:]:
        if value.isdigit():
            continue
        else:
            return False
        
def get_ticket_tier(code):
    pass

def calculate_total(prices, discount = 0):
    pass