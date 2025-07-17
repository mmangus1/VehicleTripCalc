# CPGM120-01 SP24
# Matthew Mangus
# Mar. 17, 2024
# Assignment number 5
# Takes Vehicle and Trip Information and Calculates Required Output
# In-Line comments
# Updated last: Jan. 5, 2025

import sys


class Vehicle:
    """
    A class used to represent a Vehicle.

    ...

    Attributes
    ----------
    Auto_Style : str
        Style of vehicle.
    Make : str
        Make of vehicle.
    Model : str
        Model of vehicle.
    Color : int
        Color of vehicle.
    Amount_Tank : float
        Amount of fuel the vehicles tank holds.
    Epa_Mpg : float
        Environmental protection agency miles per gallon estimation.
    Actual_Mpg : float
        Actual miles per gallon.
    Number_Wheels : int
        Number of wheels.
    Number_Doors : int
        Number of doors.
    Total_Miles : float
        Number of miles per a trip.
    Total_Length : float
        Total Length of trip in miles.


    Methods
    -------

    """
    Auto_Style = str()
    Make = str()
    Model = str()
    Color = str()
    Amount_Tank = float()
    Epa_Mpg = float()
    Actual_Mpg = float()
    Number_Wheels = int()
    Number_Doors = int()
    Total_Miles = float()
    Total_Length = float()


def gallons_used(total_miles: float, actual_mpg: float) -> float:
    """
    Function to obtain gallons used by dividing total miles by actual mpg.

    Parameters:
        total_miles (float): Total miles of trip.
        actual_mpg (float): Actual miles per gallon.

    Returns:
        float: Gallons of fuel used.
    """
    return float(total_miles / actual_mpg)


def fuel_required(total_miles: float, actual_mpg: float) -> float:
    """
    Function to obtain fuel required by dividing total miles by actual mpg
    then dividing that by total miles multiplied by 100.

    Parameters:
        total_miles (float): Total miles of trip.
        actual_mpg (float): Actual miles per gallon.

    Returns:
        float: Gallons of fuel required.
    """
    return (total_miles / actual_mpg) / (total_miles * 100)


def tanks_consumed(total_miles: float, amount_tank: float) -> float:
    """
    Function to obtain tanks of fuel consumed obtained by dividing total miles
    by the gallon amount of tank.

    Parameters:
        total_miles (float): The total miles of trip.
        amount_tank (float): Amount of gallons per tank.

    Returns:
        float: Number of tanks consumed over trip.
    """
    return total_miles / amount_tank


def total_carbon(total_miles: float, actual_mpg: float) -> float:
    """
    Function to obtain total carbon emitted by dividing total miles by actual
    miles per gallon.

    Parameters:
        total_miles (float): Total miles travelled.
        actual_mpg (float): Actual miles per gallon.

    Returns:
        float: Amount of carbon produced.
    """
    return (total_miles / actual_mpg) * 20


def main() -> None:
    """
    Main function to orchestrate program flow and help with error handling.

    """
    try:
        while True:
            print('New Vehicle? Any Input for Yes or N/No:')
            new_vehicle:str = input()
            if (new_vehicle == 'N'
                    or new_vehicle == 'n'
                    or new_vehicle == 'No'
                    or new_vehicle == 'no'):
                sys.exit()
            else:
                vehicle_1 = Vehicle()
                print('Enter Automobile Style:')
                vehicle_1.Auto_Style = str(input())
                print('Enter Automobile Make:')
                vehicle_1.Make = str(input())
                print('Enter Automobile Model:')
                vehicle_1.Model = str(input())
                print('Enter Automobile Color:')
                vehicle_1.Color = str(input())
                print('Enter Automobile Gas Tank Capacity:')
                vehicle_1.Amount_Tank = float(input())
                print('Enter EPA MPG Estimation:')
                vehicle_1.Epa_Mpg = float(input())
                print('Enter Actual MPG:')
                vehicle_1.Actual_Mpg = float(input())
                print('Enter Number of Wheels:')
                vehicle_1.Number_Wheels = int(input())
                print('Enter Number of Doors:')
                vehicle_1.Number_Doors = int(input())
                print('Enter Total Miles Traveled:')
                vehicle_1.Total_Miles = float(input())
                print('Enter Total Length of Trip:')
                vehicle_1.Total_Length = float(input())

                # Perform Calculations for Output:
                var_gallons = gallons_used(
                    vehicle_1.Total_Miles, vehicle_1.Actual_Mpg)
                var_miles = fuel_required(
                    vehicle_1.Total_Miles, vehicle_1.Actual_Mpg)
                var_tanks = tanks_consumed(
                    vehicle_1.Total_Miles, vehicle_1.Amount_Tank)
                var_carbon = total_carbon(
                    vehicle_1.Total_Miles, vehicle_1.Actual_Mpg)

                print(f'{vehicle_1.Make} {vehicle_1.Model} '
                      f'has used {var_gallons} gallons of fuel')
                print(f'{vehicle_1.Make} {vehicle_1.Model} '
                      f'has {var_miles} miles left before fuel is needed')
                print(f'{vehicle_1.Make} {vehicle_1.Model} '
                      f'has consumed {var_tanks} tanks of fuel')
                print(f'{vehicle_1.Make} {vehicle_1.Model} '
                      f'has emitted {var_carbon} of carbon')

    except SyntaxError as err:
        print(f'Syntax Error has occurred: {err}')

    except TypeError as err:
        print(f'Type Error has occurred: {err}')


if __name__ == '__main__':
    main()
