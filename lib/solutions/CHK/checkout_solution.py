

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_price = {
        "A" : 50,
        "B" : 30,
        "C" : 20,
        "D" : 15
    }

    sku_offers = {

        "A" : (3, 130),
        "B" : (2, 45)
    }

    skus_list = skus.split(',')

    sku_items = {}

    for sku in skus_list:
        if sku not in sku_price:
            return -1
        sku_items[sku] = sku_items.get(sku,0) + 1
    
    basket_total = 0

    for sku, items in sku_items.items():
        price = sku_price[sku]

        if sku in sku_offers:
            bundle, disc_price = sku_offers[sku]
            valid_bundles = items // bundle
            leftover_items = items % bundle
            basket_total += (valid_bundles * disc_price) + (leftover_items * price)
        else:
            basket_total += items * price

    return basket_total 


