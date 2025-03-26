# -s is used for checking logs
# -v is used for checking information on the function which ran
# @pytest.mark.smoke (any name) is used for tagging testcase/function
# -m followed by tag name is used for running/picking testcase/function

import pytest

@pytest.mark.sanity
@pytest.mark.usefixtures("setup")
class TestClass:
    def testdemo(self):
        print('hello')

    def testdemo3(self):
        print('Hi')

    def testdemo4(self):
        print('Hello Hi')

    def testdemo5(self):
        print('Hi Hello')