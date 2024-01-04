class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}