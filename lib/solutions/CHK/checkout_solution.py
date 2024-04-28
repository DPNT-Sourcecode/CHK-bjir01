

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
        "E" : 40
    }

    bundle_offers = {

        "A" : [(5, 200), (3, 130)],
        "B" : [(2, 45)]
    }

    free_item_offers = {
        "E": (2, 'B')
    }
    #skus_list = skus.split(',')

    sku_items = {}

    for sku in skus:
        if sku not in sku_price:
            return -1
        sku_items[sku] = sku_items.get(sku,0) + 1
    
    basket_total = 0

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
                leftover_items = items % bundle_count
                basket_total += (valid_bundles * disc_price)
            basket_total +=  (leftover_items * price)
        else:
            basket_total += items * price

    return basket_total 




