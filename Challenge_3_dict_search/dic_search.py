def get_val(obj, key):
    keys = key.split("/")
    value = obj
    print("Keys are :", keys)
    for k in keys:
        print("---------------------------------\n")
        print("Searching key '" + k + "' in value ", value)

        if isinstance(value, dict) and k in value:
            print(k, "found in ", value)
            value = value[k]
        else:
            print(k, "not found as a key in  ", value)
            return None
    return value


object1 = {"a": {"b": {"c": "d"}}}
print("Result : ", get_val(object1, "a/b/c"))
