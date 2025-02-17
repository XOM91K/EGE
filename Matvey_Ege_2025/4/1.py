def find_min_total_length(existing_codes, remaining_letters):
    if not remaining_letters:
        return sum(len(code) for code in existing_codes.values())

    min_length = float('inf')

    for letter in remaining_letters:
        for code in generate_possible_codes(existing_codes):
            new_codes = existing_codes.copy()
            new_codes[letter] = code
            new_remaining = remaining_letters.copy()
            new_remaining.remove(letter)
            current_length = find_min_total_length(new_codes, new_remaining)
            if current_length < min_length:
                min_length = current_length

    return min_length


def generate_possible_codes(existing_codes):
    used_codes = set(existing_codes.values())
    possible_codes = []

    for code in used_codes:
        possible_codes.append(code + '0')
        possible_codes.append(code + '1')

    possible_codes = list(set(possible_codes) - used_codes)
    return possible_codes


# Исходные данные
existing_codes = {'В': '101', 'М': '01'}
remaining_letters = ['Р', 'Е', 'Я']

# Находим минимальную общую длину
min_total_length = find_min_total_length(existing_codes, remaining_letters)
print(f"Минимальная общая длина кодовых слов: {min_total_length}")