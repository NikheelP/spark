

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
        self.background_color = COLOR_VARIABLE_CHILD(value=[])
        self.button_color = COLOR_VARIABLE_CHILD(value=[1 ,1 ,1])


    def get_background_color_var(self):
        return self.background_color

    def get_button_color_var(self):
        return self.button_color

        


print('this is working now')
color = COLOR_VARIABLE()
background_color = color.get_background_color_var()
background_color.set_color = [5, 6, 2]
print(background_color.get_color())

