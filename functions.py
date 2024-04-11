import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def missing_data(data, show_all=True):
    """
    Calculate the number and percentage of missing values for each column in a DataFrame.
    
    Parameters:
        data (DataFrame): The input DataFrame.
        show_all (bool): Whether to show all columns regardless of missing values. Default is True.
    
    Returns:
        DataFrame: A DataFrame containing the number and percentage of missing values for each column.
                   If show_all is True, all columns are included. If show_all is False, only columns
                   with missing values are included.
    """
    # Calculate total missing values for each column
    total = data.isnull().sum()
    # Calculate percentage of missing values for each column
    percent = (data.isnull().sum() / data.isnull().count() * 100)
    # Concatenate total and percent missing values into a DataFrame
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    
    # Get data types of each column
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['datatype'] = types
    
    # Return either all columns or only columns with missing values based on show_all parameter
    if show_all:
        return tt
    else:
        return tt[tt['Total'] > 0]



def find_constant_columns(data):
    """
    Find columns in a DataFrame containing constant values.

    Parameters:
        data (DataFrame): The input DataFrame.

    Returns:
        list: A list containing the names of columns with constant values.
    """
    constant_columns = []
    for column in data.columns:
        # Get unique values in the column
        if data[column].nunique() == 1:
            constant_columns.append(column)
    return constant_columns




def unique_values(data, max_colwidth=50):
    """
    Get unique values for each column in a DataFrame.

    Parameters:
        data (DataFrame): The input DataFrame.
        max_colwidth (int): Maximum width for displaying column values. Default is 50.

    Returns:
        DataFrame: A DataFrame containing the total count, number of unique values,
                   and unique values for each column.
    """
    # Set maximum column width for display
    pd.options.display.max_colwidth = max_colwidth
    
    # Count total values in each column
    total = data.count()
    
    # Create a DataFrame with total values
    tt = pd.DataFrame(total, columns=['Total'])
    
    # Initialize lists for unique values and their counts
    uniques = []
    values = []
    
    # Iterate over each column
    for col in data.columns:
        # Get unique values and their count for the column
        unique_values = data[col].unique()
        unique_count = data[col].nunique()
        
        # Append unique values and their count to respective lists
        values.append([unique_values])
        uniques.append(unique_count)
    
    # Add columns for unique values and their counts to the DataFrame
    tt['Uniques'] = uniques
    tt['Values'] = values
    
    # Sort DataFrame by number of unique values
    tt = tt.sort_values(by='Uniques', ascending=True)
    
    return tt


# Mini describe
def mini_describe(data: pd.DataFrame,
                  column_name: str):
    """
    Get Mini description of numeric data
    """
    desc = pd.DataFrame(data.describe().loc[:, column_name]).T
    desc["Range"] = desc["max"] - desc['min']
    desc['IQR'] = desc['75%'] - desc["25%"]
    return desc


def hist_box_qq(data: pd.DataFrame, 
                columns: list,
                second_plot='box', figsize=(12, 5)):
    """
    Plot histogram and boxplot(if second plot is 'box') or qqplot (if second plot is 'qq')

    data: The dataframe
    columns: a list of features to be plotted
    """
    num_cols = len(columns)
    
    fig, axes = plt.subplots(num_cols, 2, figsize=(figsize[0] * 2, figsize[1] * num_cols))
    if num_cols == 1:
        axes = axes.reshape(1, -1)

    for i, column in enumerate(columns):
        ax_hist = axes[i, 0]
        ax_plot = axes[i, 1]

        # Plot histogram with KDE by default
        sns.histplot(data[column], bins='auto', color='blue', kde=True, ax=ax_hist)
        ax_hist.set_title(f'Histogram of {column}')

        # Plot boxplot if second_plot is 'box', otherwise plot Q-Q plot
        if second_plot == 'box':
            sns.boxplot(data[column], ax=ax_plot, orient="h", color='green')
            ax_plot.set_title(f'Boxplot of {column}')
        elif second_plot == 'qq':
            stats.probplot(data[column], dist="norm", plot=ax_plot)
            ax_plot.set_title(f'Q-Q plot of {column}')

    plt.tight_layout()
    plt.show()



def count_plots(data: pd.DataFrame, 
                columns: list,
                palette='viridis',
                figsize=(12, 5)):
    """
    Plot countplots for one or more columns.

    data: The dataframe
    columns: a list of features to be plotted
    figsize: Tuple specifying the figure size
    """
    num_cols = len(columns)
    
    fig, axes = plt.subplots(num_cols, 1, figsize=(figsize[0], figsize[1] * num_cols))
    if num_cols == 1:
        axes = [axes]
    total_rows = len(data)

    for i, column in enumerate(columns):
        ax = axes[i]

        # Plot countplot
        sns.countplot(data=data, x=column, ax=ax, hue=column, palette=palette, legend=False)
        ax.set_title(f'Countplot of {column}')
        for p in ax.patches:
            height = p.get_height()
            ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
                    f'{height / total_rows * 100:.2f}%', ha='center')

    plt.tight_layout()
    plt.show()

