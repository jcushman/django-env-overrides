__version__ = "0.1.0"

import os
import environ

def apply_to(settings, prefix="DJANGO", env=None):
    prefix += "__"

    if not env:
        env = environ.Env()

    for key, value in os.environ.iteritems():
        if key.startswith(prefix):
            path_parts = key.split('__')
            if len(path_parts) < 2:
                continue
            path_parts.pop(0)

            # parse value
            if hasattr(env, path_parts[0]):
                value = getattr(env, path_parts[0])(key)
                path_parts.pop(0)
            else:
                value = env(key)

            # starting with global settings, walk down the tree to find the intended target for this value
            target = settings
            for i, path_part in enumerate(path_parts):
                # if it's an int, treat it as an array index
                if path_part.isdigit():
                    path_part = int(path_part)
                    target_type = type(target)
                    if target_type == list or target_type == tuple:
                        if len(target) <= path_part:
                            target += target_type([{}])*(path_part-len(target)+1)
                    else:
                        raise ValueError("Error parsing %s environment variable: If %s%s is an integer, %s%s must be an array." % (key, prefix, "__".join(path_parts[:i+1]), prefix, "__".join(path_parts[:i])))

                # otherwise it's a dict key -- make sure target exists
                elif path_part not in target:
                    if type(target) != dict:
                        raise ValueError(
                            "Error parsing %s environment variable: %s%s is not a dict." % (
                            key, prefix, "__".join(path_parts[:i+1])))
                    target[path_part] = {}

                last_target = target
                target = target[path_part]

            # assign value
            last_target[path_part] = value
