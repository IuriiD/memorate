import streamlit as st
from annotated_text import annotated_text

input = "prompt engineering is a emerging discipline within the world of generative Ai and it describes <highlight>the art of writing good intentional prompts that produce an output from a generative AI model<highlight> that we actually want and to a degree it is an R it's it's very"

def highlight_proof(reference):
    # reference is expected to contain only 1 substring, surrounded with separator
    COLOR = '#fea'
    separator = '<highlight>'
    parts = reference.split(separator)
    hightlight_tuple = (parts[1], '', COLOR)
    return [
        f'...{parts[0]}', hightlight_tuple, f'{parts[2]}...']

annotated_text(*highlight_proof(input))