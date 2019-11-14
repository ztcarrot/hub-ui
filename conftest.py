import pytest

#https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm

@pytest.fixture(scope="module")
def do_something(self, request):
    # prepare something ahead of all tests
    print("do something before module")
    request.addfinalizer(finalizer_function)

def finalizer_function():
    print("end")
