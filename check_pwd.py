# CS362
# A2: TDD Hands On
# by Kongkom Hiranpradit ONID ID: hiranprk
# 12 November 2023

def check_pwd(pwd):

    """ rule 1: Must be between 8 and 20 characters (inclusive) """
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    else:
        return True
