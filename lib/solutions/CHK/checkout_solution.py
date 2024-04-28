

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if type(skus) != str:
        return -1

    sku_price = {
        "A" : 50,
        "B" : 30,
        "C" : 20,
        "D" : 15,
        "E" : 40,
        "F" : 10,
        "G" : 20,
        "H" : 10,
        "I" : 35,
        "J" : 60,
        "K" : 70,
        "L" : 90,
        "M" : 15,
        "N" : 40,
        "O" : 10,
        "P" : 50,
        "Q" : 30,
        "R" : 50,
        "S" : 20,
        "T" : 20,
        "U" : 40,
        "V" : 50,
        "W" : 20,
        "X" : 17,
        "Y" : 20,
        "Z" : 21
    }

    bundle_offers = {

        "A" : [(5, 200), (3, 130)],
        "B" : [(2, 45)],
        "F" : [(3, 20)],
        "H" : [(10, 80), (5, 45)],
        "K" : [(2, 120)],
        "P" : [(5, 200)],
        "Q" : [(3, 80)],
        "U" : [(4, 120)],
        "V" : [(3, 130), (2, 90)]
    }

    free_item_offers = {
        "E": (2, 'B'),
        "N": (3, 'M'),
        "R": (3, 'Q')
    }
   
    group_item_offers = {
       "ZSTYX" : (3, 45)

   }

    sku_items = {}

    for sku in skus:
        if sku not in sku_price:
            return -1
        sku_items[sku] = sku_items.get(sku,0) + 1
    
    basket_total = 0

    '''
    Handle the group items from basket before calculating total
    '''

    for sku_list, offer in group_item_offers.items():
        grouped_items, disc_price = offer
    
        total_group = 0
        for sku in sku_list:
            total_group += sku_items.get(sku, 0)
        
        valid_group = total_group // grouped_items

        basket_total += valid_group * disc_price

        deduct_items = valid_group * grouped_items

        for sku in sku_list:
            if sku in sku_items:
                sku_count = sku_items[sku]
                sku_items[sku] = max(sku_count-deduct_items, 0)
                deduct_items = max(deduct_items - sku_count, 0)




    '''
    Deduct the free items from basket before calculating total
    '''

    for sku, offer in free_item_offers.items():
        req_item, free_sku = offer
        if sku in sku_items and free_sku in sku_items:
            sku_count = sku_items[sku]
            valid_free = sku_count // req_item
            sku_items[free_sku] = max(0, sku_items[free_sku] - valid_free)


    for sku, items in sku_items.items():
        price = sku_price[sku]

        if sku in bundle_offers:
            leftover_items = items
            for bundle in bundle_offers[sku]:
                bundle_count, disc_price = bundle
                valid_bundles = leftover_items // bundle_count
                leftover_items = leftover_items % bundle_count
                basket_total += (valid_bundles * disc_price)
            basket_total +=  (leftover_items * price)
        else:
            basket_total += items * price

    return basket_total 


