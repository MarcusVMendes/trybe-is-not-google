import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    else:
        try:
            with open(path_file) as file:
                return [item.strip("\n") for item in file]
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
