# Defines a @singleton decorator

def singleton(cls):
    """
    Decorator restricting the following class to have 1 instance at most.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        cls.unregister_singleton = lambda: instances.clear()

        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
