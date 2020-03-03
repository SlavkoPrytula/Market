import Get_notebook_items as notebook
import Notebook as note_info


def call_module():
    """Runs the module"""

    all_to_parse = []
    all_new_to_parse = []
    print(dir(notebook.Menu))
    classes_info = [note_info.Note, note_info.Notebook]
    for c in classes_info:
        print("{}: {}".format(c, dir(c)))
        for item in dir(c):
            if item.startswith("__") and item.endswith("__") and item not in all_to_parse:
                all_to_parse.append(item)

    print("\n\n")

    for i in all_to_parse:
        print("{}: {}".format(i, dir(i)))
        for item in dir(i):
            if item.startswith("__") and item.endswith("__") and item not in all_new_to_parse:
                all_new_to_parse.append(item)

    print("\n\n")

    for item in all_new_to_parse:
        print("{}: {}".format(item, dir(item)))


if __name__ == '__main__':
    call_module()
    notebook.Menu().run()
