"""
Descriptive Statistics Python Pandas script.
In this script, we use the Python Pandas library to calculate descriptive
statistics on a student mental health dataset, the same way that it's done
in descriptive_stats.ipynb.

We write the results to a CSV file.
All output figures are saved to the output/ directory.
"""
import pandas as pd

# run descriptive statistics on the age column, including mean, median,
# mode, and percentiles
def descriptive_stats(df, column):
    """Descriptive Statistics function"""
    # get mean, median, mode
    mean_val = df[column].mean()
    median_val = df[column].median()
    mode_val = df[column].mode()[0]

    return mean_val, median_val, mode_val

def main():
    # create data
    uids = [123, 124, 156, 455, 574, 133, 765, 234, 457, 987]
    random_values = [1433, 5643, 3645, 4676, 7557, 2342, 5685, 4577, 9866, 3453]
    data = {'uid': uids, 'value': random_values}
    df = pd.DataFrame(data)

    # get descriptive_statistics results
    mean, median, mode = descriptive_stats(df, "value")

    # open md file in output/ directory
    with open("./output/descriptive_stats.md", "w") as f:
        # write the results to the md file
        f.write("## Descriptive Statistics Results\n\n")
        f.write(f"Mean: {mean}\n\n")
        f.write(f"Median: {median}\n\n")
        f.write(f"Mode: {mode}\n\n")

if __name__ == "__main__":
    main()