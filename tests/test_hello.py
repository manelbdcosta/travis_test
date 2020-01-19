from hello_world import hello_func

def test_hello() -> None:
    out = hello_func("jorge")

    assert out == "hello jorge"
