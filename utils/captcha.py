from twocaptcha import TwoCaptcha


def break_captcha(key, file_path):
    """
    """
    
    #
    solver = TwoCaptcha(key)

    #
    try:
        #
        result = solver.normal(file_path)

        #
        return result

    #
    except Exception as e:
        #
        return e
