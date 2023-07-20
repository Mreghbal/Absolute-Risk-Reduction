def calculate_arr(experimental_group_events, experimental_group_total, control_group_events, control_group_total):
    experimental_group_rate = experimental_group_events / experimental_group_total
    control_group_rate = control_group_events / control_group_total

    arr = control_group_rate - experimental_group_rate
    return arr


# Example usage:
experimental_group_events = 50
experimental_group_total = 1000
control_group_events = 30
control_group_total = 1000

arr = calculate_arr(experimental_group_events, experimental_group_total, control_group_events, control_group_total)
print("Absolute Risk Reduction (ARR):", arr)
