"""CLI
Interactions with the terminal
"""
import os
import sys
import subprocess
import shutil


def get_input(max_len: int = 1 << 13) -> str:
    pass


def get_shell() -> str:
    """Get user's default shell

    Returns:
        str: shell's name
    """

    return (
        os.popen("ps -o comm= -p $(ps -o ppid= -p $(ps -o ppid= -p $$))").read().strip()
    )


def execute_with_prompt(cmd: str, shell: str = None) -> None:
    pass
