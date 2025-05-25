import pytest
class Test_skipp_decorator:
    @pytest.mark.skip
    def test_m1(self):
        assert True
    def test_m2(self):
        assert True
    def test_m3(self):
        assert True
    @pytest.mark.skip
    def test_m4(self):
        assert True