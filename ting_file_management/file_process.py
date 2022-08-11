from .file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file_data = txt_importer(path_file)
    process_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_data),
        "linhas_do_arquivo": file_data,
    }
    sys.stdout.write(str(process_data))
    instance.enqueue(process_data)


def remove(instance):
    all_list = instance.__len__()
    if all_list == 0:
        return sys.stdout.write("Não há elementos\n")
    file = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        position_validate = instance.search(position)
        sys.stdout.write(str(position_validate))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
