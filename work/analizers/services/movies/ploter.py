import altair as alt
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

    
class InteractivePlot:
    def plot_reveneu_vs_budget(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.budget.value, y=Columns.revenue.value, data=data,
            title="Movies: Reveneu vs Budget by Year"
        )
        return plot

    def plot_popularity_vs_budget(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.budget.value, y=Columns.popularity.value, data=data,
            title="Movies: Popularity vs Budget by Year"
        )
        return plot
    
    def plot_reveneu_vs_votes_average(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.vote_average.value, y=Columns.revenue.value, data=data,
            title="Movies: Reveneu vs Votes Average by Year"
        )   
        return plot
    
    def plot_popularity_vs_votes_average(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.vote_average.value, y=Columns.popularity.value, data=data,
            title="Movies: Popularity vs Votes Average by Year"
        )
        return plot
    
    def plot_budget_vs_votes_average(self, data: DataFrame) -> FacetGrid:
        plot = self._make_lmplot_by_year(
            x=Columns.vote_average.value, y=Columns.budget.value, data=data,
            title="Movies: Budget vs Votes Average by Year"
        )   
        return plot
    
    def _make_lmplot_by_year(self, x: str, y: str, data: DataFrame, title:str) -> FacetGrid:
        click = alt.selection_multi(encodings=['color'])
        x_line = alt.X(f"{x}:Q")
        y_line = alt.Y(f"{y}:Q")
        color = alt.condition(
            click, alt.Color(
                shorthand=f"{Columns.release_year.value}:N"
            ), alt.value('lightgray')
        )
        
        plot = alt.Chart(data).mark_circle(
        ).encode(x=x_line, y=y_line,  color=color
                ).properties(width=600, title=title).add_selection(click)

        return plot
