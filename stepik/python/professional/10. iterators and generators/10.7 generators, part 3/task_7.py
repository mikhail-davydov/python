def txt_to_dict():
    try:
        with open('planets.txt', encoding='u8') as i_file:
            while True:
                yield dict([next(i_file).strip().split(' = ') for _ in range(4)])
                next(i_file)
    except:
        pass


planets = txt_to_dict()

print(*planets)


# alt
def planet_features(file):
    features = {}
    for _ in range(4):
        key, value = file.readline().strip().split(' = ')
        features[key] = value
    return features


def txt_to_dict():
    with open('planets.txt') as file:
        line = 'lets some yield'
        while line:
            yield planet_features(file)
            line = file.readline()
