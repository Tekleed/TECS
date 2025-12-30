import os
import importlib

# Get the directory where this __init__.py file is located
Directory = os.path.dirname(__file__)

# List to store all system modules
Systems = []

# Iterate through all .py files in the Systems directory
for filename in os.listdir(Directory):
    if filename.endswith('.py') and filename != '__init__.py':
        # Remove .py extension to get module name
        module_name = filename[:-3]
        # Import the module
        module = importlib.import_module(f'.{module_name}', package='ECS.Systems')
        Systems.append(module)

def Update(delta: float):
    for System in Systems:
        if hasattr(System, 'Update'):
            System.Update(delta)
