"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    setattr(cls, 'counter', 0)

    def __init__(self):
        super(cls, self).__init__()
        cls.counter += 1

    @classmethod
    def get_created_instances(cls):
        return cls.counter

    @classmethod
    def reset_instances_counter(cls):
        counts, cls.counter = cls.counter, 0
        return counts

    setattr(cls, '__init__', __init__)
    setattr(cls, 'get_created_instances', get_created_instances)
    setattr(cls, 'reset_instances_counter', reset_instances_counter)
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
