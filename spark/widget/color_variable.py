import inspect

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

        






    '''
        #define default color layout
        self._background_color = []
        self._button_color = []
            
    #BACKGROUND COLOR
    def set_background_color(self, value):
        if not isinstance(value, list):
            frame = inspect.currentframe()
            function_name =  inspect.getframeinfo(frame).function
            raise Exception(f'value is not a list please Define the List to {function_name}' )
        
        self._background_color = value
        return self._background_color

    def get_background_color(self):
        \'''
        return the background color
        \'''
        return self._background_color

    #BUTTON COLOR
    def set_button_color(self, value):
        \'''
        set button color value
        @param value: value list
        @type value: list
        \'''
        if not isinstance(value, list):
            frame = inspect.currentframe()
            function_name =  inspect.getframeinfo(frame).function
            raise Exception(f'value is not a list please Define the List to {function_name}' )
        
        self._button_color = value
        return self._button_color
        

    def get_button_color(self):
        \'''
        return the button color
        \'''
        return self._button_color

    '''


print('this is working now')
color = COLOR_VARIABLE()
background_color = color.get_background_color_var()
background_color.set_color = [5, 6, 2]
print(background_color.get_color())

#color.set_background_color(['acae', 'aec', 'aec', 'asc'])
#color.set_button_color([22, 22, 33, 55])

#background_color = color.get_background_color()
#button_color = color.get_button_color()

#print(background_color)
#print(button_color)