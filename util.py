def ensure_in_place(func):
    """Decorator for the next question. Nothing to see here"""

    def inner(inp, inc_value):
        _orig_id = id(inp)
        _orig = inp
        response = func(inp, inc_value)
        msg =  'Whoops! Looks like you made a new item in memory! See if you can alter the list in place.'
        assert id(response) == _orig_id, msg
        return response
    return inner


