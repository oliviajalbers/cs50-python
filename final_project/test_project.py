from project import add, remove, update, sort_book

def test_add():
    assert add('olivia', '111') == [{'name': 'olivia', 'number': '111'}]
    assert add('matt', '222') == [{'name': 'matt', 'number': '222'}, {'name': 'olivia', 'number': '111'}]

def test_remove():
    remove('olivia')
    remove('matt')
    add('sue', '333')
    add('matt', '222')
    assert remove('sue') == [{'name': 'matt', 'number': '222'}]

def test_update():
    assert update('matt', 'matteo', '212') == [{'name': 'matteo', 'number': '212'}]

def test_sort_book():
    assert sort_book([{'name': 'olivia', 'number': '111'}, {'name': 'matt', 'number': '222'}]) == [{'name': 'matt', 'number': '222'}, {'name': 'olivia', 'number': '111'}]

