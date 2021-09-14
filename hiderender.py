
bl_info = {
    "name": "Hide Render",
    "category": "3D View",
    "author": "Emils Geršisnskis - Ješinskis / EMILSVFX",
    "blender": (2,80,0),
    "location": "View3D",
    "description":"Hide object from viewport when render toggle is off",
    "warning": "",
    "wiki_url":"https://github.com/emilsvfx/hideRender",
    "version":(1,0,1)
}

import bpy

def main(context):
    sel_objs = bpy.context.selected_objects
    for obj in sel_objs:
        view = obj.driver_add("hide_viewport")
        drv = view.driver
        drv.type= "AVERAGE"
        newVar = drv.variables.new()
        newVar.name = "hide_render"
        newVar.type = 'SINGLE_PROP'
        newVar.targets[0].id_type = 'OBJECT'
        newVar.targets[0].id = obj
        newVar.targets[0].data_path = 'hide_render' 
        
        
class SimpleOperator(bpy.types.Operator):
    """Hide Renders"""
    bl_idname = "object.simple_operator"
    bl_label = "Hide Render"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


class LayoutDemoPanel(bpy.types.Panel):
    bl_idname = "hide_render"
    bl_label = "Hide Render"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View" 

    def draw(self, context):
        layout = self.layout

        layout.label(text="Hide Render:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_operator")


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()
