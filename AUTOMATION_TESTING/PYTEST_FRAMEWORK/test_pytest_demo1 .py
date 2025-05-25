import pytest

class Test_demo1:
    def test_name_comparision(self):
        act_name="srini midde"
        assert act_name=="srini midde","Name mismatch"
    def test_phone_no_comp(self):
        act_phone="7799132754"
        assert act_phone=="7799132754",'Phone number mismatch'
    def test_equal_numbers_comp(self):
        a=100
        b=200
        c=a+b
        assert c==300,"Numbers mismatch"