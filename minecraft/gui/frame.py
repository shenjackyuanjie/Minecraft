# Minecraft-in-python, a sandbox game
# Copyright (C) 2020-2023  Minecraft-in-python team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from minecraft.utils.utils import *
from minecraft.gui.widget import InputWidget


class Frame():
    """小部件框架。

    绑定到窗口以实现交互功能。
    """

    def __init__(self):
        self._widget = []
        self._enable = False
        self._focused = -1

    def add_widget(self, *widgets):
        for widget in widgets:
            self._widget.append(widget)

    def clean(self):
        self._widget = []
        self._enable = False

    def enable(self):
        self._enable = True
        self._focused = -1
        self.on_mouse_motion(*get_game().mouse_position, 0, 0)
        get_game().push_handlers(self)
        for widget in self._widget:
            if isinstance(widget, InputWidget):
                self._focused = self._widget.index(widget)
                widget.on_focus()
                return

    def disable(self):
        self._enable = False
        get_game().remove_handlers(self)

    def on_key_press(self, symbol, modifiers):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_key_press", symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_key_release", symbol, modifiers)

    def on_mouse_press(self, x, y, buttons, modifiers):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_mouse_press", x, y, buttons, modifiers)

    def on_mouse_release(self, x, y, buttons, modifiers):
        for widget in self._widget:
            widget.dispatch_event("on_mouse_release", x, y, buttons, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_mouse_drag", x, y,
                                  dx, dy, buttons, modifiers)

    def on_mouse_scroll(self, x, y, index, direction):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_mouse_scroll", x, y, index, direction)

    def on_mouse_motion(self, x, y, dx, dy):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_mouse_motion", x, y, dx, dy)

    def on_text(self, text):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_text", text)

    def on_text_motion(self, motion):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_text_motion", motion)

    def on_text_motion_select(self, motion):
        if not self._enable:
            return
        for widget in self._widget:
            widget.dispatch_event("on_text_motion_select", motion)

    def draw(self):
        if not self._enable:
            return
        for widget in self._widget:
            widget.draw()

    def on_resize(self, width, height):
        for widget in self._widget:
            widget.on_resize(width, height)
