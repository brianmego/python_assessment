def ensure_in_place(func):
    """Decorator for the next question. Nothing to see here"""

    def inner(inp, inc_value):
        _orig_id = id(inp)
        _orig = inp
        response = func(inp, inc_value)
        if id(response) != _orig_id:
            return 'Whoops! Looks like you made a new item in memory!'
        return response
    return inner


