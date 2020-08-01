from services.movies.files_handlers import MoviesCsvHandler
from services.movies.ploter import StaticPlots
from services.movies.service import MoviesService


class ServicesFactorie:
    
    def get_movies_static_analyse_service(self) -> MoviesService:
        return MoviesService(
            files_handler=MoviesCsvHandler(),
            ploter=StaticPlots()
        )
