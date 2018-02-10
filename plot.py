def axes_lims(x_data, y_data, gap_frac=0.1):
    if type(x_data) == tuple:
        x_min = min([min(x) for x in x_data])
        x_max = max([max(x) for x in x_data])
    else:
        x_min = min(x_data)
        x_max = max(x_data)
    if type(y_data) == tuple:
        y_min = min([min(y) for y in y_data])
        y_max = max([max(y) for y in y_data])
    else:
        y_min = min(y_data)
        y_max = max(y_data)

    x_diff = x_max - x_min
    y_diff = y_max - y_min

    y_lim = (y_min - gap_frac * y_diff, y_max + gap_frac * y_diff)
    x_lim = (x_min - gap_frac * x_diff, x_max + gap_frac * x_diff)

    return x_lim, y_lim
