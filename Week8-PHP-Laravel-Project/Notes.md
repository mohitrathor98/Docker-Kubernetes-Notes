#### What if we don't provide ENTRYPOINT or CMD in our dockerfile?

    In this case ENTRYPOINT or CMD mentioned in the base image of the dockerfile is used.
    
    If we mention it then, the ENTRYPOINT or CMD gets appended(in case of base image doesn't have it) and overwritten(in case it already have one defined).