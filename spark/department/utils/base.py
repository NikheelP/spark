import maya.cmds as cmds
import maya.mel as mel


class base_class():
    def __init__(self):
        pass
    
    def is_type(self, node_name, node_type):
        '''
        this is the is type value where it will conpare the node namd with node type
        @param node_name: node name
        @type node_name: str
        @param node_type: node type
        @type node_type: str
        '''
        #check if geo is exists or not
        if not cmds.objExists(node_name): return False

        #check the node type is not none
        if cmds.objectType(node_name) != node_type :  return False

        return True


    
