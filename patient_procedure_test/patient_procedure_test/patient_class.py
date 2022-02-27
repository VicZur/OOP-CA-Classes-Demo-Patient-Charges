# This program creates a Patient class
# The Patient class stores the data: first/middle/last name, address/city/zip code,
# phone number, emergency contact name/number

class Patient:

    # Create the __init__ method
    def __init__(self, f_name, m_name, l_name, address, city, zipc, phone, emerg_name, emerg_number):

        self.set_first_name(f_name)
        self.set_middle_name(m_name)
        self.set_last_name(l_name)
        self.set_address(address)
        self.set_city(city)
        self.set_zip_code(zipc)
        self.set_phone_num(phone)
        self.set_emergency_name(emerg_name)
        self.set_emergency_number(emerg_number)


    # Create Set (mutator) Methods

    #Function to set the first name
    def set_first_name(self, f_name):

        #Check the value is between 2 - 20 characters
        if (len(f_name) > 20) or (len(f_name) < 2):
            print('First name must be between 2 and 20 characters')
            raise ValueError
        else:
            self.__first_name = f_name



    #Function to set the middle name
    def set_middle_name(self, m_name):

        #Check the value is not more than 20 characters
        if (len(m_name) > 20):
            print('Middle name must be less than 20 characters')
            raise ValueError
        else:
            self.__middle_name = m_name


    #Function to set the last name
    def set_last_name(self, l_name):
        #Check the value is between 2 - 30 characters
        if (len(l_name) > 30) or (len(l_name) < 2):
            print('Last name must be between 2 and 30 characters')
            raise ValueError
        else:
            self.__last_name = l_name



    #Function to set the address
    def set_address(self, address):
        #Check the value is between 5 - 50 characters
        if (len(address) > 50) or (len(address) < 5):
            print('Address must be between 5 and 50 characters')
            raise ValueError
        else:
            self.__address = address



    #Function to set the city
    def set_city(self, city):
        #Check the value is between 2 - 20 characters
        if (len(city) > 20) or (len(city) < 2):
            print('City must be between 2 and 20 characters')
            raise ValueError
        else:
            self.__city = city



    #Function to set the zip code
    def set_zip_code(self, zipc):
        #Check if the value entered is digits (assume American program asking for zip code)
        if (zipc.isdigit() == False) or len(zipc) != 5:
            print('Zip code must contain 5 digits')
            raise ValueError
        else:
            self.__zip_code = zipc



    #Function to set the phone number
    def set_phone_num(self, phone):
        #Check if the value entered is digits
        if (phone.isdigit() == False) or len(phone) < 10:
            print('Phone number must contain at least 10 digits')
            raise ValueError
        else:
            self.__phone_num = phone




    #Function to set the emergency name
    def set_emergency_name(self, emerg_name):
        #Check the value is between 3 - 50 characters
        if (len(emerg_name) > 50) or (len(emerg_name) < 3):
            print('Emergency name must be between 3 and 30 characters')
            raise ValueError
        else:
            self.__emergency_name = emerg_name



    #Function to set the emergncy number
    def set_emergency_number(self, emerg_number):
        #Check if the value entered is digits
        if (emerg_number.isdigit() == False) or len(emerg_number) < 10:
            print('Emergency number must contain at least 10 digits')
            raise ValueError
        else:
            self.__emergency_number = emerg_number


    # Create Get (accessor) Methods
    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_zip_code(self):
        return self.__zip_code

    def get_phone_num(self):
        return self.__phone_num

    def get_emergency_name(self):
        return self.__emergency_name

    def get_emergency_number(self):
        return self.__emergency_number


     # Create a __str__ method to display the patient info
    def __str__(self):
        result = '-----Patient Info-----' + \
        '\n Name: ' + self.__first_name + ' ' +  self.__middle_name + ' ' + self.__last_name + \
        '\n Address: ' + self.__address + ', ' + self.__city + ', ' +self.__zip_code + \
        '\n Phone: ' + self.__phone_num + \
        '\n Emergency Contact: ' + self.__emergency_name + ' ' + self.__emergency_number

        return result

