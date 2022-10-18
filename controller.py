import model_mul as model
import view

# Метод кнопки
def button_click():
    value_a= view.get_value() # Метод получения данных из view get_value()
    value_b= view.get_value()
    model.init(value_a, value_b) #инициализация начальных значений
    result = model.mul() # расчет суммы из model
    view.view_data(result) #передаем результат в view