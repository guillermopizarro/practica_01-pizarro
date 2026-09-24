import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MODEL = "gemini-3.5-flash-lite"

CONTEXT_WINDOW_LIMIT = 1_048_576  # gemini-2.5-flash
    
SYSTEM_INSTRUCTION = (
    "Eres un instructor de programación para principiantes. "
    "Respondes en español, máximo 3 frases. "
    "Sin jerga sin explicar, sin inventar funciones."
)

def print_budget(contents: list[dict]) -> None:
    tokens = client.models.count_tokens(model=MODEL, contents=contents)
    used_ratio = tokens.total_tokens / CONTEXT_WINDOW_LIMIT
    print(f"Historial: {tokens.total_tokens} tokens ({used_ratio:.4%} de la ventana)")

def ask(prompt: str, temperature: float = 1.3) -> tuple[str, str]:
    """Returns (text, finish_reason)."""
    response = client.models.generate_content(
        model=MODEL,
        contents=[{"role": "user", "parts": [{"text": prompt}]}],
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=temperature,
            max_output_tokens=200,
        ),
    )
    finish_reason = str(response.candidates[0].finish_reason)
    if "MAX_TOKENS" in finish_reason:
        print("[warning] La respuesta viene truncada por max_output_tokens.")
    return response.text, finish_reason


def main() -> None:
    # 1. Creamos un historial ficticio
    history = [
        {"role": "user", "parts": [{"text": "¿Qué opinas de var en JS?"}]},
        {
            "role": "model",
            "parts": [
                {
                    "text": "'var' es la forma antigua de declarar variables en JavaScript y tiene alcance de función. "
                    "Hoy en día es mejor usar 'let' o 'const' para evitar errores impredecibles. "
                    "Facilita mantener un código más limpio y seguro."
                }
            ],
        },
        {"role": "user", "parts": [{"text": "¿Y cuál es la diferencia con let?"}]},
    ]

    # 2. Imprimimos el presupuesto de tokens del historial
    print_budget(history)
    
    text, _ = ask("¿Qué opinas de var en JS?")
    print(text)

if __name__ == "__main__":
    main()
