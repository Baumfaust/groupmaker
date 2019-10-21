#!/usr/bin/python3

import csv

with open('source/items.csv', 'r') as items_file, open('search.txt', 'r') as search_file:
    items = csv.reader(items_file)
    search_items = search_file.read().splitlines()
        search_items_count = 0
    items_found = 0
    not_found = []
    for search_item in search_items:
        if not search_item or search_item.isspace() :
            continue
        search_items_count += 1
        items_file.seek(0)
        found = False
        for num, item in enumerate(items, start=1):
            if search_item.lower() == item[1].lower():
                print("i:"+item[0])
                items_found += 1
                found = True
                break
        if not found:
            not_found.append(search_item)
                
print("Valid search items: " + str(search_items_count))
print("Items : " + str(items_found))

for i in not_found:
    print(i)