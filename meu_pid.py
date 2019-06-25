import random
from decimal import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

y_data = []
x_data = []
error_value_data = []
current_value_data = []
controller_output_data = []
proportional_value_data = []
integral_value_data = []
derivative_value_data = []
setpoint_value_data = []
process_value_data = []

OUTGOING_FILES_DIRECTORY = "C:\\automação tempo real\\reservatorio_conico\\trunk"

def create_offset(setpoint_value):
    offset_value = random.randint(-128, 128)
    offset_value_incrementation = float(offset_value / 100)
    return setpoint_value - offset_value_incrementation

def Pt_controller(process_error_value, Pgain_value):
    Pt = process_error_value * Pgain_value
    return Pt

def It_controller(It, process_error_value, Igain_value):
    It = It + process_error_value
    It = It * Igain_value
    return It

def Dt_controller(current_control_output_value, previous_control_output_value, derivative_gain_value):
    Dt = (current_control_output_value - previous_control_output_value) * derivative_gain_value
    # print(current_control_output_value, previous_control_output_value, Dt)
    return Dt

def process_error(setpoint_value, current_value):
    return setpoint_value - current_value

def pid_controller(proportional_value, integral_value, derivative_value):
    pid_output = derivative_value + (proportional_value + integral_value)
    return pid_output

def graph_line_data(x_value, error_value, proportional_value, integral_value, derivative_value, setpoint_value, process_value, PID_value):

    if max(x_value) > 500:
        width = max(x_value)/200
    else:
        width = 10
    height = 5
    plt.figure(figsize=(width, height), dpi=100)

    # Choose which data
    plt.plot(x_value, PID_value, '#FF4500')
    # plt.plot(x_value, error_value, 'r')
    # plt.plot(x_value, proportional_value, '#9F00A0')
    # plt.plot(x_value, integral_value, 'green')
    # plt.plot(x_value, derivative_value, '#00BBFF')
    plt.plot(x_value, setpoint_value, 'k--')
    # plt.plot(x_value, process_value, 'b')

    plt.xlabel('Iteration Count')
    plt.ylabel('Output')
    plt.title('PID Controller\n(P=0.82, I=0.155, D=0.45)')

    plt.legend(['PID Controller Output', 'Set point'], loc='upper right')
    # plt.legend(['PID Controller Output'], loc='upper right')

    # plt.legend(['PID Controller Output', 'Error Value', 'Integral Value'], loc='upper right')

    # plt.legend(['PID', 'Error Value', 'Proportional Value', 'Integral Value',
    #            'Derivative Value', 'Set point', 'Process Value'], loc='upper right')

    png_filename = "Steady_PID_Simulation"

    output_file_path = os.path.join(OUTGOING_FILES_DIRECTORY, png_filename)

    plt.savefig(output_file_path)

    print("Finished creating: " + png_filename + ".png")

def pid_simulator():
    # set point
    setpoint_value = 0

    # gain values          # P = 0.82 / I = 0.15 / D = 0.40
    proportional_gain_value = 0.82
    integral_gain_value = 0.15
    derivative_gain_value = 0.40
    #proportional_gain_value = 1
    #integral_gain_value = 0
    #derivative_gain_value = 0

    # initialisation values
    derivative_value = 1
    controller_output_value = 0
    integral_value = 0
    x_value = 0
    number_of_iterations = 200

    while x_value < number_of_iterations:
        x_value += 1

        process_value = setpoint_value

        error_value = process_value - setpoint_value

        if x_value == number_of_iterations / 5:
            setpoint_value = 100
        if x_value == number_of_iterations / 2:
            setpoint_value = 200
        if x_value == 6 * (number_of_iterations / 10):
            setpoint_value = 300
        if x_value == 7 * (number_of_iterations / 10):
            setpoint_value = 400
        if x_value == (number_of_iterations - (number_of_iterations / 5)):
            setpoint_value = 0

        # PROPORTIONAL
        proportional_value = Pt_controller(process_value, proportional_gain_value)

        # INTEGRAL
        integral_value = It_controller(integral_value, process_value, integral_gain_value)

        # CONTROLLER OUTPUT
        previous_controller_output_value = controller_output_value
        controller_output_value = proportional_value + integral_value + derivative_value

        # DERIVATIVE
        derivative_value = Dt_controller(controller_output_value, previous_controller_output_value, derivative_gain_value)
        # derivative_value = 0.25 * derivative_value

        # print(integral_value)
        # print(number_of_iterations - x_value)
        x_data.append(x_value)
        controller_output_data.append(controller_output_value)
        error_value_data.append(error_value)
        integral_value_data.append(integral_value)
        setpoint_value_data.append(setpoint_value)
        process_value_data.append(process_value)
        derivative_value_data.append(derivative_value)
        proportional_value_data.append(proportional_value)

    graph_line_data(x_data, error_value_data, proportional_value_data, integral_value_data, derivative_value_data,
                    setpoint_value_data, process_value_data, controller_output_data)

def main():
    pid_simulator()

if __name__ == "__main__":
    main()