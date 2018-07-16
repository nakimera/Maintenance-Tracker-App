class Config:
    SECRET_KEY = "8AZsk5bD2FQl9oXSv4fuxlRxxZnHsV4y"
    DEBUG = False
    TESTING = False 
    DEVELOPMENT = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    
configuration = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig,
    "production" : ProductionConfig
}