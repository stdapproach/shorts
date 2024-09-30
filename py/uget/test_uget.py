from uget import uget


def test_null_data():
    data = None
    actual = uget(data, None)
    expected = None
    assert actual == expected


def test_data_with_null_keys():
    data = 42
    actual = uget(data, None)
    expected = 42
    assert actual == expected


def test_data_with_empty_keys():
    data = 42
    actual = uget(data, [])
    expected = 42
    assert actual == expected


def test_data_with_null_key():
    data = 42
    actual = uget(data, [None])
    expected = None
    assert actual == expected


def test_data_with_null_data_nonnull_key():
    data = None
    actual = uget(data, [42])
    expected = None
    assert actual == expected


def test_data_with_null_data_null_key():
    data = None
    actual = uget(data, [None])
    expected = None
    assert actual == expected


def test_data_simple_dict():
    data = {"key": 42}
    actual = uget(data, [None])
    expected = None
    assert actual == expected


def test_data_simple_dict2():
    data = {"key": 42}
    actual = uget(data, ["key"])
    expected = 42
    assert actual == expected


def test_data_dict_empty():
    data = {}
    actual = uget(data, ["key"])
    expected = None
    assert actual == expected


def test_data_dict_without_desired_key():
    data = {"42": 42}
    actual = uget(data, ["key"])
    expected = None
    assert actual == expected


def test_data_list_empty():
    data = []
    actual = uget(data, ["key"])
    expected = None
    assert actual == expected


def test_data_list_nonempty_access_by_string():
    data = [42]
    actual = uget(data, ["key"])
    expected = None
    assert actual == expected


def test_data_list_nonempty_access_by_int():
    data = [42]
    actual = uget(data, [0])
    expected = 42
    assert actual == expected


def test_data_tuple_empty():
    data = ()
    actual = uget(data, ["key"])
    expected = None
    assert actual == expected


def test_data_tuple_nonempty_access_by_string():
    data = (42)
    actual = uget(data, ["key"])
    expected = None
    assert actual == expected


def test_data_tuple_nonempty_access_by_int():
    data = (0, 42)
    actual = uget(data, [1])
    expected = 42
    assert actual == expected


def test_data_access_dict_list_tuple():
    data = {
        "first": None,
        "second": [(41, 42), (43, 44)],
        "third": None,
    }
    actual = uget(data, ["second", 0, 1])
    expected = 42
    assert actual == expected


def test_data_access_list_tuple_dict():
    struct = {
        "first": None,
        "second": [(41, 42), (43, 44)],
        "third": None,
    }
    data = [(None, None), (None, None), (None, struct)]

    actual = uget(data, [2, 1, "second", 0, 1])
    expected = 42
    assert actual == expected
