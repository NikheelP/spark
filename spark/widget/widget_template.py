from spark.widget.import_module import *


class WIDGET_TEMPLATE():

    def __init__(self):
        pass

    def pushButton_def(self, MinSize=[0.0, 0.0], MaxSize=[0.0, 0.0], StyleSheet='', text='', icon='', icon_size=[0.0, 0.0], setObjectName='', toolTip=''):
        '''
        create push button layout with specify the value from above

        @param MinSize: specify MinSize Ex: [0.0, 0.0]
        @type MinSize: list
        
        @param MaxSize: specify MaxSize Ex: [0.0, 0.0]
        @type MaxSize: list

        @param StyleSheet: specify StyleSheet Ex: 'QPushButton{background-color: rgba(255, 255, 255, 0);'
        @type StyleSheet: str

        @param text: specify text Ex: 'TextButton'
        @type text: str

        @param icon: specify text Ex: 'iconPath'
        @type icon: str

        @param icon_size: specify icon_size Ex: [0.0, 0.0]
        @type icon_size: list 

        @param setObjectName: specify setObjectName Ex: 'setObjectName'
        @type setObjectName: str 
        '''
        pushButton = QPushButton()
        
        #setText
        pushButton.setText(text)
        if setObjectName == '':
            pushButton.setObjectName(text)
        else:
            pushButton.setObjectName(setObjectName)

        #get the Min size for pushButton
        if MinSize[0] != 0.0 and MinSize[1] != 0.0:
            pushButton.setMinimumSize(QSize(MinSize[0], MinSize[1]))
        
        #get the Max size for pushButton
        if MaxSize[0] != 0.0 and MaxSize[1] != 0.0:
            pushButton.setMaximumSize(QSize(MinSize[0], MinSize[1]))

        #setStyleSheet
        if StyleSheet != '':
            pushButton.setStyleSheet(StyleSheet)

        #setIcon
        if icon != '':
            icon = QIcon()
            icon.addPixmap(QPixmap(icon), QIcon.Normal, QIcon.Off)
            pushButton.setIcon(icon)

        #iconSize
        if icon_size[0] != 0.0 and icon_size[1] != 0.0:
            pushButton.setIconSize(QSize(icon_size[0], icon_size[1]))

        #toolTip
        if toolTip != '':
            pushButton.setToolTip(toolTip)


        return pushButton

    def styleSheet_string(self, obj_name, color=[]):
        '''
        specify the string value for styleSheet
        @param obj_name : specify the object name in string
        @type obj_name: str

        @param red : specify list of the Color value it should be 3 Color Ex=[1, 2, 3]
        @type red: list

        
        '''
        if len(color) != 3:
            return None
        return f'{obj_name}: rgb({color[0]}, {color[1]}, {color[2]});\n'

    def styleSheet_def(self, obj_name, color=[] , background_color = [], alternate_background_color=[], border_color=[],border_top_color=[],
                        border_right_color=[], border_bottom_color=[],
                        border_left_color=[], gridline_color=[], selection_background_color=[], selection_color=[], border_radius=0.0):

        '''
        Specify the StyhleSheet 

        @param obj_name : specify the object name in string
        @type obj_name: str

        @param color : specify the color in list
        @type color: list or str

        @param background_color : specify the baclkground color in list
        @type background_color: list or str

        @param alternate_background_color : specify the alternate background color
        @type alternate_background_color: list or str

        @param border_color : specify the border color in list
        @type border_color: list or str

        @param border_top_color : specify the border top color in list
        @type border_top_color: list or str

        @param border_right_color : specify the border right color in list
        @type border_right_color: list or str

        @param border_bottom_color : specify the border bottom color in list
        @type border_bottom_color: list or str

        @param border_left_color : specify the boirder left color in list
        @type border_left_color: list or str

        @param gridline_color : specify the gridline color in list
        @type gridline_color: list or str
        
        @param selection_background_color : specify the selection background color in list
        @type selection_background_color: list or str

        @param selection_color : specify the selection color in list
        @type selection_color: list or str
        '''


        #SPECIFY THE START OF THE COLOR
        string_val = ''.join([obj_name ,'{\n'])
        space = '    '
        #ADD COLOR IF  SPECIFIED
        if color != [] and len(color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='color', color=color)])
        elif type(color) == str:
            string_val = ''.join([string_val, space, 'color: ', color, '\n'])

        #ADD BACKGROUND COLOR IF  SPECIFIED
        if background_color != [] and len(background_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='background-color', color=background_color)])
        elif type(background_color) == str:
            string_val = ''.join([string_val, space, 'background-color: ', background_color, '\n'])
            
        #ADD ALTERNATE BACKGROUND COLOR IF  SPECIFIED
        if alternate_background_color != [] and len(alternate_background_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='alternate-background-color', color=alternate_background_color)])
        elif type(alternate_background_color) == str:
            string_val = ''.join([string_val, space, 'alternate-background-color: ', alternate_background_color, '\n'])
        
        #ADD BORDER COLOR IF  SPECIFIED
        if border_color != [] and len(border_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='border-color', color=border_color)])
        elif type(border_color) == str:
            string_val = ''.join([string_val, space, 'border-color: ', border_color, '\n'])

        #ADD BORDER TOP COLOR IF  SPECIFIED
        if border_top_color != [] and len(border_top_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='border-top-color', color=border_top_color)])
        elif type(border_top_color) == str:
            string_val = ''.join([string_val, space, 'border-top-color: ', border_top_color, '\n'])

        #ADD BORDER RIGHT COLOR IF  SPECIFIED
        if border_right_color != [] and len(border_right_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='border-right-color', color=border_right_color)])
        elif type(border_right_color) == str:
            string_val = ''.join([string_val, space, 'border-right-color: ', border_right_color, '\n'])

        #ADD BORDER BOTTOM COLOR IF  SPECIFIED
        if border_bottom_color != [] and len(border_bottom_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='border-bottom-color', color=border_bottom_color)])
        elif type(border_bottom_color) == str:
            string_val = ''.join([string_val, space, 'border-bottom-color: ', border_bottom_color, '\n'])

        #ADD BORDER LEFT COLOR IF  SPECIFIED
        if border_left_color != [] and len(border_left_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='border-left-color', color=border_left_color)])
        elif type(border_left_color) == str:
            string_val = ''.join([string_val, space, 'border-left-color: ', border_left_color, '\n'])

        #ADD GRIDLINE  COLOR IF  SPECIFIED
        if gridline_color != [] and len(gridline_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='gridline-color', color=gridline_color)])
        elif type(gridline_color) == str:
            string_val = ''.join([string_val, space, 'gridline-color: ', gridline_color, '\n'])

        #ADD SELECTION BACKGRIUND COLOR IF  SPECIFIED
        if selection_background_color != [] and len(selection_background_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='selection-background-color', color=selection_background_color)])
        elif type(selection_background_color) == str:
            string_val = ''.join([string_val, space, 'selection-background-color: ', selection_background_color, '\n'])

        #ADD SELCTION COLOR IF  SPECIFIED
        if selection_color != [] and len(selection_color) == 3:
            string_val = ''.join([string_val, space, self.styleSheet_string(obj_name='selection-color', color=selection_color)])
        elif type(selection_color) == str:
            string_val = ''.join([string_val, space, 'selection-color: ', selection_color, '\n'])

        #ADD BORDER RADIUS
        if border_radius != 0.0:
            string_val = ''.join([string_val, space, 'border-radius:', str(border_radius), 'px\n'])
        elif type(border_radius) == str:
            string_val = ''.join([string_val, space, 'border-radius: ', border_radius])
            #border-radius: 10px


        string_val = string_val + '}'

        return string_val




