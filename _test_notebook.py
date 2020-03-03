import Get_notebook_items as notebook
import Notebook as note_info


def call_module():
    """Runs the module"""

    print(dir(notebook.Menu))
    classes_info = [note_info.Note, note_info.Notebook]
    for c in classes_info:
        print(dir(c))

    notebook.Menu().run()


if __name__ == '__main__':
    call_module()
