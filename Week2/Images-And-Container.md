### What are Images?

    -- Images are the blueprint or templates for container.
    -- They contain the code to run and required environments.

### What are Containers?

    -- They are running using of images or running software.

### Why do we have two things -- Images and Containers?

    --  We can trigger multiple containers based upon one image.
    --  Multiple instances of one image can be created and run with different env configs.

## Layer based architecture of image

    When we build or re-build an image, instructions that gets changed and the instructions that follows gets re-evaluated.
    For the unchanged instructions, docker just uses cache.

<strong><em>Using this concept we can optimize our docker file. For eg, copy the code after environment creation, so every code change doesn't trigger installation of the packages.</em></strong>