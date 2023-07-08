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

# Constants
HIDE_VIEWPORT = "hide_viewport"
HIDE_RENDER = "hide_render"

def add_viewport_hide_driver(obj):
    # Adds a driver to the 'hide_viewport' property of the object.
    # The driver controls the property based on the object's 'hide_render' property.
    try:
        view = obj.driver_add(HIDE_VIEWPORT)
    except Exception as e:
        print(f"Failed to add driver to object {obj.name}: {e}")
        return

    drv = view.driver
    drv.type = "AVERAGE"

    hide_render_var = drv.variables.new()
    hide_render_var.name = HIDE_RENDER
    hide_render_var.type = 'SINGLE_PROP'
    hide_render_var.targets[0].id_type = 'OBJECT'
    hide_render_var.targets[0].id = obj
    hide_render_var.targets[0].data_path = HIDE_RENDER 

def main(context):
    # Processes all selected objects in the current context
    # and adds a viewport hide driver to them.
    sel_objs = bpy.context.selected_objects
    for obj in sel_objs:
        add_viewport_hide_driver(obj)


class SimpleOperator(bpy.types.Operator):
    # Blender Operator that hides selected objects in the viewport when the render toggle is off.
    bl_idname = "object.simple_operator"
    bl_label = "Hide Render"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


class LayoutDemoPanel(bpy.types.Panel):
    # Blender Panel that provides a UI for the Hide Render operator in the 3D Viewport.
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
