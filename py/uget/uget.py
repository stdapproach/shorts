

def uget(data, keys: list):
    """This function provides unified access via list of indexes to complex data
    Support the sequence accessing for dict/tuple/list by index
    @param data The complex data itself
    @param keys list of indexes for accessing the data. string key correspond for accessing to the dict,
        int key provides access to tuple/list by index
    """
    if keys is None:
        return data  # nothing to access
    if keys == []:
        return data  # nothing to access
    it = data  # iterator over complex data
    if data is None:
        return None  # nothing to access
    for key in keys:
        if key is None:
            return None  # no way for further accessing
        if it is None:
            return None  # no way for further accessing
        if isinstance(it, dict):
            if key in it:
                it = it[key]
            else:
                return None
        elif isinstance(it, list) or isinstance(it, tuple):
            if isinstance(key, int):
                it = it[key]
            else:
                return None  # supports integer index accessing list/tuple for
            pass
        else:
            return None  # unsupported type here
        pass

    return it