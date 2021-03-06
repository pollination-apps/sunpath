"""Add additional elements for loading sunpath in Rhino."""
import streamlit as st
from ladybug.sunpath import Sunpath
from shared import prepare_geometry

from pollination_streamlit_io import inputs, button

def add_rhino_controls(sunpath: Sunpath, radius: int, north_angle: float):
    geometries = prepare_geometry(sunpath=sunpath,
        radius=radius, north_angle=north_angle)

    # layout
    st.markdown('---')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        inputs.send(
            data=geometries,
            unique_id='preview-sunpath',
            default_checked=True,
            key='sunpath',
            label='Preview',
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
            key='bake-sunpath'
        )
