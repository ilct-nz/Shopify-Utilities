# Shopify-Utilities

In order to use these utilities, you must have a `.credentials` file with the following format:

```
[profile name]
API_KEY = ****
PASSWORD = ****
STORE_URL_PREFIX = my-store
```

## change_template_based_on_product_type.py
Use this script to change the template of your products based on their product type.  This is helpful given that, as of July 2018, it is not possible to specify the template for products when uploading them via a csv file.

## delete_all_products.py
Use this script to delete all of the products in your store (can be modified easily to delete only products with certain attributes).

## delete_products_of_specific_product_type.py
Use this script to delete all products of a specific product type.

## change_weight_of_specific_variants_to_zero.py
Use this script to change the weight of specific variants to zero.