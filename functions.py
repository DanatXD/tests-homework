def summator(a, b=0):
    return a + b


def div(a, b):
    return a / b


def flat_generator(list_of_lists):
    for inner_list in list_of_lists:
        for item in inner_list:
            yield item