"""
Compatibility stubs for GUI dependencies not required in CLI mode.
"""

try:
    from PySide6.QtWidgets import QCheckBox
    from osdag_core.compat import Qt
    from PySide6 import QtWidgets
except ImportError:
    class QCheckBox:
        """Stub for CLI mode where PySide6 is not available."""
        def __init__(self, *args, **kwargs): pass
        def isChecked(self): return False
        def checkState(self): return 0

    class Qt:
        """Stub for CLI mode."""
        Checked = 2
        Unchecked = 0
        PartiallyChecked = 1

    class QtWidgets:
        """Stub for CLI mode."""
        pass

    class QDialog:
        def __init__(self, *args, **kwargs): pass
        def exec(self): return None
