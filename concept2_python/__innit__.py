def VO2max(weight, time, isFemale):  # for male athletes who are trained
    _pace = (time)/60  # pace in minutes
    if isFemale:
        if weight <= 61.36:
            _Y = 14.6 - (1.5 * _pace)
            return (_Y * 1000) / weight
        else:
            _Y = 14.9 - (1.5 * _pace)
            return (_Y * 1000) / (weight)
    else:
        if weight <= 75:
            _Y = 15.1 - (1.5 * _pace)
            return (_Y * 1000) / weight 
        else:
            _Y = 15.7 - (1.5 * _pace)
            return (_Y * 1000) / (weight)


def watts(time):
    _pace = time / 4
    return 2.80/(_pace**3)


def weightAdjustedTime(weight, time):
    _wf = (weight / 122.4699399)**0.222
    return time * _wf