# Test failure - HIGH RISK
# Should create PR requiring manual review

def process_payment(amount, currency="USD"):
    """Process a payment transaction"""
    if amount <= 0:
        return False
    
    # Simulate payment processing
    fee = amount * 0.03  # 3% fee
    total = amount + fee
    
    return {
        'success': True,
        'amount': amount,
        'fee': fee,
        'total': total,
        'currency': currency
    }

def test_process_payment():
    """Test payment processing"""
    result = process_payment(100)
    
    # Wrong assertion - will fail
    assert result['total'] == 100  # Should be 103 (100 + 3% fee)
    assert result['success'] == True

def test_negative_amount():
    """Test negative amount"""
    result = process_payment(-50)
    assert result == False

if __name__ == "__main__":
    # Run tests
    test_process_payment()
    test_negative_amount()
    print("All tests passed!")
