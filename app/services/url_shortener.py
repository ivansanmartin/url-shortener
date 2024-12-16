from app.db.repositories.url_shortener_repository import UrlShortenerRepository

class UrlShortenerService:
    def __init__(self, url_shortener_repository: UrlShortenerRepository):
        self.url_shortener_repository = url_shortener_repository
    
    def get_shortener(self):
        return self.url_shortener_repository.get_shortener()
    
    def create_shortener(self):
        return self.url_shortener_repository.create_shortener()