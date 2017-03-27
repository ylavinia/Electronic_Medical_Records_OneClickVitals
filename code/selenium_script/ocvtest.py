import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class OneclickvitalsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_title(self):
        self.driver.get('http://localhost:8000/')

        self.assertEqual(
            self.driver.title,
            'OneClickVitals')

    def test_login(self):
        self.driver.get('http://localhost:8000/accounts/login/')

        loginform = self.driver.find_element_by_class_name('form-signin')

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')

        username.send_keys('victor.vitals')
        password.send_keys('vitals')
        password.send_keys(Keys.RETURN)

    def test_appointment(self):
        self.driver.get('http://localhost:8000/accounts/login/')
        loginform = self.driver.find_element_by_class_name('form-signin')

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')

        username.send_keys('victor.vitals')
        password.send_keys('vitals')
        password.send_keys(Keys.RETURN)
        menu = self.driver.find_element_by_id('appointment_menu')
        add_appointment_link = self.driver.find_element_by_id('add_appointment')
        ActionChains(self.driver).move_to_element(menu).click(add_appointment_link).perform()
        appointment_form = self.driver.find_element_by_id('appointment_form')
        username = self.driver.find_element_by_name('user')
        type_of_appointment = self.driver.find_element_by_name('type_of_appointment')
        reason_for_appointment = self.driver.find_element_by_name('reason_for_appointment')
        phone_number = self.driver.find_element_by_name('phone_number')
        appointment_date = self.driver.find_element_by_name('appointment_date')
        appointment_time = self.driver.find_element_by_name('appointment_time')
        username.send_keys('lucy.grimm')
        type_of_appointment.send_keys('Follow-Up')
        phone_number.send_keys('(919)764-1234')
        reason_for_appointment.send_keys('severe illness')
        appointment_date.send_keys('2015-05-06')
        appointment_time.send_keys('15:15:29')
        self.driver.find_element_by_id("submit").click()


    def test_labtestorder(self):
        self.driver.get('http://localhost:8000/accounts/login/')
        loginform = self.driver.find_element_by_class_name('form-signin')

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')

        username.send_keys('victor.vitals')
        password.send_keys('vitals')
        password.send_keys(Keys.RETURN)

        menu = self.driver.find_element_by_id('labtest_menu')
        add_labtest_link = self.driver.find_element_by_id('add_labtest')
        ActionChains(self.driver).move_to_element(menu).click(add_labtest_link).perform()
        labtest_form = self.driver.find_element_by_id('labtest_form')

        username = self.driver.find_element_by_name('user')
        test_date = self.driver.find_element_by_name('test_date')
        urine_culture = self.driver.find_element_by_name('urine_culture')
        blood_culture = self.driver.find_element_by_name('blood_culture')
        allergy_test = self.driver.find_element_by_name('allergy_test')
        blood_glucose = self.driver.find_element_by_name('blood_glucose')
        thyroid = self.driver.find_element_by_name('thyroid')
        viral_test = self.driver.find_element_by_name('viral_test')
        pregnancy_test = self.driver.find_element_by_name('pregnancy_test')
        x_ray = self.driver.find_element_by_name('x_ray')

        print ("About to enter fields")
        username.send_keys('lucy.grimm')
        test_date.send_keys('2015-05-06')
        urine_culture.send_keys('yes')
        blood_culture.send_keys('no')
        allergy_test.send_keys('no')
        blood_glucose.send_keys('no')
        thyroid.send_keys('no')
        viral_test.send_keys('no')
        pregnancy_test.send_keys('no')
        x_ray.send_keys('none')
        self.driver.find_element_by_id("submit").click()


    def test_vitals(self):
        self.driver.get('http://localhost:8000/accounts/login/')
        loginform = self.driver.find_element_by_class_name('form-signin')

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')

        username.send_keys('victor.vitals')
        password.send_keys('vitals')
        password.send_keys(Keys.RETURN)

        menu = self.driver.find_element_by_id('diagnosis_menu')
        add_vitalsigns_link = self.driver.find_element_by_id('add_vitalsigns')
        ActionChains(self.driver).move_to_element(menu).click(add_vitalsigns_link).perform()
        vitalsigns_form = self.driver.find_element_by_id('vitalsigns_form')
        username = self.driver.find_element_by_name('user')
        heart_rate = self.driver.find_element_by_name('heart_rate')
        blood_pressure = self.driver.find_element_by_name('blood_pressure')
        temperature = self.driver.find_element_by_name('temperature')
        current_weight = self.driver.find_element_by_name('current_weight')
        current_height = self.driver.find_element_by_name('current_height')
        notes = self.driver.find_element_by_name('notes')

        username.send_keys('lucy.grimm')
        heart_rate.send_keys('80')
        blood_pressure.send_keys('110/80')
        temperature.send_keys('100')
        current_weight.send_keys('168')
        current_height.send_keys('68')
        notes.send_keys('testing')
        self.driver.find_element_by_id("submit").click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
