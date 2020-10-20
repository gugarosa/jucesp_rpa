import configparser

from twocaptcha import TwoCaptcha

# Initializes and reads the configuration object
config = configparser.ConfigParser()
config.read('config.ini')

# Defines the 2Captcha's API key
CAPTCHA_KEY = config.get('KEY', '2CAPTCHA_KEY')


def solve(file_path):
    """Solves an image-based captcha.

    Args:
        file_path (str): Path to the captcha that will be solved.

    Returns:
        The string from the solved captcha or an exception if any error has occured.

    """

    # Instantiates the 2Captcha's solver
    solver = TwoCaptcha(CAPTCHA_KEY)

    # Tries to perform the following block
    try:
        # Solves the captcha
        result = solver.normal(file_path)

        # Returns the solved captcha
        return result['code']

    # If an exception has been raised
    except Exception as e:        
        # Returns the exception
        return e
