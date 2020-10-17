

class COLOR_VARIABLE_CHILD():
    def __init__(self, value):
        if not isinstance(value, list):
            raise Exception(f'value is not a list please Define the List')

        self._color_value = value
    
    @property
    def set_color(self):
        '''
        return the color value
        '''
        return self._color_value

    def get_color(self):
        '''
        return the color value
        '''
        return self._color_value

    @set_color.setter
    def set_color(self, value):
        '''
        setting up the new value
        @param value: list value
        @type value: list

        '''
        if not isinstance(value, list):
            raise Exception(f'value is not a list please Define the List')
        
        self._color_value = value
        return self._color_value
    
class COLOR_VARIABLE():
    '''
    this is the color variable which will be include all the related to color in the widget
    can be get and set new value to change the widget color
    '''
    def __init__(self):
        self.minimize_color = COLOR_VARIABLE_CHILD(value=[0, 255, 0])
        self.maxmize_color = COLOR_VARIABLE_CHILD(value=[255, 255, 0])
        self.close_color = COLOR_VARIABLE_CHILD(value=[255, 0, 0])

        self.background_color = COLOR_VARIABLE_CHILD(value=[])
        self.button_color = COLOR_VARIABLE_CHILD(value=[1 ,1 ,1])


    def get_background_color_var(self):
        return self.background_color

    def get_button_color_var(self):
        return self.button_color

    def get_minimize_color(self):
        return self.minimize_color

    def get_maxmize_color(self):
        return self.maxmize_color

    def get_close_color(self):
        return self.close_color

        



