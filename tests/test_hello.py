from hello_world import hello_func

def test_hello():
    out = hello_func("jorge")

    assert out == "ola rui"
