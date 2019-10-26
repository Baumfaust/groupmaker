#!/usr/bin/python3

import csv

input = ['resell', 'engineer', 'alchemy', 'recipes']

for group in input:
    with open('source/items.csv', 'r') as items_file, open(str(group)+'.txt', 'r') as search_file:
        items = csv.reader(items_file)
        search_items = search_file.read().splitlines()
        search_items_count = 0
        items_found_count = 0
        items_found = []
        not_found = []

        for search_item in search_items:
            if not search_item or search_item.isspace() :
                continue
            search_items_count += 1
            items_file.seek(0)
            found = False
            for num, item in enumerate(items, start=1):
                if search_item.lower() == item[1].lower():
                    items_found.append([item[1],item[0], 'https://de.classic.wowhead.com/item='+item[0], 'https://www.bootybaygazette.com/#eu/lucifron-h/item/'+item[0]])
                    items_found_count += 1
                    found = True
                    break
            if not found:
                not_found.append(search_item)

    with open('results_'+group+'.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['Name', 'ID', 'Wowhead Classic', 'Booty Bay Gazette'])
        for row in items_found:
            writer.writerow(row)

    print('TSM group: '+group)
    for i in items_found:
        print('i:'+i[1]+',', sep='', end='', flush=True)

    print('\n')
    print("Valid search items: " + str(search_items_count))
    print("Items found + added: " + str(items_found_count))
    print('===========================================')

    for i in not_found:
        print(i)