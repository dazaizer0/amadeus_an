import aLib as ai
import random

def GEN_2VAL_LIST(short_temp):
    """
    Generate list with random data
    :param short_temp:
    :return:
    """
    while short_temp[0] == short_temp[1]:
        short_temp = [random.randint(5, 100), random.randint(5, 100)]

    return short_temp

def GEN_2VAL_LISTS_ANSWERS(number_of_lists, x_list: list, answer_list: list):
    """
    Generate answers to data list
    :param number_of_lists:
    :param x_list:
    :param answer_list:
    :return:
    """
    for i in range(0, number_of_lists):
        short_temp = [0, 0]
        short_temp = GEN_2VAL_LIST(short_temp)

        if short_temp[0] > short_temp[1]:
            answer_list.append(False)
        else:
            answer_list.append(True)

        x_list.append(short_temp)