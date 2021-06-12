import ClientClass

def debug_print(text: str):
    print(f'Debug: {text}')

def assert_type(variable, type):
    assert isinstance(variable, type), f'{variable} must be {type}'