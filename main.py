def is_criticality_balanced(temperature, neurons_per_s):
    if temperature < 800 and neurons_per_s > 500 and temperature * neurons_per_s < 500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current,theoretical_max_power):
    generated_power = voltage * current
    percent_value = (generated_power / theoretical_max_power)*100.0
    if percent_value >= 80.0:
        return "zielony"
    elif 80.0 > percent_value >= 60.0:
        return "pomarańczowy"
    elif 60.0 > percent_value >= 30.0:
        return "czerwony"
    elif percent_value < 30.0:
        return "czarny"
    else:
        return "Błąd pomiaru"

def fail_safe(temperature, neurons_per_s, threshhold):
    control_value = temperature * neurons_per_s
    if control_value < threshhold*0.9:
        return "LOW"
    elif threshhold*0.9 < control_value < threshhold*1.1:
        return "NORMAL"
    else:
        return "BŁĄD"
