def exists_word(word, instance):
    results = list()

    for index in range(instance.__len__()):
        archive = instance.search(index)
        ocurrences = list()

        for index, line in enumerate(archive['linhas_do_arquivo']):
            if word.lower() in line.lower():
                ocurrences.append({"linha": index + 1})

        if ocurrences:
            results.append({
                "palavra": word,
                "arquivo": archive['nome_do_arquivo'],
                "ocorrencias": ocurrences,
            })

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
