def exists_word(word, instance):
    word_to_lower = word.lower()
    result_from_word = list()
    word_occurrence = list()
    for element in instance.line:
        repeated_word = 0
        for text in element['linhas_do_arquivo']:
            repeated_word += 1
            if word_to_lower in text.lower():
                word_occurrence.append({"linha": repeated_word})
        if len(word_occurrence) == 0:
            return word_occurrence
        response = {
            "palavra": word.lower(),
            "arquivo": element['nome_do_arquivo'],
            "ocorrencias": word_occurrence
        }
        result_from_word.append(response)
    return result_from_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
