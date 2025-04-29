from selenium.webdriver import Keys
from UrbanRoutesLocatores import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from GetPhoneCode import UrbanHelper

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators

    #Metodos para seleccionar una ruta
    #Metodo para ingresar una destino en el campo Desde
    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.from_field))
        self.driver.find_element(*self.locators.from_field).send_keys(from_address)

    # Metodo para ingresar una destino en el campo Hasta
    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    # Metodo para regresar el valor del campo Desde
    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    # Metodo para regresar el valor del campo Hasta
    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    # Metodo para llevar a cabo el ingresar la ruta del viaje
    def set_route(self,address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    #Metodos para seleccionar taxi
    #Metodo para dar click al boton "pedir taxi"
    def click_request_taxi_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.button_order_taxi))
        self.driver.find_element(*self.locators.button_order_taxi).click()

    #Metodo para dar click al elemento tcard que nos permitira seleccionar la tarifa comfort
    def click_tariff_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.button_tariff_comfort))
        self.driver.find_element(*self.locators.button_tariff_comfort).click()

    #Metodo que verificar que el estado del elemento tcard seleccionado
    def get_comfort_button_status(self):
        return self.driver.find_element(*self.locators.i_button_tariff_comfort).is_displayed()

    #Metodos para agregar numero de telefono
    #Metodo para dar click en el campo numero de telefono
    def click_phone_number_field(self):
        self.driver.find_element(*self.locators.phone_field).click()

    #Metodo para agregar un numero de telefono en el campo numero de telefono de la ventana emergente
    def set_phone_field(self, phone_number):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.phone_insert_field))
        self.driver.find_element(*self.locators.phone_insert_field).send_keys(phone_number)

    #Metodo para dar click al boton siguiente despues de agregar un numero de telefono en la ventana emergente
    def click_button_phone_number_confirmation(self):
        self.driver.find_element(*self.locators.button_phone_confirmation).click()

    #Metodo para ingresar el codigo de confirmacion despues de agregar el numero de telefono
    def set_code_phone_number_confirmation(self, code):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.phone_code_field))
        self.driver.find_element(*self.locators.phone_code_field).send_keys(code)

    #Metodo para dar click en el boton de confirmar despues de agregar el codigo
    def click_button_code_phone_number_confirmation(self):
        self.driver.find_element(*self.locators.button_code_confirmation).click()

    #Metodo para regresar el numero de telefono que fue ingresado
    def get_phone(self):
        return self.driver.find_element(*self.locators.phone_value).text

    #Conjunto de metodos que llevan a cabo el ingresar un numero de telefono en el campo "numero de telefono" de la vista principal
    def set_phone_number(self, phone_number):
        phone_code_helper = UrbanHelper(self.driver)
        self.click_phone_number_field()
        self.set_phone_field(phone_number)
        self.click_button_phone_number_confirmation()
        code = phone_code_helper.retrieve_phone_code(self.driver)
        self.set_code_phone_number_confirmation(code)
        self.click_button_code_phone_number_confirmation()

    #Metodos para agregar metodo de pago
    #Metodo para dar click al campo "Metodo de pago"
    def click_button_pay_method(self):
        self.driver.find_element(*self.locators.button_pay_method).click()

    #Metodo para dar click al campo de ingresar un nuevo metodo de pago
    def click_button_add_pay_method(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.button_add_method_payment))
        self.driver.find_element(*self.locators.button_add_method_payment).click()

    #Metodo para ingresar el numero de tarjeta
    def set_card_number(self, card_number):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.card_number_field))
        self.driver.find_element(*self.locators.card_number_field).send_keys(card_number)

    #Metodo para ingresar el numero de codigo de la tarjeta
    def set_code_number(self, code_number):
        self.driver.find_element(*self.locators.code_number_field).send_keys(code_number)
        self.driver.find_element(*self.locators.code_number_field).send_keys(Keys.TAB)

    #Metodo para dar click al boton "Agregar" despues de agregar los datos de la tarjeta
    def click_code_number_confirmation_button(self):
        self.driver.find_element(*self.locators.button_confirm_card_info).click()

    #Metodo para cerrar la ventana de metodos de pago
    def click_button_close_pay_method(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.button_close_pay_method_selection))
        self.driver.find_element(*self.locators.button_close_pay_method_selection).click()

    #Metodo para regresar el texto del tipo de metodo de campo que se encuentra en el campo "metodo de pago"
    def get_pay_method(self):
        return self.driver.find_element(*self.locators.value_pay_method).text

    #Conjunto de metodos para registrar y agregar un nuevo metodo de pago
    def set_payment_method(self, card_number, code_number):
        self.click_button_pay_method()
        self.click_button_add_pay_method()
        self.set_card_number(card_number)
        self.set_code_number(code_number)
        self.click_code_number_confirmation_button()
        self.click_button_close_pay_method()

    #Metodo para agregar un mensaje para el conductor
    def set_message(self, comment):
        self.driver.find_element(*self.locators.message_for_driver_field).send_keys(comment)

    #Metodo para regresar el valor del campo "Mensaje para el conductor"
    def get_message(self):
        return self.driver.find_element(*self.locators.message_for_driver_field).get_property('value')

    #Metodos para agregar requisitos del pedido
    #Metodo para dar click al slide button de los requisitos "Manta y pañuelos"
    def click_slide_button_towel_paper(self):
        view_slide_button = self.driver.find_element(*self.locators.slide_button_towel_paper)
        self.driver.execute_script("arguments[0].scrollIntoView();", view_slide_button)
        view_slide_button.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.slide_button_towel_paper))

    #Metodo para dar click al plus button del requisito "helado" dos veces
    def click_plus_button_icecream(self):
        self.driver.find_element(*self.locators.plus_button_icecream).click()
        self.driver.find_element(*self.locators.plus_button_icecream).click()

    #Metodo para regresar la el valor de la cantidad de servicios agregados en el requisto "helado"
    def get_counter_value(self):
        return self.driver.find_element(*self.locators.counter_value_icecream).text

    #Metodo para regresar si el estado del slide button
    def get_switch_button_status(self):
        return self.driver.find_element(*self.locators.confirmation_slider_button_towel_paper).is_selected()

    #Medotos para dar click al boton reservar el taxi
    def click_button_request_taxi(self):
        self.driver.find_element(*self.locators.button_request_taxi).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.show_order_window))

    #Metodo para verificar si la ventana emergente despues de pedir el taxi se muestra
    def check_order_window(self):
        order_window = self.driver.find_element(*self.locators.show_order_window)
        return order_window.is_displayed()

    #Metodo para esperar pa informacion del conductor
    def wait_driver_info(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.locators.order_number))

    #Metodo que regresar el nombre del primer elemento que se encuentra en la informacion del conductor
    def check_driver_info(self):
        driver_info = self.driver.find_element(*self.locators.driver_info)
        return driver_info.text




