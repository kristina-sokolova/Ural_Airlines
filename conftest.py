def pytest_addoption(parser):
    parser.addoption("--local",action="store_true")
    parser.addoption("--bv", default="128")
    parser.addoption("--executor", default="127.0.0.1")
