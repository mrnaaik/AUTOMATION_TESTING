import pytest
class Test_grouping_decorator:
    @pytest.mark.regression
    def test_m1(self):
        print("iam belonging to regression testing")

    @pytest.mark.regression
    def test_m2(self):
        print("iam belonging to regression testing")

    @pytest.mark.regression
    def test_m3(self):
        print("iam belonging to regression testing")

    @pytest.mark.sanity
    def test_m4(self):
        print("iam belonging to sanity testing")

    @pytest.mark.sanity
    def test_m5(self):
        print("iam belonging to sanity testing")

    @pytest.mark.sanity
    def test_m6(self):
        print("iam belonging to sanity testing")

    @pytest.mark.smoke
    def test_m7(self):
        print("iam belonging to smoke testing")

    @pytest.mark.smoke
    def test_m8(self):
        print("iam belonging to smoke testing")

    @pytest.mark.smoke
    def test_m9(self):
        print("iam belonging to smoke testing")