import pytest
from pytest_bdd import scenarios, given, when, then

# Loading  the feature file
scenarios("../features/login.feature")

class LoginPage:
    def __init__(self):
        self.username = None
        self.password = None
        self.message = None

    def enter_username(self, username):
        self.username = username 

    def enter_password(self, password):
        self.password = password 

    def click_login(self):  
        if self.username == "Ayeesha" and self.password == "blacklover12345":
            self.message = "Success!"
        else:
            self.message = "Failed to login!" 
        return self.message


login_page = LoginPage()

# Step Definitions

@given("I enter my username as 'Ayeesha'")
def enter_correct_username():
    login_page.enter_username("Ayeesha")

@given("I enter my password as 'blacklover12345'")
def enter_correct_password():
    login_page.enter_password("blacklover12345")

@given("I enter wrong username as 'Afi'")
def enter_wrong_username():
    login_page.enter_username("Afi")

@given("I enter a wrong password as '123opps'")
def enter_wrong_password():
    login_page.enter_password("123opps")

@when("I click the login button")
def click_login():
    login_page.click_login()

@then("I should login successfully with a 'success!' message on my screen")
def check_success_message():
    assert login_page.message == "Success!", "Expected success message was not found"

@then("I should fail to login and see a 'Failed to login!' message on my screen")
def check_failure_message():
    assert login_page.message == "Failed to login!", "Expected failure message was not found"
