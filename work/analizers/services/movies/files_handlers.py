from os import getcwd

import pandas as pd
from pandas import DataFrame

from services.constants import Columns


class MoviesCsvHandler:
    DATA_DIR = f"{getcwd()}/data/"
    
    def get_revenue_vs_budget_by_year_df(self, file_name: str = None) -> DataFrame:
        df = self._open_file(file_name)
        df = df[[Columns.revenue.value, Columns.budget.value, Columns.release_year.value]]
        df[Columns.release_year.value] = df[Columns.release_year.value].astype('category')
        return df
    
    def get_popularity_vs_budget_by_year_df(self, file_name: str = None) -> DataFrame:
        df = self._open_file(file_name)
        df = df[[Columns.popularity.value, Columns.budget.value, Columns.release_year.value]]
        df[Columns.release_year.value] = df[Columns.release_year.value].astype('category')
        return df
    
    def get_revenew_vs_votes_average(self, file_name: str = None) -> DataFrame:
        df = self._open_file(file_name)
        df = df[[Columns.revenue.value, Columns.vote_average.value, Columns.release_year.value]]
        df[Columns.release_year.value] = df[Columns.release_year.value].astype('category')
        return df
    
    def get_popularity_vs_votes_average(self, file_name: str = None) -> DataFrame:
        df = self._open_file(file_name)
        df = df[[Columns.popularity.value, Columns.vote_average.value, Columns.release_year.value]]
        df[Columns.release_year.value] = df[Columns.release_year.value].astype('category')
        return df
    
    def get_budget_vs_votes_average(self, file_name: str = None) -> DataFrame:
        df = self._open_file(file_name)
        df = df[[Columns.budget.value, Columns.vote_average.value, Columns.release_year.value]]
        df[Columns.release_year.value] = df[Columns.release_year.value].astype('category')
        return df
    
    def _open_file(self, file_name: str = None) -> DataFrame:
        if file_name:
            return pd.read_csv(f"{self.DATA_DIR}{file_name}")
        
        return pd.read_csv(f"{self.DATA_DIR}tmdb-movies.csv")

