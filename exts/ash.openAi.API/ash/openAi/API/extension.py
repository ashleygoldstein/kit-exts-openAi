import omni.ext
import omni.ui as ui
import omni.kit.commands
from pxr import Sdf

# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[ash.openAi.API] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[ash.openAi.API] MyExtension startup")

        self._count = 0

        self._window = ui.Window("My Window", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("")


                def on_click():
                    omni.kit.commands.execute('DeletePrims',
                        paths=['/World/Plane/Looks'],
                        destructive=False)

                    omni.kit.commands.execute('CreateAndBindMdlMaterialFromLibrary',
                        mdl_name='OmniSurface.mdl',
                        mtl_name='OmniSurface',
                        mtl_created_list=['/World/Looks/OmniSurface'],
                        bind_selected_prims=False)

                    omni.kit.commands.execute('MovePrim',
                        path_from='/World/Looks',
                        path_to='/World/Plane/Looks',
                        destructive=False)


                def on_reset():
                    omni.kit.commands.execute('ChangeProperty',
                        prop_path=Sdf.Path('/World/Plane/Looks/OmniSurface/Shader.inputs:diffuse_reflection_color_image'),
                        value=Sdf.AssetPath('C:/Users/agoldstein/OneDrive - NVIDIA Corporation/Documents/omniverse extensions/kit-exts-openAi/generatedImg.png'),
                        prev=None)


                on_reset()

                with ui.HStack():
                    ui.Button("Add", clicked_fn=on_click)
                    ui.Button("Generate", clicked_fn=on_reset)

    def on_shutdown(self):
        print("[ash.openAi.API] MyExtension shutdown")
