# TODO  Напишите функцию count_letters
def count_letters(text):
    text_lower = text.lower()
    letters = [char for char in text_lower if char.isalpha()]
    letters_count = {}
    for letters in letters:
        if letters not in letters_count:
            letters_count[letters] = 0
        letters_count[letters] += 1

    return letters_count

# TODO Напишите функцию calculate_frequency


def calculate_frequency(letter_counts):
    total_letters = sum(letter_counts.values())
    frequency = {}
    for letters, count in letter_counts.items():
        frequency[letters] = count / total_letters
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_count = count_letters(main_str)

frequency_dict = calculate_frequency(letter_count)

# TODO Распечатайте в столбик букву и её частоту в тексте
for letter, freq in frequency_dict.items():
    print(f"{letter}: {freq:.2f}")
