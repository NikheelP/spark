import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya


class BASE():
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

    def is_exist(self, obj_name):
        '''
        check if the object is exists or not
        @param obj_name: object Name
        @type obj_name: str
        '''
        if not cmds.objExists(obj_name):
            return False

        return True

    def get_selection_list(self, obj_name):
        '''
        return the object in selection list
        @param obj_name: object Name
        @type obj_name: str
        '''
        if not self.is_exist(obj_name):
            return False

        selection_list = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getSelectionListByName(obj_name, selection_list)

        return selection_list


    def get_MObject(self, obj_name):
        '''
        get the object name from the selction
        @param obj_name: object Name
        @type obj_name: str
        '''
        if not self.is_exist(obj_name):
            return False
            raise Exception('Object is not exits')
            
        selection_list = self.get_selection_list(obj_name)
        mObject = OpenMaya.MObject()
	    selection_list.getDependNode(0, mObject)
        
        return mObject

    def get_mDagpath(self, obj_name):
        '''
        get the dag path from the obj_name
        @param obj_name: object Name
        @type obj_name: str
        '''
        if not self.is_exist(obj_name):
            return False
            raise Exception('Object is not exits')

        selection_list = self.get_selection_list(obj_name)
        mDagPath = OpenMaya.mDagPath()
        selectionList.getDagPath(0, mDagPath)
        
        return mDagPath


    def get_poition(self, obj_name):
        '''
        returh the position of the point, Transform 
        
        '''
        pass






    
