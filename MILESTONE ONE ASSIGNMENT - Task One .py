'''
Make a template using the dictionary data.
Your Template must have at least two sentences.
USD must be converted to BDT
example Output: Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
'''

mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }



name_mobile = mobile_data['data'][0]['name']
made_in = mobile_data['data'][0]['made']
mobile_price = mobile_data['data'][1]['price']
price_dollar = float(mobile_data['data'][0]['price'][:3])
bdt_convert = (price_dollar * 107.25)

x = (f'{name_mobile} is made in {made_in}. The price is {mobile_price} which is almost equal to {bdt_convert} BDT.')

print(x)



