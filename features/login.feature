Feature: User login
    Scenario: Successfull login
        Given I enter my username as 'Ayeesha'
        And I enter my password as 'blacklover12345'
        When I click the login button
        Then I should login successfully with a 'success!' message on my screen

    Scenario: Unsuccessfull login 
        Given I enter wrong username as 'Afi'
        And I enter a wrong password as '123opps'
        When I click the login button
        Then I should fail to login and see a 'Failed to login!' message on my screen

    