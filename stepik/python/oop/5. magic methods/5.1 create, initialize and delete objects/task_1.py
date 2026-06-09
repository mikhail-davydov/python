class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, program_name='GenerationPy', environment='release', loglevel='verbose', version='1.0.0'):
        self.version = version
        self.loglevel = loglevel
        self.environment = environment
        self.program_name = program_name


# alt
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.program_name = 'GenerationPy'
            cls._instance.environment = 'release'
            cls._instance.loglevel = 'verbose'
            cls._instance.version = '1.0.0'
        return cls._instance


config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)

print(10 * '-')

config1 = Config()
config2 = Config()
config3 = Config()

print(config1 is config2)
print(config1 is config3)
