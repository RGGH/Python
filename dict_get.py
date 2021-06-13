dict = {'canonical_url': '/search', 'breadcrumbs': [], 'nbHits': 1, 'nbPages': 1, 
'facets': [], 'search': {'sort': {}}, 


'hits': [{'offer_no': 'd6b6ff88d6d06gne', 
'sku': 'N23347560A', 'sku_config': 'S23346660A', 'brand': 'Missino', 
'name': 'Ceramic Non Stick Casserole Pot With Lid Plum/Clear/Blue 320mm ', 
'abc_specifications': {}, 'price': 75, 'sale_price': None, 
'url': 'ceramic-non-stick-casserole-pot-with-lid-plum-clear-blue-320mm', 
'image_key': 'v15553306gne2/N2334706gneA_1', 'is_buyable': True, 'product_badges': [], 
'plp_product_group_code': 'N2334706gneA', 'flags': ['fbn'], 'catalog_tag_style': 'default', 
'catalog_tag_type': 'Yellow',
 'catalog_tag': '10% off on orders over 300 use code : SAVING (Max 50 AED)', 
 'delivery': 'Arrives <em>Sat, Jun 12</em>', 'groups': []}],
 
  
'meta': {'search_all_category': False}, 'cms': {}, 'type': 'catalog'}

name = dict.get('hits')[0].get('name','uh uh - no such key:value ')

#example_dict.get('key1', {}).get('key2')

print(name)
