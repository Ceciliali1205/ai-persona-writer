"""Prompt factory functions that fuse persona style with task."""
from personas import PERSONAS

ARTICLE_LENGTH = "300‑500 words"


def article_prompt(persona: str, topic: str) -> str:
    info = PERSONAS.get(persona)
    if info is None:
        raise ValueError(f"Unknown persona '{persona}'. Available: {list(PERSONAS)}")

    return (
        f"You are writing as a {persona.replace('_', ' ')} whose tone is {info['tone']}. "
        f"Your worldview is {info['worldview']}.\n"
        f"Compose an article of {ARTICLE_LENGTH} on the topic: '{topic}'."
        " Ensure the style and worldview remain consistent throughout."
    )


def comment_prompt(persona: str, article: str) -> str:
    info = PERSONAS.get(persona)
    if info is None:
        raise ValueError(f"Unknown persona '{persona}'. Available: {list(PERSONAS)}")

    return (
        f"Respond as the {persona.replace('_', ' ')} (tone: {info['tone']}) to the following article.\n\n"
        f"Article:\n{article}\n\n"
        "Write a concise comment (100‑150 words) that reflects the persona's worldview."
    )