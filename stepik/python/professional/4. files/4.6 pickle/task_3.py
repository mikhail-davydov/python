import pickle


def filter_dump(filename: str, objects: list[object], typename: type):
    objects_filtered = list(filter(lambda obj: isinstance(obj, typename), objects))
    with open(filename, 'wb') as o_file:
        pickle.dump(objects_filtered, o_file)