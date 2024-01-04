def my_cook_book():
  with open('__test_in.txt', encoding='utf-8') as file:
    cook_book = {}
    for txt in file.read().split('\n\n'):
        name, _, *args = txt.split('\n')
        tmp = []
        for arg in args:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
            tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[name] = tmp
  return cook_book


def get_shop_list_by_dishes(dishes, person_count):
  cook_book = my_cook_book()
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      name = ingredient['ingredient_name']
      quantity = ingredient['quantity'] * person_count
      measure = ingredient['measure']
      if name in shop_list:
        shop_list[name]['quantity'] += quantity
      else:
        shop_list[name] = {'measure': measure, 'quantity': quantity}
  return shop_list