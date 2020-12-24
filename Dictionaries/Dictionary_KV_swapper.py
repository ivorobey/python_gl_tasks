# You need to write a function for swapping key/values in given dictionary. In other words, values in old dict should become keys on new dict and their values should be original corresponding keys.
# The function should take a dict as input and return a new dict.

# Example:

# a = {"key1: 25, 100: "value100"}
# dict_swap(a)
# should resulted this dict:

# {25: "key1", "value100": 100}
# Advanced task: * One of the test cases will be the situation where the value can't be a key (because it's not hashable).
# You can check for allowed types or check is it have __hash__ method or simply use try/except to handle this case (by not adding this such key to resulted dict).


data = {"key1": 25, 100: "value100", "cadabra": "abra",
        (1, 2): (3, 4), "shmobject": object, False: None}


def dict_swap(data):
    new_dict = dict()

    new_dict = dict([(value, key)
                     for key, value in data.items()if value.__hash__])
    return new_dict


print(dict_swap(data))
