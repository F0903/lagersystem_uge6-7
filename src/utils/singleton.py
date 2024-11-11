def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        cls.unregister_singleton = lambda: instances.clear()

        if cls not in instances:
            instance = cls(*args, **kwargs)
            instances[cls] = instance
        return instances[cls]

    def unregister_singleton():
        """Reset the singleton instance."""
        instances.pop(cls)
        print()

    get_instance.unregister_singleton = unregister_singleton
    return get_instance
