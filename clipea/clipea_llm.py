"""LLM
Interactions with `llm` python library
"""
import os
import llm.cli
import llm
import clipea.cli
from clipea import ENV, HOME_PATH, CLIPEA_DIR, utils


def init_llm(llm_model: str = "") -> llm.Model:
    pass


def stream_commands(response: llm.Response, command_prefix: str = "") -> None:
    pass
