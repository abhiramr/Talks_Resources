import streamlit.components.v1 as components
from typing import Tuple

# Create a function _component_func which will call the frontend component when run
_component_func = components.declare_component(
    "custom_slider",
    url="http://localhost:3001",  # Fetch frontend component from local webserver
)

# Define a public function for the package,
# which will wrap the caller to the frontend code
def st_custom_slider(label: str, min_value: int, max_value: int, value: int = 0, key=None):
    component_value = _component_func(label=label, minValue=min_value, maxValue=max_value, initialValue=[value], key=key, default=[value])
    return component_value[0]


def st_range_slider(label: str, min_value: int, max_value: int, value: Tuple[int, int], key=None) -> Tuple[int, int]:
    component_value = _component_func(label=label, minValue=min_value, maxValue=max_value, initialValue=value, key=key, default=value)
    return tuple(component_value)