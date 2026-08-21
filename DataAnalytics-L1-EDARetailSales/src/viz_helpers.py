"""
viz_helpers.py

Reusable plotting functions for the retail sales EDA project.
Each function saves its figure to disk and returns the file path,
so notebooks can call one line instead of repeating six lines of
matplotlib/seaborn setup for every chart.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns


def set_plot_style():
    """Applies consistent styling across every chart in the project."""
    sns.set_style("whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["axes.titlesize"] = 13
    plt.rcParams["axes.titleweight"] = "bold"


def save_current_fig(figures_dir, filename):
    """
    Saves whatever figure is currently active in matplotlib.

    Parameters
    ----------
    figures_dir : str
        Folder where figures should be saved.
    filename : str
        Name of the output PNG file, e.g. 'phase4_monthly_trend.png'.

    Returns
    -------
    str
        Full path of the saved figure.
    """
    os.makedirs(figures_dir, exist_ok=True)
    path = os.path.join(figures_dir, filename)
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    return path


def plot_line_trend(series, title, xlabel, ylabel, figures_dir, filename, color="teal"):
    """
    Plots and saves a line chart from a pandas Series (used for monthly/quarterly trends).

    Parameters
    ----------
    series : pd.Series
        Index is the time period, values are the metric (e.g. total_amount).
    title, xlabel, ylabel : str
        Chart labels.
    figures_dir : str
        Folder to save the output figure.
    filename : str
        Output PNG filename.
    color : str
        Line color.

    Returns
    -------
    str
        Full path of the saved figure.
    """
    plt.figure(figsize=(14, 6))
    plt.plot(series.index, series.values, marker="o", color=color, linewidth=1.8)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    path = save_current_fig(figures_dir, filename)
    plt.show()
    return path


def plot_bar_ranking(series, title, xlabel, ylabel, figures_dir, filename,
                      palette="mako", horizontal=True):
    """
    Plots and saves a ranked bar chart from a pandas Series
    (used for category revenue, mall revenue, age group counts, etc.).

    Parameters
    ----------
    series : pd.Series
        Index is the category label, values are the metric to rank by.
    title, xlabel, ylabel : str
        Chart labels.
    figures_dir : str
        Folder to save the output figure.
    filename : str
        Output PNG filename.
    palette : str
        Seaborn color palette name.
    horizontal : bool
        If True, plots horizontal bars (better for long category names).

    Returns
    -------
    str
        Full path of the saved figure.
    """
    plt.figure(figsize=(11, 6))
    if horizontal:
        sns.barplot(x=series.values, y=series.index, hue=series.index,
                    palette=palette, legend=False)
    else:
        sns.barplot(x=series.index, y=series.values, hue=series.index,
                     palette=palette, legend=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    path = save_current_fig(figures_dir, filename)
    plt.show()
    return path


def plot_correlation_heatmap(corr_matrix, title, figures_dir, filename):
    """
    Plots and saves a correlation heatmap.

    Parameters
    ----------
    corr_matrix : pd.DataFrame
        Output of df[numeric_cols].corr().
    title : str
        Chart title.
    figures_dir : str
        Folder to save the output figure.
    filename : str
        Output PNG filename.

    Returns
    -------
    str
        Full path of the saved figure.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1,
                linewidths=0.5, fmt=".2f")
    plt.title(title)
    path = save_current_fig(figures_dir, filename)
    plt.show()
    return path