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