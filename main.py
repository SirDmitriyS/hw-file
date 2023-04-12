from pprint import pprint

def read_cook():
    cook_book = {}
    with open('рецепты.txt', encoding='UTF-8') as f:
      while True: 
        name = f.readline().strip()
        if name =='':
          return cook_book
        # print(name)
        cook_book[name] = []
        for a in range(int(f.readline())):
            ingr_str = f.readline().strip()
            ingr = ingr_str.split(' | ')
            # print({'ingredient_name': ingr[0] , 'quantity': ingr[1] , 'measure': ingr[2]})
            cook_book[name].append({'ingredient_name': ingr[0] , 'quantity': int(ingr[1]) , 'measure': ingr[2]})
        f.readline()
    print(cook_book)  

# cook = read_cook()
# pprint(cook,width=100,compact=True)


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            shop_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': 0})
            shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

# Merge files to one file
def merge_files(file_list, result_file_name, encoding='UTF-8'):
    content = []
    for file_name in file_list:
        with open(file_name, encoding=encoding) as file:
            file_content = file.readlines()
            content.append({'file_name': file_name, 'lines': file_content, 'lines_count': len(file_content)})
    content.sort(key=lambda file_info: file_info['lines_count'])
    with open(result_file_name, 'wt', encoding=encoding) as result_file:
        for file_content in content:
            result_file.writelines(file_content['file_name'] + '\n')
            result_file.writelines(str(file_content['lines_count']) + '\n')
            result_file.writelines(file_content['lines'])
            # To start next file section from new line
            if file_content['lines'][-1][-1] != '\n':
                result_file.writelines('\n')


cook = read_cook()
pprint(cook,width=100,compact=True)
print()

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(cook, dishes, person_count)
print(f'Список покупка для приготовления блюд {", ".join(dishes)} на {person_count} персон(ы):')
pprint(shop_list, compact=True, width=100)

file_list = ['1.txt', '2.txt', '3.txt']
merge_files(file_list, 'merged.txt')