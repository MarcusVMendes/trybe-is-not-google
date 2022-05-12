from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if path_file in instance.data:
        return None
    instance.enqueue(path_file)
    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    print(data, file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        deleted = instance.dequeue()
        sys.stdout.write(f'Arquivo {deleted} removido com sucesso\n')


def file_metadata(instance, position):
    if position >= len(instance) or position < 0:
        sys.stderr.write("Posição inválida")
    else:
        file = txt_importer(instance.data[position])
        data = {
            "nome_do_arquivo": instance.data[position],
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
        sys.stdout.write(f"{data}")
