import data
from selenium import webdriver
from UrbanRoutesMethods import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    #Prueba 1 Configurar la dirección
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    #Prueba 2 Seleccionar la tarifa Comfort
    def test_set_tariff_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_request_taxi_button()
        tariff_button_initial_status = routes_page.get_comfort_button_status()
        routes_page.click_tariff_button()
        tariff_button_after_status = routes_page.get_comfort_button_status()
        assert tariff_button_initial_status != tariff_button_after_status

    #Prueba 3 Rellenar el número de teléfono
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        phone_number_on_field = routes_page.get_phone()
        assert phone_number == phone_number_on_field

    #Prueba 4 Agregar una tarjeta de crédito
    def test_set_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        code_number = data.card_code
        initial_pay_method = routes_page.get_pay_method()
        routes_page.set_payment_method(card_number, code_number)
        after_pay_method = routes_page.get_pay_method()
        assert initial_pay_method != after_pay_method

    #Prueba 5 Escribir un mensaje para el controlador.
    def test_set_comment(self):
        routes_page = UrbanRoutesPage(self.driver)
        comment = data.message_for_driver
        initial_comment = routes_page.get_message()
        routes_page.set_message(comment)
        after_comment = routes_page.get_message()
        assert initial_comment != after_comment

    #Prueba 6 Pedir una manta y pañuelos.
    def test_set_service_requirements_switch(self):
        routes_page = UrbanRoutesPage(self.driver)
        initial_switch_button_status = routes_page.get_switch_button_status()
        routes_page.click_slide_button_towel_paper()
        final_switch_button_status = routes_page.get_switch_button_status()
        assert initial_switch_button_status != final_switch_button_status

    #Prueba 7 Pedir 2 helados.
    def test_set_service_requirements_plus(self):
        routes_page = UrbanRoutesPage(self.driver)
        initial_counter_value = routes_page.get_counter_value()
        routes_page.click_plus_button_icecream()
        final_counter_value = routes_page.get_counter_value()
        assert initial_counter_value != final_counter_value

    #Prueba 8 Aparece el modal para buscar un taxi.
    def test_service_request(self):
        routes_page = UrbanRoutesPage(self.driver)
        initial_order_window = routes_page.check_order_window()
        routes_page.click_button_request_taxi()
        final_order_window = routes_page.check_order_window()
        assert final_order_window != initial_order_window

    #Prueba 9 Esperar a que aparezca la información del conductor en el modal.
    def test_driver_info_display(self):
        routes_page = UrbanRoutesPage(self.driver)
        initial_driver_info = routes_page.check_driver_info()
        routes_page.wait_driver_info()
        final_driver_info = routes_page.check_driver_info()
        assert final_driver_info != initial_driver_info

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
