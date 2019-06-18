class Config:
    """
    general configuration parent class
    """
    MOVIE_API_BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}"
    pass
class ProdConfig(Config):
    """
    production configuration child
    
    Args:
        config: The parent configuration class with General configuration settings
    """
    pass
class DevConfig(Config):
    """
    Development configuration child class
    
    Args:
        config: the parent configuration class with General configuration settings
    """
    DEBUG=True