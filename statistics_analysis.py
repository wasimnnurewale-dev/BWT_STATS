"""Basic descriptive-statistics analysis for a sample dataset."""

from collections import Counter
from math import sqrt


def percentile(sorted_values: list[float], proportion: float) -> float:
    """Return a percentile using linear interpolation."""
    if not sorted_values:
        raise ValueError("The dataset cannot be empty.")

    position = (len(sorted_values) - 1) * proportion
    lower = int(position)
    upper = min(lower + 1, len(sorted_values) - 1)
    weight = position - lower
    return sorted_values[lower] + (sorted_values[upper] - sorted_values[lower]) * weight


def analyze(data: list[float]) -> dict[str, float | list[float] | list[float]]:
    """Calculate common descriptive statistics."""
    if not data:
        raise ValueError("The dataset cannot be empty.")

    values = sorted(data)
    count = len(values)
    mean = sum(values) / count
    variance = sum((value - mean) ** 2 for value in values) / (count - 1) if count > 1 else 0.0
    frequencies = Counter(values)
    highest_frequency = max(frequencies.values())
    modes = sorted(
        value for value, frequency in frequencies.items() if frequency == highest_frequency
    )

    quartiles = [
        percentile(values, 0.25),
        percentile(values, 0.50),
        percentile(values, 0.75),
    ]

    return {
        "count": count,
        "mean": mean,
        "median": quartiles[1],
        "mode": modes,
        "minimum": values[0],
        "maximum": values[-1],
        "range": values[-1] - values[0],
        "variance": variance,
        "standard_deviation": sqrt(variance),
        "quartiles": quartiles,
        "interquartile_range": quartiles[2] - quartiles[0],
    }


def print_report(results: dict[str, float | list[float] | list[float]]) -> None:
    """Print the analysis in a readable format."""
    print("Descriptive Statistics")
    print("----------------------")
    print(f"Count:                {results['count']}")
    print(f"Mean:                 {results['mean']:.2f}")
    print(f"Median:               {results['median']:.2f}")
    print(f"Mode:                 {results['mode']}")
    print(f"Minimum:              {results['minimum']:.2f}")
    print(f"Maximum:              {results['maximum']:.2f}")
    print(f"Range:                {results['range']:.2f}")
    print(f"Variance:             {results['variance']:.2f}")
    print(f"Standard deviation:   {results['standard_deviation']:.2f}")
    print(f"Quartiles (Q1/Q2/Q3): {results['quartiles']}")
    print(f"Interquartile range:  {results['interquartile_range']:.2f}")


if __name__ == "__main__":
    data = [12, 15, 15, 18, 20, 21, 21, 21, 24, 27, 30, 33]
    print_report(analyze(data))

