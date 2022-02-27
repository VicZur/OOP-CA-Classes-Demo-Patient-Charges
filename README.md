# OOP-CA-Classes-Demo-Patient-Charges

This program was created as part of the Assessment Project for an Object Oriented Programming module (Level 8) at the Dublin Business School.

It received a pending grade of 90-95%, earned for demonstrating a high standard of coding practices and adding additional features.

### The project requirements
Programs to create a Patient class and Procedure class, with the attributes specified on the brief. Each class has appropriate mutator and accessor methods.

A program that creates an instance of the Patient class, and 3 intances of the Procedure class, displaying all of the information and total procedure charges.

### Additional Functionality Added
This program uses the information from the assignment brief as default values, however it also allows the user to customize both the patient information as well as the procedure information. The program runs as specified by the brief by entering: “n” , “n”. The program also loops for user convenience. 

I achieved the ability to customize the instances of these classes by utilizing functions to gather input and initialize the objects. The attributes used for the objects are stored in a dictionary, with the key being the information needed from the user, and the value the user input. I included error checking when gathering user input, such as not allowing null values (except middle name), and ensuring numbers are entered where necessary (such as procedure charge). Y or N values are also checked when appropriate. 

I also included error checking within the Classes themselves. Each initialization method (patient & procedure) references other functions within the class ensure data validation when initializing an object.  For example, phone numbers must be all digits and at least 10 digits long. Each argument that accepts a string value must be between a particular length (except middle name, which can be null). The procedure date must be a real date. Procedure charges must be a float value. 

I used things such as a sample_proc_meta list (containing 3 lists with sample procedure data) to optimize my code when creating instances of each object when using the default data. I also optimized the gathering of user data by using dictionaries for both patient & procedure attributes that could be passed to the same single function.
