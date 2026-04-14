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
@pytest.mark.parametrize("prices, discount, expected",([15, 10, 9,], 0.5, 17),([12.45, 15.99, 3.45], 0, 31.89),([13.40, 12.50, 60.10], 1.0, 0))
def test_totalCalc(prices, discount, expected):
    assert calculate_total(prices, discount) == expected

def test_totalCalc_noPrice():
    with pytest.raises(ValueError):
        price = calculate_total([], 0.1)
        assert price == None

def test_totalCalc_PriceNoList():
    with pytest.raises(TypeError):
        price = calculate_total(12.45, 0.5)
        assert price == None

def test_totalCalc_DiscountOutOfBounUP():
    with pytest.raises(ValueError):
        assert calculate_total([1, 47, 67], 1.5) == None
