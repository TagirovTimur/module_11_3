def introspection_info(obj):
    obj_type = type(obj).__name__

    attribut = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    method = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    module = obj.__module__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attribut,
        'methods': method,
        'module': module
    }

    return info

class One_test:

    def __init__(self,test):
        self.test = test

object_test = One_test(42)

number_info = introspection_info(object_test)
print(number_info)