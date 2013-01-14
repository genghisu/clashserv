class UnboundFormException(Exception):
    """
    Raise when an unbound form (no request data) calls a member function that requires request data
    """
    pass