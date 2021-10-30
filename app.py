import hug

@hug.get('/happy_birthday')
def happy_birthday):
    """Says happy birthday to a user"""
    return "Hello folks"