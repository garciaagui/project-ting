def get_ocurrences(word, archive, function):
    ocurrences = list()

    for index, line in enumerate(archive['linhas_do_arquivo']):
        if word.lower() in line.lower():
            value = (
                {"linha": index + 1}
                if function == 'exists_word'
                else {"linha": index + 1, "conteudo": line}
            )

            ocurrences.append(value)

    return ocurrences


def exists_word(word, instance):
    results = list()

    for index in range(instance.__len__()):
        archive = instance.search(index)

        ocurrences = get_ocurrences(word, archive, "exists_word")

        if ocurrences:
            results.append({
                "palavra": word,
                "arquivo": archive['nome_do_arquivo'],
                "ocorrencias": ocurrences,
            })

    return results


def search_by_word(word, instance):
    results = list()

    for index in range(instance.__len__()):
        archive = instance.search(index)

        ocurrences = get_ocurrences(word, archive, "search_by_word")

        if ocurrences:
            results.append({
                "palavra": word,
                "arquivo": archive['nome_do_arquivo'],
                "ocorrencias": ocurrences,
            })

    return results
