from seaborn.axisgrid import FacetGrid

from services.movies.files_handlers import MoviesCsvHandler
from services.movies.ploter import StaticPlots


class MoviesService:
    
    def __init__(self, files_handler: MoviesCsvHandler,  ploter: StaticPlots):
        self._file_handler = files_handler
        self._ploter = ploter
        self._LAST_FEW_YEARS = 2
        
    def get_revenue_vs_budget_analisis(self, file_name: str = None, last_few_years: int = None) -> FacetGrid:
        if last_few_years:
            self._LAST_FEW_YEARS = last_few_years

        df = self._file_handler.get_revenue_vs_budget_by_year_df(file_name, self._LAST_FEW_YEARS)
        return self._ploter.plot_reveneu_vs_budget(df)
    
    def get_popularity_vs_budget_analisis(self, file_name: str = None, last_few_years: int = None) -> FacetGrid:
        if last_few_years:
            self._LAST_FEW_YEARS = last_few_years
            
        df = self._file_handler.get_popularity_vs_budget_by_year_df(file_name, self._LAST_FEW_YEARS)
        return self._ploter.plot_popularity_vs_budget(df)
    
    def get_reveneu_vs_votes_average_analisis(self, file_name: str = None, last_few_years: int = None) -> FacetGrid:
        if last_few_years:
            self._LAST_FEW_YEARS = last_few_years
            
        df = self._file_handler.get_reveneu_vs_votes_average(file_name, self._LAST_FEW_YEARS)
        return self._ploter.plot_reveneu_vs_votes_average(df)
    
    def get_popularity_vs_votes_average_analisis(self, file_name: str = None, last_few_years: int = None) -> FacetGrid:
        if last_few_years:
            self._LAST_FEW_YEARS = last_few_years
            
        df = self._file_handler.get_popularity_vs_votes_average(file_name, self._LAST_FEW_YEARS)
        return self._ploter.plot_popularity_vs_votes_average(df)
    
    def get_budget_vs_votes_average_analisis(self, file_name: str = None, last_few_years: int = None) -> FacetGrid:
        if last_few_years:
            self._LAST_FEW_YEARS = last_few_years
            
        df = self._file_handler.get_budget_vs_votes_average(file_name, self._LAST_FEW_YEARS)
        return self._ploter.plot_budget_vs_votes_average(df)