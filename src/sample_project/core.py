"""Small, dependency-free example domain logic."""


def greet(name: str = "world") -> str:
    """Return a friendly greeting for *name*.

    Empty or whitespace-only names use the default ``world`` value.
    """
    cleaned_name = name.strip() or "world"
    return f"Hello, {cleaned_name}!"
