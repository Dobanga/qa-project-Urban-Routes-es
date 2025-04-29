from selenium.webdriver.common.by import By

class Locators:
    from_field = (By.ID, 'from') #Localizador del campo desde
    to_field = (By.ID, 'to') #Localizador del campo hasta
    button_order_taxi = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]") #Localizador del boton pedir taxi
    button_tariff_comfort = (By.XPATH, "//div[@class='tcard'][4]") #localizador del boton tarifa comfort
    i_button_tariff_comfort = (By.XPATH, "//button[@data-for='tariff-card-4']")#localizador para verificar el estado del elemento seleccionado
    phone_field = (By.CSS_SELECTOR, ".np-button") #Localizador del campo de numero de telefono
    phone_value = (By.CSS_SELECTOR, ".np-text") #Localizador para el valor del campo del numero de telefono
    phone_insert_field = (By.ID, "phone") #Localizador de campo para ingresar numero de telefono
    button_phone_confirmation = (By.XPATH, "//button[contains(text(), 'Siguiente')]") #Localizador del boton para confirmar numero de telefono
    phone_code_field = (By.XPATH, "//*[@id='code']") #localizador de campo para ingresar codigo
    button_code_confirmation = (By.XPATH, "//button[contains(text(), 'Confirmar')]") #localizador para boton confirmar code
    button_pay_method = (By.CLASS_NAME, "pp-text") #localizador del campo metodo de pago
    value_pay_method = (By.CLASS_NAME, "pp-value-text") #localizador para almacenar el valor del metodo de pago
    button_add_method_payment = (By.CLASS_NAME, "pp-plus-container") #localizador del campo para agregar un nuevo metodo de pago
    card_number_field = (By.XPATH, "//*[@id='number']") #localizador del campo del numero de la tarjera para el metodo de pago
    code_number_field = (By.XPATH, "//input[@placeholder='12']") #localizador del campo codigo de la tarjeta para el metodo de pago
    button_confirm_card_info = (By.XPATH, "//button[contains(text(), 'Agregar')]") #localizador para boton de confirmar informacion de la tarjeta para el metodo de pago
    button_close_pay_method_selection = (By.XPATH, "//div[@class='payment-picker open']//button[@class='close-button section-close']") #localizador del boton close de la ventana de seleccion de metodos de pago
    message_for_driver_field = (By.ID, "comment") #localizador del campo mensaje para el conductor
    slide_button_towel_paper = (By.XPATH, "//span[@class='slider round'][1]") #localizador de slide buton para ordenar manta y pañuelos
    confirmation_slider_button_towel_paper = (By.XPATH, "//input[@class='switch-input'][1]")#Localizador para el verificar el estado del slider button
    plus_button_icecream = (By.XPATH, "//div[@class='counter-plus'][1]") #localizador para boton agregar healdo
    counter_value_icecream = (By.XPATH,"//div[@class='counter-value'][1]")  # localizador checar la cantidad de helados ordenados
    button_request_taxi = (By.CLASS_NAME, "smart-button") #localizador para boton de ordenar taxi
    show_order_window = (By.CLASS_NAME, "order-body") #localizador para verificar que aparece el order body
    driver_info = (By.XPATH, "//div[@class='order-btn-group'][1]") #localizador de la informacion del conductor
    order_number = (By.CLASS_NAME, "order-number")#Localizador para el numero de la orden
