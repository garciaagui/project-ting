import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(instance.__len__()):
        value = instance.search(index)
        if value["nome_do_arquivo"] == path_file:
            return None

    lines = txt_importer(path_file)
    value_to_enqueue = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(value_to_enqueue)
    print(f"{value_to_enqueue}", file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
