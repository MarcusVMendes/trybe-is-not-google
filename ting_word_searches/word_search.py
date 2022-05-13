def exists_word(word, instance):
    result = list()
    for item in instance.data:
        with open(item) as file:
            lines = file.read().split("\n")
            result.append({
                "palavra": word,
                "arquivo": item,
                "ocorrencias": [],
            })
            for index, line in enumerate(lines):
                if word.lower() in line.lower():
                    result[-1]["ocorrencias"].append({
                        "linha": index + 1,
                    })
            if result[-1]["ocorrencias"] == []:
                result.pop()
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
