from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('janis','joplin')
    assert formatted_name=='janis joplin'.title()

def test_first_last_middle_name():
    formatted_name=get_formatted_name('walfgang','mozart','adm')
    assert formatted_name =='walfgang adm mozart'.title()
    