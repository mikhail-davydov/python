import csv
from collections import defaultdict


def condense_csv(filename, id_name):
    objects = defaultdict(dict)
    properties = set()
    
    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file)
        for obj_id, prop, value in reader:
            objects[obj_id][prop] = value
            properties.add(prop)
    
    # Get properties in order of appearance
    property_order = []
    for obj_id, prop, value in csv.reader(open(filename, encoding='utf-8')):
        if prop not in property_order:
            property_order.append(prop)
    
    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow([id_name] + property_order)
        # Write data rows
        for obj_id in sorted(objects.keys()):
            row = [obj_id] + [objects[obj_id].get(prop, '') for prop in property_order]
            writer.writerow(row)