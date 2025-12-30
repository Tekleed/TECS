import ECS
from ECS import Components

Entity = ECS.Entity()

ECS.Add(Entity, "Position")

Position_Component: Components.Position = ECS.Get(Entity, "Position")