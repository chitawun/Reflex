"""Stub file for reflex/components/radix/themes/components/icon_button.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el import elements
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.vars.base import Var

from ..base import (
    RadixLoadingProp,
    RadixThemesComponent,
)

LiteralButtonSize = Literal["1", "2", "3", "4"]

class IconButton(elements.Button, RadixLoadingProp, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        size: Optional[
            Union[
                Breakpoints[str, Literal["1", "2", "3", "4"]],
                Literal["1", "2", "3", "4"],
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3", "4"]],
                        Literal["1", "2", "3", "4"],
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "ghost", "outline", "soft", "solid", "surface"],
                Var[Literal["classic", "ghost", "outline", "soft", "solid", "surface"]],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[Var[bool], bool]] = None,
        radius: Optional[
            Union[
                Literal["full", "large", "medium", "none", "small"],
                Var[Literal["full", "large", "medium", "none", "small"]],
            ]
        ] = None,
        auto_focus: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        form: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_action: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_enc_type: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        form_method: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_no_validate: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        form_target: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        name: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        type: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        value: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        access_key: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        draggable: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        hidden: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        input_mode: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        item_prop: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        spell_check: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        tab_index: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        title: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        loading: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_click: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_focus: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_mount: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_scroll: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "IconButton":
        """Create a IconButton component.

        Args:
            *children: The children of the component.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            size: Button size "1" - "4"
            variant: Variant of button: "classic" | "solid" | "soft" | "surface" | "outline" | "ghost"
            color_scheme: Override theme color for button
            high_contrast: Whether to render the button with higher contrast color against background
            radius: Override theme radius for button: "none" | "small" | "medium" | "large" | "full"
            auto_focus: Automatically focuses the button when the page loads
            disabled: Disables the button
            form: Associates the button with a form (by id)
            form_action: URL to send the form data to (for type="submit" buttons)
            form_enc_type: How the form data should be encoded when submitting to the server (for type="submit" buttons)
            form_method: HTTP method to use for sending form data (for type="submit" buttons)
            form_no_validate: Bypasses form validation when submitting (for type="submit" buttons)
            form_target: Specifies where to display the response after submitting the form (for type="submit" buttons)
            name: Name of the button, used when sending form data
            type: Type of the button (submit, reset, or button)
            value: Value of the button, used when sending form data
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
            loading: If set, show an rx.spinner instead of the component children.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Raises:
            ValueError: If no children are passed.

        Returns:
            The IconButton component.
        """
        ...

    def add_style(self): ...

icon_button = IconButton.create