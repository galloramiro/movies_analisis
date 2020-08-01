import matplotlib.pyplot as plt
from pandas import DataFrame
import seaborn as sns
from seaborn.axisgrid import FacetGrid

from services.constants import Columns


class StaticPlots:
    
    def __init__(self):
        sns.set()
        self._HEIGHT = 4
        self._ASPECT = 4.5
    
    def plot_reveneu_vs_budget(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.budget.value, y=Columns.revenue.value, data=data,
        )
        plot.set_axis_labels("Budget (M)", "Revenue (M)")
        plot.fig.suptitle("Movies: Reveneu vs Budget by Year")
        return plot

    def plot_popularity_vs_budget(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.budget.value, y=Columns.popularity.value, data=data,
        )
        plot.set_axis_labels("Popularity (K)", "Budget (M)")
        plot.fig.suptitle("Movies: Popularity vs Budget by Year")
        return plot
    
    def plot_reveneu_vs_votes_average(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.vote_average.value, y=Columns.revenue.value, data=data,
        )   
        plot.set_axis_labels("Votes Average (?)", "Revenue (M)")
        plot.fig.suptitle("Movies: Reveneu vs Votes Average by Year")
        return plot
    
    def plot_popularity_vs_votes_average(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.vote_average.value, y=Columns.popularity.value, data=data,
        )   
        plot.set_axis_labels("Votes Average (?)", "Popularity (K)")
        plot.fig.suptitle("Movies: Popularity vs Votes Average by Year")
        return plot
    
    def plot_budget_vs_votes_average(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.vote_average.value, y=Columns.budget.value, data=data,
        )   
        plot.set_axis_labels("Votes Average (?)", "Budget (M)")
        plot.fig.suptitle("Movies: Budget vs Votes Average by Year")
        return plot
    
    def _make_lmplot_by_year(self, x: str, y: str, data: DataFrame) -> FacetGrid:
        plot = sns.lmplot(
            x=x,
            y=y,
            hue=Columns.release_year.value,
            data=data,
            height=self._HEIGHT,
            aspect=self._ASPECT,
        )
        return plot
