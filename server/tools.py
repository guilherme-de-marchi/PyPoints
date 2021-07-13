def debug_print(text: str):
    print(f'Debug: {text}')

def assert_type(variable, type_target):
    assert isinstance(variable, type_target), f'{variable} must be {type_target}'

def for_each(iterable, function):
    for item in iterable:
        function(item)