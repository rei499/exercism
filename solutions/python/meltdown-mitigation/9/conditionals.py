"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature (int or float): The temperature value in kelvin.
    :param neutrons_emitted (int or float): The number of neutrons emitted per second.

    :returns (bool): Is criticality balanced?

    A reactor is said to be balanced in criticality if it satisfies the following conditions:
        - The temperature is less than 800 K.
        - The number of neutrons emitted per second is greater than 500.
        - The product of temperature and neutrons emitted per second is less than 500000.
    """
    
    temp_x_neut = temperature * neutrons_emitted
    is_balanced = True
    
    if temperature < 800 and neutrons_emitted > 500:
        return is_balanced if temp_x_neut < 500000 else False 
    return False
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.
    
    :param voltage (int or float): Voltage value.
    :param current (int or float): Current value.
    :param theoretical_max_power (int or float): The power level that corresponds to a 100% efficiency.

    :returns (str): One of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:
        1. green -> efficiency of 80% or more,
        2. orange -> efficiency of less than 80% but at least 60%,
        3. red -> efficiency below 60%, but still 30% or more,
        4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    percentage_value = (generated_power/ theoretical_max_power)*100

    if percentage_value >= 80:
        return "green"
    if percentage_value >= 60:
        return "orange"
    if percentage_value >= 30:
        return "red"
    return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature (int or float): The value of the temperature in kelvin.
    :param neutrons_produced_per_second (int or float): The neutron flux.
    :param threshold (int or float): The threshold for the category.

    :returns (str): One of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    temp_x_neut = temperature * neutrons_produced_per_second
    low_status = threshold * 0.9
    normal_lower_status = threshold - (threshold * 0.10) 
    normal_upper_status = threshold + (threshold * 0.10) 
    
    if temp_x_neut < low_status:
        return "LOW"
    if normal_lower_status <= temp_x_neut <= normal_upper_status:
        return "NORMAL"
    return "DANGER"
