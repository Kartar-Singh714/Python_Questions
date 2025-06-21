import statistics
def mean_mode_median(l1):
    #return statistics.mean(l1), statistics.median(l1), statistics.mode(l1) # In form of tuple
    return [statistics.mean(l1), statistics.median(l1), statistics.mode(l1)] # In form of List

#mean_mode_median([3,23,56,23,78,89])
mean, median, mode = mean_mode_median([3,23,56,23,78])
print(f"Mean = {mean}, \nMode = {mode}, \nMedian = {mode}")