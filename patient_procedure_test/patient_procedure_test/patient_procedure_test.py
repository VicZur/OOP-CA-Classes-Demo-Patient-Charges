# This program uses the Classes Patient and Procedure (from patient_class and procedure_class)
# It create an instance of patient & 3 procedure instances
# It then displays the patient & procedures info and the total charges of all 3 procedures

import patient_class
import procedure_class

def main():

    #set variable to loop the program
    again = 'y'

    while again == 'y':

        #create variable to determine if the user wants default or custom data
        #set to default 'n' to align with original assignment
        c_procedure = 'n'

        #Create an empty list to store procedures in
        #To be used for increased functionality - to allow a variable number of procedures 
        #to be input by a user - important for calculating the total charges later & displaying info
        procedures_list = []


        #Create an instance of the Patient class
        patient = create_patient()

        #Initialize lists to represent the 3 sample procedures as given in the assignment breif
        #each list stores data to be used to initialize an instance of the Procedure Class
        sample_proc_1 = ['Physical Exam', '15/09/2021', 'Dr Jones', 300]
        sample_proc_2 = ['X-Ray', '15/09/2021', 'Dr Ryan', 600]
        sample_proc_3 = ['Blood Test', '15/09/2021', 'Dr Smith', 100]

        #Create a list to hold all of the sample_proc lists (to be used in order to loop through all sample_proc 's when initializing the objects
        sample_proc_meta = [sample_proc_1, sample_proc_2, sample_proc_3]


        #create a dictionary to link the variable name to the name to be displayed to the user
        #use the key as the info to be displayed to the user, and the value as a variable to store the information
        procedure_info_dict = {'Procedure Name' : '', 'Procedure Date' : '', 'Doctor' : '', 'Procedure Charge' : ''}


        #Ask user if they want to use the default procedures or add their own
        c_procedure = customize('Would you like to input your own procedure info? y/n')



        if c_procedure == 'y': #User would like to input their own data

            procedures_list = create_procedures(procedure_info_dict, procedures_list)       

        else: #user wants to use the default program (assignment requirements)
       
           #Iterate through the list pointing to all the sample_proc lists, initialize an instance of the Procedure class for each sample_proc
            for sample_proc in sample_proc_meta:

                #Create an instance of the Procedure class
                procedure = procedure_class.Procedure(sample_proc[0], sample_proc[1], sample_proc[2], sample_proc[3])
            
                #add the new instance procedure to the list storing all of the initialized Procedure objects 
                #to be used later for display purposes 
                procedures_list.append(procedure)
        

        display_spacing()

        #print the patient info
        print(patient)

        print()

        #call the function to print the procedures info
        display_proc_info(procedures_list)

        display_spacing()

        #ask the user if they would like to start again
        again = y_n_check(input('Would you like to start again? y/n : '))

    print()
    print('Thanks for checking the Patient and Procedure info!')

#--------------------------------------------------------------------------------------------------------------------------
#FUNCTIONS  


#This method determines if the user would like to use the default patient data or enter their own custom patient data
#it takes a string message as an argument (to determine what is being customized)
#it returns a y or n value to indicate customization
def customize(message):
    custom = 'n'

    print(message)
    answer = input()
    
    custom = y_n_check(answer)

    return custom


#--------------------------------------------------------------------------------------------------------------------------


#This method checks to ensure valid imput of y or n is entered when required
def y_n_check(answer):

    #set variable to determine if valid
    is_valid = False

    while is_valid == False:
        if answer.lower() != 'n' and answer.lower() != 'y':
            print('That is not a valid answer')
            print('Please enter y / n: ')
            answer = input()

        else:
            is_valid = True

    return answer.lower()



#--------------------------------------------------------------------------------------------------------------------------

#This function creates an instance of the Patient class
#It returns an instance of the Patient class
def create_patient():
    
    #set variable to help with error checking - to determine if an instance of the Patient class has been created
    patient_exists = False

    
    #create variable to determine if the user wants default or custom data
    #set to default 'n' to align with original assignment
    c_patient = 'n'

    while patient_exists == False:

        #create a dictionary to link the variable name to the name to be displayed to the user
        #set the values to default patient value info
        patient_info_dict = {'First Name' : 'John', 'Middle Name' : 'J', 'Last Name' : 'Doe', 'Address' : '123 Street', 'City' : 'Capital', 
                                'Zip Code' : '90210', 'Phone Number' : '5550123456', 'Emergency Contact Name' : 'Mrs Doe', 'Emergency Contact Phone Number' : '5551234567'}


        #Ask user if they would like to run the default program or input their own info
        c_patient = customize('Would you like to input your own patient info? y/n')

        #If the user wants to customize the patient info , update the dictionary
        if c_patient == 'y':

            #Call the function to prompt the user to enter their own data to update the values in the dictionary
            patient_info_dict = get_user_data(patient_info_dict)


        #Create an instance of the patient class
        #Use the patient_info_dict as the argument - which will either contain the default values
        #or the updated values if the user chose to customize
        try:
            patient = patient_class.Patient(patient_info_dict['First Name'], patient_info_dict['Middle Name'], patient_info_dict['Last Name'], patient_info_dict['Address'], patient_info_dict['City'], patient_info_dict['Zip Code'], patient_info_dict['Phone Number'], patient_info_dict['Emergency Contact Name'], patient_info_dict['Emergency Contact Phone Number'])
            patient_exists = True
        except:
            print('Error - please check the values and try again')
            display_spacing()
            patient_exists = False

        else: # c_patient == 'n'
            patient = patient_class.Patient(patient_info_dict['First Name'], patient_info_dict['Middle Name'], patient_info_dict['Last Name'], patient_info_dict['Address'], patient_info_dict['City'], patient_info_dict['Zip Code'], patient_info_dict['Phone Number'], patient_info_dict['Emergency Contact Name'], patient_info_dict['Emergency Contact Phone Number'])
            patient_exists = True


    return patient

#--------------------------------------------------------------------------------------------------------------------------

#This function prompts the use to enter values to update a dictionary
#it accepts a dictionary as an argument - which contains the name of the prompt as the key (ie. "First Name") and stores the 
#in putted user data in the variable value
#it the returns the updated dictionary
def get_user_data(dict):
    #iterate through each key in the dictionary
    for key in dict:

        #Set the value of the particular key to the input
        value = input(key + ': ')

        if key != 'Middle Name':
            check_not_null(value)

        if key == 'Procedure Charge':
            value = check_float(value)

        dict[key] = value


    return dict


#--------------------------------------------------------------------------------------------------------------------------

#This function checks that the values input are not null it returns a value that is not null

def check_not_null(user_input):

    is_correct = False

    while is_correct == False:
        if user_input == '':
            print('This field cannot be empty')
            user_input = input()
            is_correct = False
        else:
            is_correct = True

    return user_input

#--------------------------------------------------------------------------------------------------------------------------

#This function checks if the value is accepts as an argument in a float, and prompts the user to enter a float if not
#it returns a float value
def check_float(number):

    is_float = False

    while is_float == False:
        try:
           float(number)
           if float(number) > 0:
               is_float = True
           else:
               print('Please enter a number greater than 0')
               number = input()
               is_float = False
        except ValueError:
            print('Please enter a numeric value')
            number = input()
            is_float = False

    return number

#--------------------------------------------------------------------------------------------------------------------------

#This function creates instances of the Procedure class
#It accepts a dictionary as an argument which holds the values to be used
#It returns a list which contains the new instances of the Procedure class created
def create_procedures(procedure_info_dict, procedures_list):
        
    success = False

    #Create a variable to track if the user would like to enter an additional procedure
    another = 'y'

    #while the user wants to continuing entering date , get the data from the user
    while another == 'y':
        #Call the function to prompt the user to enter their own data to update the values in the dictionary
        procedure_info_dict = get_user_data(procedure_info_dict)

        try:
            #Create an instance of the Procedure class, using the updated dictionary values as arguments
            procedure = procedure_class.Procedure(procedure_info_dict['Procedure Name'], procedure_info_dict['Procedure Date'], procedure_info_dict['Doctor'], float(procedure_info_dict['Procedure Charge']))
            
            #Add the new procedure to the list of procedures (to allow for easy display later)
            procedures_list.append(procedure)
            
        except:
            print('Error - please check the values and try again')


        #Ask the user if they would like to enter another procedure
        #Do this via the function to validate if the user input is y or n
        display_spacing()
        another = customize('Would you like to enter another procedure? y/n ')

    return procedures_list



#--------------------------------------------------------------------------------------------------------------------------

#This function displays data to the user and calculates the total_charges
#it accepts a list as a funtion

def display_proc_info(procedures_list):
   
   #create a varaible to store the total charges
    total_charges = 0

    print('-----Procedures-----')

    #loop through all of the procedures added to the procedures_list (all procedures)
    for procedure in procedures_list:

        #add the procedure charges to the total
        total_charges = total_charges + procedure.get_procedure_charges()

        #display the details of the procedure
        print(procedure)
        print()

    #Display the total charges of all procedures
    print('The total charges for the', len(procedures_list), 'procedures are: ', total_charges)    


#--------------------------------------------------------------------------------------------------------------------------

#This function prints rows of blank lines
def display_spacing():
    for i in range(3):
        print()

main()