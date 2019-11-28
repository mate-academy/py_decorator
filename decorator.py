'''
Module
'''


def hide(funct):
    '''

    :param fnctn:
    :return:
    '''
    def decorat(number):
        '''

        :param number:
        :return:
        '''
        if number < 5:
            number *= 2
        number = funct(number)
        if number % 2:
            number += 1
            return number
        return number
    return decorat


@hide
def fnctn(number):
    '''

    :param x:
    :return:
    '''
    return number + 5
