def validate_ticket(code):
    if not isinstance(code, str):
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
    if not code[3].isdigit:
        raise ValueError

    if code[3] >= 0 or code[3] <=3:
        return "General"
    elif code[3] >=4 or code[3] <=6:
        return "VIP"
    elif code[3] >=7 or code[3] <=9:
        return "Platinum"
    

def calculate_total(prices, discount = 0):
    if prices
    if len(prices) == 0 or discount > 1 or discount < 0:
        raise ValueError