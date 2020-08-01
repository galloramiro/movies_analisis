from services.movies.files_handlers import MoviesCsvHandler
from services.movies.ploter import StaticPlots, InteractivePlot
from services.movies.service import MoviesService


class ServicesFactorie:
    
    def get_static_movies_analyse_service(self) -> MoviesService:
        return MoviesService(
            files_handler=MoviesCsvHandler(),
            ploter=StaticPlots()
        )
    
    def get_interactive_movies_analyse_service(self) -> MoviesService:
        return MoviesService(
            files_handler=MoviesCsvHandler(),
            ploter=InteractivePlot()
        )
