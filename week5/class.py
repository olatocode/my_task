class Student:
    def __init__(self, name, course, level):
        print("creating a new student...")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created")

student1 = Student("Tobi", "AIengineer", "level 1")


class NigeriaStudent:
    def __init__(self, name, state, course):
        print(f"Step 1: Creating student objects..")
        self.name = name
        self.state_of_origin = state
        self.course = course
        self.student_id = self.generate_id()
        print(f"Step 6: {self,name} from {self.state_of_origin}")
    
    def generate_id(self):
        import random
        return f"UNISAIL{random.randint(1000, 9999)}"
    
student2 = NigeriaStudent("Tobi Awosola", "Ogun", "Accounting")
print(student2.name)
print(student2.student_id)
    


class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")
    
    def buy_airtime(self, amount):
        self.airtime += amount  # self ensures it goes to the RIGHT person
        return f"{self.name} now has ₦{self.airtime} airtime"


# Creating multiple users
abeeb = PhoneUser("Abeeb Bakare", "MTN")     
onisemo = PhoneUser("Onisemo Williams", "Airtel") 

# Each person's actions affect only their own account
print(abeeb.buy_airtime(500))     # Tunde now has ₦500 airtime
print(onisemo.buy_airtime(1000)) # Blessing now has ₦1000 airtime
print(abeeb.airtime)              # 500 (Tunde's airtime unchanged)
print(onisemo.airtime)           # 1000 (Blessing's airtime unchanged)

class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False
    

     # Method: action the student can do
    def pay_school_fees(self):                   
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    # Method: another action
    def register_courses(self):                   
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
    
      # Method: calculates CGPA
    def calculate_cgpa(self, grades):           
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
    
# Using methods
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())        
print(Abiodun.register_courses())       
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5])) 


class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()
    
    # METHODS - What the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"

# Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# Attributes (characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")


# Methods (actions)
print(adunni_account.deposit(25000))    
print(adunni_account.withdraw(10000))  
print(adunni_account.transfer(15000, "Sunday James"))  
print(adunni_account.check_balance())       


class NaijaPhone:
    def __init__(self, brand, model, network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance = 0
        self.is_on = False
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f"₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
    def make_call(self, number):
        if self.is_on and self.airtime_balance > 0:
            self.airtime_balance -= 10
            return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
        return "Cannot make call. Check phone power and airtime balance"
    
    def send_sms(self, message, number):
        if self.airtime_balance >= 4:
            self.airtime_balance -= 4
            return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
        return "Insufficient airtime to send SMS"
    

    # Using the encapsulated account
ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# These work - public interface
print(ibrahim_account.deposit(10000))      # ₦10,000 deposited successfully
print(ibrahim_account.withdraw(5000, "1234"))  # ₦5,000 withdrawn successfully
print(ibrahim_account.check_balance("1234"))   # Current balance: ₦55,000


from abc import ABC, abstractmethod

# Abstract base class - defines what a Nigerian student should do
class NigerianStudent(ABC):
    def __init__(self, name, course, level):
        self.name = name
        self.course = course
        self.level = level
        self.fees_paid = False
    
    # Concrete method - all students can do this
    def pay_school_fees(self, amount):
        self.fees_paid = True
        return f"{self.name} paid ₦{amount:,} school fees"
    
    # Abstract method - each type of student implements differently
    @abstractmethod
    def study_method(self):
        pass
    
    @abstractmethod
    def take_exam(self):
        pass

# Concrete classes - specific implementations
class MedicalStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} studies anatomy books and practices on cadavers"
    
    def take_exam(self):
        return f"{self.name} takes practical exam in the anatomy lab"

class EngineeringStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} solves mathematical problems and builds prototypes"
    
    def take_exam(self):
        return f"{self.name} takes exam with calculations and technical drawings"

class ComputerScienceStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} codes programs and debugs software"
    
    def take_exam(self):
        return f"{self.name} takes practical programming exam on computer"
    
    # Using abstraction
students = [
    MedicalStudent("Dr.Adeyinka Ogunsanya", "Medicine", 400),
    EngineeringStudent("Dr. Ajala Gift", "Mechanical Engineering", 300),
    ComputerScienceStudent("Fatima Hassan", "Computer Science", 200)
]


# Same interface, different implementations
for student in students:
    print(student.pay_school_fees(150000))  # Same for all
    print(student.study_method())           # Different for each
    print(student.take_exam())              # Different for each
    print("---")


    #Simple abstraction for phone interface

class SimplePhone:
    def __init__(self, brand):
        self.brand = brand
        self._complex_internal_system = "Very complicated stuff"
    
    # Simple interface - user doesn't need to know internal complexity
    def make_call(self, number):
        self._establish_network_connection()
        self._encode_voice_signal()
        self._transmit_to_tower()
        return f"Calling {number} from {self.brand} phone..."
    
    def send_sms(self, message, number):
        self._connect_to_sms_center()
        self._format_message()
        self._send_through_network()
        return f"SMS sent to {number}: '{message}'"
    
    # Complex internal methods - hidden from user
    def _establish_network_connection(self):
        # Complex networking code here
        pass
    
    def _encode_voice_signal(self):
        # Complex audio processing here
        pass
    
    def _transmit_to_tower(self):
        # Complex radio transmission here
        pass

    # User only needs to know the simple interface
my_phone = SimplePhone("Tecno")
print(my_phone.make_call("08012345678"))  # Simple to use
print(my_phone.send_sms("How far?", "08098765432"))  # Don't need to know internals


# Parent class - Base Nigerian Person
class NigerianPerson:
    def __init__(self, first_name, last_name, state_of_origin):
        self.first_name = first_name
        self.last_name = last_name
        self.state_of_origin = state_of_origin
        self.can_speak_english = True
    
    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}"
    
    def greet(self):
        return "Good morning!"
    
    def speak_local_language(self):
        return "I speak my local language"

# Child class 1 - Nigerian Student inherits from NigerianPerson
class NigerianStudent(NigerianPerson):
    def __init__(self, first_name, last_name, state_of_origin, course, level):
        # Inherit parent's initialization
        super().__init__(first_name, last_name, state_of_origin)
        # Add student-specific attributes
        self.course = course
        self.level = level
        self.cgpa = 0.0
    
    # Override parent method with student-specific version
    def introduce(self):
        parent_intro = super().introduce()  # Get parent's introduction
        return f"{parent_intro}. I'm a {self.level} level {self.course} student"
    
    # Add student-specific methods
    def study(self):
        return f"{self.first_name} is studying {self.course}"
    
    def take_exam(self):
        return f"{self.first_name} is writing {self.course} exam"

# Child class 2 - Nigerian Worker inherits from NigerianPerson
class NigerianWorker(NigerianPerson):
    def __init__(self, first_name, last_name, state_of_origin, job_title, company):
        super().__init__(first_name, last_name, state_of_origin)
        self.job_title = job_title
        self.company = company
        self.salary = 0
    
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro}. I work as a {self.job_title} at {self.company}"
    
    def work(self):
        return f"{self.first_name} is working as a {self.job_title}"
    
    def receive_salary(self, amount):
        self.salary += amount
        return f"{self.first_name} received ₦{amount:,} salary"

# Child class 3 - Nigerian Teacher (inherits from NigerianWorker)
class NigerianTeacher(NigerianWorker):
    def __init__(self, first_name, last_name, state_of_origin, subject, school):
        # Teacher is a type of worker
        super().__init__(first_name, last_name, state_of_origin, "Teacher", school)
        self.subject = subject
        self.students = []
    
    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}. I teach {self.subject} at {self.company}"
    
    def teach(self):
        return f"Teacher {self.first_name} is teaching {self.subject}"
    
    def grade_students(self):
        return f"Teacher {self.first_name} is grading {self.subject} assignments"