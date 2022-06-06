"""Add additional elements for loading sunpath in Rhino."""
from platform import platform
import streamlit as st
from ladybug.sunpath import Sunpath
from shared import prepare_geometry

from pollination_streamlit_io import button

def add_sketchup_controls(sunpath: Sunpath, radius: int, north_angle: float):
    geometries = prepare_geometry(sunpath=sunpath,
        radius=radius, north_angle=north_angle)
    
    # layout
    st.markdown('---')
    col1, col2, col3 = st.columns(3)

    with col1:
        # add bake button to side bar
        button.send(
            action='DrawGeometry',
            data=geometries,
            unique_id='preview-sunpath',
            options={
                "units": "Meters"},
            key='preview-sunpath',
            platform='sketchup'
        )

    with col2:
        # add bake button to side bar
        button.send(
            action='BakeGeometry',
            data=geometries,
            unique_id='bake-sunpath',
            options={
                "layer": "Sunpath",
                "units": "Meters"},
            key='bake-sunpath',
            platform='sketchup'
        )
