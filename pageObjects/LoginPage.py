from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():

    username_input_Id = "username"
    password_input_ID = "password"
    submit_button_XPATH = "//button[@id='submit']"
    successful_logging_url = "https://practicetestautomation.com/logged-in-successfully/"
    paragraph_text_XPATH = "//p[@class='has-text-align-center']"
    congratulation_text = "Congratulations student. You successfully logged in!"
    Logout_button_LINKTEXT = "Log out"
    incorrectUsername_text_XPATH = "//div[@id='error']"
    invalid_username_text = "Your username is invalid!"

    def __init__(self, driver):
        self.driver = driver
        self.myWait = WebDriverWait(self.driver, 10)

    def input_username(self, username):
        self.myWait.until(EC.visibility_of_element_located((By.ID, self.username_input_Id))).clear()
        self.myWait.until(EC.visibility_of_element_located((By.ID, self.username_input_Id))).send_keys(username)

    def input_password(self, password):
        self.myWait.until(EC.visibility_of_element_located((By.ID, self.password_input_ID))).clear()
        self.myWait.until(EC.visibility_of_element_located((By.ID, self.password_input_ID))).send_keys(password)

    def click_submit_button(self):
        self.myWait.until(EC.visibility_of_element_located((By.XPATH, self.submit_button_XPATH))).click()

    def check_url(self):
        try:
            result = self.myWait.until(EC.url_contains(self.successful_logging_url))
            return result
        except:
            return False

    def check_page_text(self):
        try:
            expected_text = self.myWait.until(EC.text_to_be_present_in_element((By.XPATH, self.paragraph_text_XPATH), self.congratulation_text))
            return expected_text
        except:
            return False

    def check_logout_button(self):
        try:
            displayed_button = self.driver.find_element(By.LINK_TEXT, self.Logout_button_LINKTEXT).is_displayed()
            return displayed_button
        except:
            print("The Logout button isn't displayed")
            return False

    def check_incorrectUsername_text(self):
        try:
            error_text = self.myWait.until(EC.visibility_of_element_located((By.XPATH, self.incorrectUsername_text_XPATH)))
            return error_text
        except:
            return False

    def check_username_errorMessage(self):
        error_message_text = self.myWait.until(EC.visibility_of_element_located((By.XPATH, self.incorrectUsername_text_XPATH))).text
        if error_message_text == self.invalid_username_text:
            return True
        else:
            return False

