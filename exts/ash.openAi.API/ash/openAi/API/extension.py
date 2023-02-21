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

        self._window = ui.Window("GenAI API Sample", width=600, height=300)
        with self._window.frame:
            with ui.VStack():
                with ui.HStack():
                    ui.Label("Open this Extension in VS Code.")
                with ui.HStack():
                    ui.Label("Step 1: Insert your custom API key in api.py.")
                with ui.HStack():
                    ui.Label("Step 2: Change the AssetPath in def on_reset in extension.py.")
                with ui.HStack():
                    ui.Label("Step 3: Customize your prompt in generate.py.")
                with ui.HStack():
                    ui.Label("Step 4: Follow the buttons 1-4 below.")
                with ui.HStack():
                    ui.Label("This is a sample of how to use a Generative AI API and not intended for final production use.",
                            word_wrap=True)

                with ui.CanvasFrame():
                    with ui.HStack():
                        def on_click():
                            omni.kit.commands.execute('DeletePrims',
                                paths=['/World/Looks', '/World/Plane'],
                                destructive=False)
                        
                            omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
                                prim_type='Plane',
                                prim_path=None,
                                select_new_prim=True,
                                prepend_default_prim=True)

                        def on_create():
                            omni.kit.commands.execute('CreateAndBindMdlMaterialFromLibrary',
                                mdl_name='OmniSurface.mdl',
                                mtl_name='OmniSurface',
                                mtl_created_list=['/World/Looks/OmniSurface'],
                                bind_selected_prims=['/World/Plane'])


                        def on_reset():
                            omni.kit.commands.execute('ChangeProperty',
                                prop_path=Sdf.Path('/World/Plane/Looks/OmniSurface/Shader.inputs:diffuse_reflection_color_image'),
                                #Change the AssetPath to wherever your image is generated to. example "C:/Users/...Pictures/generatedImg.png"
                                value=Sdf.AssetPath(''),
                                prev=None)
                        
                        def on_bind():
                            omni.kit.commands.execute('MovePrim',
                                path_from='/World/Looks',
                                path_to='/World/Plane/Looks',
                                keep_world_transform=False,
                                destructive=False)

                        ui.Button("1.Add", clicked_fn=on_click)
                        ui.Button("2.Create", clicked_fn=on_create)
                        ui.Button("3.Bind", clicked_fn=on_bind)
                        ui.Button("4.Generate", clicked_fn=on_reset)

    def on_shutdown(self):
        print("[ash.openAi.API] MyExtension shutdown")
