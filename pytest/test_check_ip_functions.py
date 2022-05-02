import check_ip_functions

def test_check_ip():
    c = check_ip_functions
    result = c.check_ip('393.1.1.1')
    assert result == False

test_check_ip()
