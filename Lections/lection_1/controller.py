import imp


import module as model
import view

def button_clicl():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a,value_b)
    result = model.sum()
    view.view_data(result)