import pytest
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

#------validate_ticket-------
def test_ticketValid():
    scan = validate_ticket("TK433873")
    assert scan == True

def test_ticketInvalid_TK():
    scan = validate_ticket("UK674209")
    assert scan == False

def test_ticketInvalid_String():
    with pytest.raises(TypeError):
        scan = validate_ticket(910212)
        assert scan == False

#------get_ticket_tier-------
def test_tierGeneral():
    scan = get_ticket_tier("TK023478")
    assert scan == "General"

def test_tierPlatinum_edge():
    scan = get_ticket_tier("TK987654")
    assert scan == "Platinum"

#------calculate_total-------

@pytest.mark.parametrize(([1.5, 10.75, 8.99,], 0.5),([12.45, 15.99, 3.45], 0.0),([13.40, 12.50, 60.10], 1.0))
def test_totalCalc():
    pass

def test_totalCalc_noPrice():
    price = calculate_total([], 0.1)
    assert price == None

def test_totalCalc_PriceNoList():
    price = calculate_total(12.45, 0.5)
    assert price == None

@pytest.mark.parametrize(([1.45, 51.99, 6.16], -0.9), ([1.45, 47.1, 67.67], 1.5))
def test_totalCalc_DiscountOutOfBound(prices, discount, expected):
    assert calculate_total(prices, discount) == expected