import json
import streamlit as st
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os

DATASTRAX_TOKEN_JSON = os.getenv("DATASTRAX_TOKEN_JSON")
SECURE_BUNDLE_ZIP = os.getenv("SECURE_BUNDLE_ZIP")

@st.cache_resource
def create_datastax_connection():
    cloud_config = {"secure_connect_bundle": SECURE_BUNDLE_ZIP}

    with open(DATASTRAX_TOKEN_JSON) as f:
        secrets = json.load(f)

    CLIENT_ID = secrets["clientId"]
    CLIENT_SECRET = secrets["secret"]

    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    astra_session = cluster.connect()
    return astra_session
