from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from typing import *


def get_default_layout(
    title: str, xaxis_title: str, yaxis_title: str
) -> Dict[str, Any]:
    return {
        "title": title,
        "xaxis_title": xaxis_title,
        "yaxis_title": yaxis_title,
        "font": dict(size=12),
        "legend": dict(
            # orientation="h",
            # entrywidth=0.2,
            # entrywidthmode='fraction',
            # yanchor="bottom",
            # y=1.1,
            # xanchor="right",
            # x=0.1,
            font=dict(size=10),
            itemsizing="constant",
            traceorder="normal",
            itemclick="toggle",
            itemdoubleclick="toggleothers",
        ),
        # "height": 900,
        # "width": 1000,
        # "margin": dict(l=0, r=0, t=0, b=150)
    }


def get_color_sequence() -> list:
    return [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ]


def get_line_style(color: str) -> Dict[str, Any]:
    return dict(color=color)


def get_marker_style(color: str) -> Dict[str, Any]:
    return dict(color=color, size=10)
