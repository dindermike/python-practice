# Various Exception statement exercises.


print('Check If A String Is A Number?')


def is_number(this_str=''):
    """
    Check if a String is a Number.

    :param this_str: String, any string to check.
    :returns: True/False.
    :rtype: boolean
    """
    value = False

    try:
        float(this_str)
    except (ValueError, TypeError):
        print(f'The String "{this_str}" is NOT a Number!')
    else:
        print(f'The String "{this_str}" IS a Number.')
        value = True

    return value


is_number('Dinder')
is_number('14')
is_number('28.76')

print('--------------------------------------------------')
