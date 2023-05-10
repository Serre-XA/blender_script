# SPDX-License-Identifier: GPL-2.0-or-later

import bpy

from bpy.types import Menu

bl_info = {
    "name": "Maya_pie_RC",
    "author": "Serre",
    "version": (0, 0, 8),
    "blender": (3, 4, 1),
    "location": "3D View",
    "description": "",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "mia.ceb2@gmail.com",
    "category": "Interface"
}


# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)

class MAYAPRC_OT_SelObj(bpy.types.Operator):
    bl_label = "MAYAPRC_OT_SelObj"
    bl_idname = "mayaprc.sel_obj"


    def execute(self, context):
        edit_mode = bpy.context.mode

#edit mode to object mode

        if edit_mode != "OBJECT" :
            bpy.ops.object.mode_set(mode = "OBJECT")
            return{"FINISHED"}

        else :
            return{"FINISHED"}


class MAYAPRC_OT_SelVert(bpy.types.Operator):
    bl_label = "MAYAPRC_OT_SelVert"
    bl_idname = "mayaprc.sel_vert"

    def execute(self, context):
        select_mode = bpy.context.tool_settings.mesh_select_mode[:1]
#(true, false, false)mitai ni natteru kara kiru
        edit_mode = bpy.context.mode
        
        if select_mode != True :
            
            if edit_mode != "EDIT_MESH" :
                bpy.ops.object.editmode_toggle()
                
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            return{"FINISHED"}
        
        else :
            return{"FINISHED"}


class MAYAPRC_OT_SelEdge(bpy.types.Operator):
    bl_label = "MAYAPRC_OT_SelEdge"
    bl_idname = "mayaprc.sel_edge"
        
    def execute(self, context):
        select_mode = bpy.context.tool_settings.mesh_select_mode[1:2]
        edit_mode = bpy.context.mode
        
        if select_mode != True :
            
            if edit_mode != "EDIT_MESH" :
                bpy.ops.object.editmode_toggle()
                
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            return{"FINISHED"}
        
        else :
            return{"FINISHED"}

class MAYAPRC_OT_SelFace(bpy.types.Operator):
    bl_label = "MAYAPRC_OT_SelFace"
    bl_idname = "mayaprc.sel_face"
        
    def execute(self, context):
        select_mode = bpy.context.tool_settings.mesh_select_mode[2:]
        edit_mode = bpy.context.mode
        if select_mode != True :
            
            if edit_mode != "EDIT_MESH" :
                bpy.ops.object.editmode_toggle()

            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            return{"FINISHED"}
        else :
            return{"FINISHED"}
        
        
class MAYAPRC_OT_SelWeight(bpy.types.Operator):
    bl_label = "MAYAPRC_OT_SelWeight"
    bl_idname = "mayaprc.sel_weight"

    def execute(self, context):
        edit_mode = bpy.context.mode

        if edit_mode != "PAINT_WEIGHT" :
            bpy.ops.object.mode_set(mode = "WEIGHT_PAINT")
            return{"FINISHED"}

        else :
            return{"FINISHED"}


class MAYAPRC_OT_SelEditArmature(bpy.types.Operator):
    bl_label = "MAYAPRC_OT_SelEditArmature"
    bl_idname = "mayaprc.sel_edit_armature"

    def execute(self, context):
        edit_mode = bpy.context.mode

        if edit_mode != "EDIT_ARMATURE" :
            bpy.ops.object.mode_set(mode = "EDIT")
            return{"FINISHED"}

        else :
            return{"FINISHED"}

class MAYAPRC_OT_SelPoseArmature(bpy.types.Operator):
    bl_label = "MAYAPRC_OT_SelPoseArmature"
    bl_idname = "mayaprc.sel_pose_armature"

    def execute(self, context):
        edit_mode = bpy.context.mode

        if edit_mode != "POSE" :
            bpy.ops.object.mode_set(mode = "POSE")
            return{"FINISHED"}

        else :
            return{"FINISHED"}


class MAYA_MT_PIE_RC(Menu):
    # label is displayed at the center of the pie menu.
    # "RC" means "Right Click"
    bl_label = "Maya_pie_RC"


    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        if bpy.context.view_layer.objects.active == None:
            object_type = False

        elif bpy.context.object.hide_viewport or bpy.context.object.hide_get():
            object_type = False

        else :
            object_type = bpy.context.object.type

        if object_type == "MESH" :
            pie.operator("mayaprc.sel_vert", text = "Vertex_mode", icon = "VERTEXSEL")
            pie.operator("mayaprc.sel_obj", text = "Object_mode", icon = "OBJECT_DATAMODE")
            pie.operator("mayaprc.sel_face", text = "Face_mode", icon = "FACESEL")
            pie.operator("mayaprc.sel_edge", text = "Edge_mode", icon = "EDGESEL")
            pie.separator()
            pie.separator()
            pie.separator()
            pie.operator("mayaprc.sel_weight", text = "Weight_paint", icon = "WPAINT_HLT")


        elif object_type == "ARMATURE" :
            
            pie.operator("mayaprc.sel_edit_armature", text = "Edit_armature", icon = "EDITMODE_HLT")
            pie.operator("mayaprc.sel_obj", text = "Object_mode", icon = "OBJECT_DATAMODE")
            pie.separator()
            pie.operator("mayaprc.sel_pose_armature", text = "Pose_armature", icon = "POSE_HLT")

        else :
            pie.separator()
            pie.operator("mayaprc.sel_obj", text = "Object_mode", icon = "OBJECT_DATAMODE")

def register():
    bpy.utils.register_class(MAYA_MT_PIE_RC)
    bpy.utils.register_class(MAYAPRC_OT_SelObj)
    bpy.utils.register_class(MAYAPRC_OT_SelVert)
    bpy.utils.register_class(MAYAPRC_OT_SelEdge)
    bpy.utils.register_class(MAYAPRC_OT_SelFace)
    bpy.utils.register_class(MAYAPRC_OT_SelWeight)
    bpy.utils.register_class(MAYAPRC_OT_SelEditArmature)
    bpy.utils.register_class(MAYAPRC_OT_SelPoseArmature)

def unregister():
    bpy.utils.unregister_class(MAYA_MT_PIE_RC)
    bpy.utils.unregister_class(MAYAPRC_OT_SelObj)
    bpy.utils.unregister_class(MAYAPRC_OT_SelVert)
    bpy.utils.unregister_class(MAYAPRC_OT_SelEdge)
    bpy.utils.unregister_class(MAYAPRC_OT_SelFace)
    bpy.utils.unregister_class(MAYAPRC_OT_SelWeight)
    bpy.utils.unregister_class(MAYAPRC_OT_SelEditArmature)
    bpy.utils.unregister_class(MAYAPRC_OT_SelPoseArmature)


if __name__ == "__main__":
    register()

