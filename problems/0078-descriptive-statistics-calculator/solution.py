import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    array = np.array(data)
    mean = float(np.mean(array))
    median = float(np.median(array))
    unique, counts = np.unique(array, return_counts=True)
    mode = int(unique[np.argmax(counts)])
    variance = float(np.var(array))
    standard_deviation = float(np.std(array))
    
    p25 = float(np.percentile(array, 25))
    p50 = float(np.percentile(array, 50))
    p75 = float(np.percentile(array, 75))
    iqr = float(p75 - p25)
    
    return {
        'mean': round(mean, 4),
        'median': round(median, 4),
        'mode': mode,
        'variance': round(variance, 4),
        'standard_deviation': round(standard_deviation, 4),
        '25th_percentile': round(p25, 4),
        '50th_percentile': round(p50, 4),
        '75th_percentile': round(p75, 4),
        'interquartile_range': round(iqr, 4)
    }