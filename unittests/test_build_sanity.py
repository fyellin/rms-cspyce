import pytest
import inspect

import cspyce.cspyce1 as cspyce1

"""
This file contains tests of the build process
"""

def test_sane_argnames_and_signatures():
    """
    For every function in cspyce1, it has the ARGNAMES attribute iff it has the SIGNATURE
    attribute.  The ARGNAMES attribute, the SIGNATURE attribute, and the actual length
    of the function's parameters must be identical.
    """

    # This function finds as many errors as it can, rather than reporting them one by one.
    errors = []
    for name, func in vars(cspyce1).items():
        if callable(func):
            argnames = getattr(func, 'ARGNAMES', None)
            signature = getattr(func, 'SIGNATURE', None)

            if argnames is None and signature is None:
                # We're not interested
                continue

            if argnames is None or signature is None:
                if argnames is None:
                    errors.append(f"cs1.{name}.ARGNAMES is missing")
                else:
                    errors.append(f"cs1.{name}.SIGNATURE is missing")
                continue

            # Both argnames and signature are non-NULL
            parameters = inspect.signature(func).parameters

            if len(argnames) != len(parameters):
                error = f"cs1.{name}.ARGNAMES has length {len(argnames)} but " \
                        f"actually takes {len(parameters)} arguments."
                errors.append(error)

            if len(argnames) != len(signature):
                errors.append(f'cs1.{name}.ARGNAMES has length {len(argnames)}; '
                              f'cs1.{name}.SIGNATURE has length {len(signature)}.')

    if errors:
        error_message = "These functions may have bad Typemaps:\n" + "\n".join(errors)
        pytest.fail(error_message)
