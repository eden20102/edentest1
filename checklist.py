def check_list(x):
    for element in x:
        if not isinstance(element, int):
            raise ValueError(
                "all elements of the list must be of type int")

        elif not 1 <= int(element) <= 100:
            raise ValueError(
                "all elements of the list must be between 1-100")


x=[1,2,3,4,1,3]