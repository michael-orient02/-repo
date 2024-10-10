# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 * 1024 * 1024
volume_in_symbol = 4
page = 100
line = 50
symbol_in_line = 25
volume_in_book = volume_in_symbol * symbol_in_line * line * page
total_book = round(volume // volume_in_book)

print("Количество книг, помещающихся на дискету:", total_book)
