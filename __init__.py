# python3 main.py




__app_name__ = "AWS Kit"
__version__ = "0.1.0"



def current_function() -> str:
    import sys
    '''
    Used for testing and debugging
    
    Will return a string displaying the function being called
    
    Example:
    - Calling the list_databases() command

    '''
    return f"Calling the {sys._getframe(1).f_code.co_name}() command"