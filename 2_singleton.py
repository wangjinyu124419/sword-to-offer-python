class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls, *args, **kwargs)
            return cls._instance
        return cls._instance

    def __init__(self):
        self.name='singleton'
if __name__ == '__main__':
    s1=Singleton()
    s2=Singleton()
    print(id(s1))
    print(id(s2))
    print('s1是否是s2:%r'%(s1 is s2))
