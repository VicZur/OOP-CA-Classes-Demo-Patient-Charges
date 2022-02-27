#This program creates a Procedure class, representing a medical procedure
#The Procedure class stores the name & date of the procedure, the doctor
#performing it, and the charges

from dateutil.parser import parse

class Procedure:

    # Create the __init__ method
    def __init__(self, proc_name, proc_date, proc_doctor, proc_charges):
        self.set_procedure_name(proc_name)
        self.set_procedure_date(proc_date)
        self.set_procedure_doctor(proc_doctor)
        self.set_procedure_charges(proc_charges)


    #Error checking:
    #References
    #https://towardsdatascience.com/6-approaches-to-validate-class-attributes-in-python-b51cffb8c4ea
    #https://www.programiz.com/python-programming/property

    # Create Set (mutator) Methods

    #Function to set the procedure name
    def set_procedure_name(self, proc_name):

        #Error checking to ensure the procedure name is valid
        #must be greater than 5 characters
        if len(proc_name) < 5:
            print('Procedure Name must be greater than 5 characters')
            raise ValueError

        self.__procedure_name = proc_name


    #Function to set the procedure date
    def set_procedure_date(self, proc_date):

        #Error checkin
        #g to ensure the user enters a valid date
        #Reference
        #https://stackoverflow.com/questions/9987818/in-python-how-to-check-if-a-date-is-valid
        try:
            parse(proc_date)
        except:
            print('Procedure date is incorrect')
            raise ValueError

        self.__procedure_date = proc_date


    #Function to set the procedure doctor
    def set_procedure_doctor(self, proc_doctor):

        #Error checking to ensure the doctor name is valid
        #must be greater than 3 characters
        if len(proc_doctor) < 3:            
            print('Procedure Doctor must be greater than 3 characters')
            raise ValueError

        self.__procedure_doctor = proc_doctor


    #Function to set the procedure charges
    def set_procedure_charges(self, proc_charges):

        #Check the user inputs a number greater than 0
        try:
            float(proc_charges)
            
            if float(proc_charges) < 0:
                raise ValueError
                print('Procedure charges must be greater than 0')
        except:
            print('Procedure charges must be greater than 0')
            raise ValueError


        self.__procedure_charges = proc_charges


    # Create Get (accessor) Methods

    #Function to get the procedure name
    def get_procedure_name(self):
        return self.__procedure_name

    #Function to get the procedure date
    def get_procedure_date(self):
        return self.__procedure_date

    #Function to get the procedure doctor
    def get_procedure_doctor(self):
        return self.__procedure_doctor

    #Function to get the procedure charges
    def get_procedure_charges(self):
        return self.__procedure_charges 



    # Create a __str__ method to display the procedure info
    def __str__(self):
        result = ' Procedure Name: ' + self.__procedure_name + \
        '\n Procedure Date: ' + self.__procedure_date + \
        '\n Doctor: ' + self.__procedure_doctor + \
        '\n Charge: ' + str(self.__procedure_charges)

        return result

