def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for start_time, end_time in permanence_period:
            if start_time <= target_time <= end_time:
                counter += 1
        return counter
    except TypeError:
        return None
