# scripts/analyze_data.py
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# project script import
from wrangle import wrangle

def analyze_data(path=None):
    """
    Analyzes a dataset and returns summary statistics, a correlation matrix, and a scatter plot.

    Parameters:
        path (str): File path to the cleaned data. If not provided, uses the default path from wrangle().

    Returns:
        dict: A dictionary containing the analysis results.
              - 'summary_stats': HTML representation of summary statistics.
              - 'correlation_matrix': HTML representation of the correlation matrix.
              - 'plot_path': Path to the saved scatter plot image.
    """

    # Use the default path if not provided
    if path is None:
        path = wrangle()

    print(f"Attempting to load file from: {path}")

    # Check if the file exists
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Error: The file 'cleaned_kc_hoouse_data.csv' was not found at {path}.")

    # Load the dataset
    data = pd.read_csv(path)

    # Perform analysis (replace this with your actual analysis)
    summary_stats = data.describe(exclude="object").round(2)
    
    # Calculate correlation matrix for numeric columns only
    correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr().round(2)

    # Visualize data without triggering Matplotlib GUI
    fig, ax = plt.subplots()
    ax.scatter(data["sqft_living"], data["price"])
    ax.set_title("Scatter Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Save the plot as a static file
    scatter_plot_path = "../static/scatterplot.jpg"
    fig.savefig(scatter_plot_path)
    plt.close(fig)  # Close the figure to avoid displaying it in Flask

    # Return analysis results
    return {
        "summary_stats": summary_stats.to_html(),
        "correlation_matrix": correlation_matrix.to_html(),
        "plot_path": scatter_plot_path
    }

if __name__ == "__main__":
    # If the script is run directly, perform the analysis
    analyze_data()