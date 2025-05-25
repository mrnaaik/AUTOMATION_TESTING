import pytest

class Test_parameteriz_demo:
    @pytest.mark.parametrize("num1,num2",[(100,100),(200,200),(300,300),(1000,500)])
    def test_numbers_equality_test(self,num1,num2):
        assert num1==num2,"NUMBERS ARE UNEQUAL"
    @pytest.mark.parametrize("str1,str2",[("venkat","venkat"),("srini","srini"),("manish","midde")])
    def test_string_comparisions(self,str1,str2):
        assert str1==str2,"STRINGS ARE UNEQUAL"