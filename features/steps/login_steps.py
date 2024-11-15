from behave import given, when, then

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


@given(u'I enter my username as \'Ayeesha\'')
def step_impl(context):
    login_page.enter_username('Ayeesha')

@given(u'I enter my password as \'blacklover12345\'')
def step_impl(context):
    login_page.enter_password('blacklover12345')

@given(u'I enter wrong username as \'Afi\'')
def step_impl(context):
    login_page.enter_username('Afi')

@given(u'I enter a wrong password as \'123opps\'')
def step_impl(context):
    login_page.enter_password('123opps')

@when(u'I click the login button')
def step_impl(context):
    login_page.click_login()

@then(u'I should login successfully with a \'success!\' message on my screen')
def step_impl(context):
    assert login_page.message == "Success!", f"Expected 'Success!' message but got {login_page.message}"

@then(u'I should fail to login and see a \'Failed to login!\' message on my screen')
def step_impl(context):
    assert login_page.message == "Failed to login!", f"Expected 'Failed to login!' message but got {login_page.message}"
