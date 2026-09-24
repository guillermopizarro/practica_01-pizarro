## Clase 2 — APIs de IA Generativa y memoria conversacional

### Conversación de 8 turnos (Paso 7)

Ver evidencia en `entregas/s02/evidencia/memoria.png`.

```bash
Direct use of automatic function calling (AFC) in Models.generate_content is not recommended. Instead, we recommend to use AFC in Chat.send_message. Similarly, direct use of AFC in Models.generate_content_stream is not recommended. Instead, we recommend to use AFC in Chat.send_message_stream.
¡Hola, Alex! Encantado de conocerte. El verde es un color precioso, fresco y lleno de vida. ¿En qué te puedo ayudar hoy?
Como soy una inteligencia artificial, no tengo acceso al contenido específico de tus clases particulares o de tu curso. 

Si me dices de qué temática trata el curso (por ejemplo, desarrollo web, ciencia de datos o inteligencia artificial), ¡quizás pueda adivinar cuál es! ¿Te acuerdas de algún detalle más?
Un ejemplo clásico es **$10^{100}$** (un número 1 seguido de 100 ceros, conocido como *gúgol*). 

En lenguajes como Python, esto se maneja automáticamente convirtiéndolo en un tipo de dato más grande, pero en lenguajes como C++ o Java, un `int` estándar se desbordaría (overflow) con números mayores a 2,147,483,647. Para esos casos se usan tipos como `long long` o `BigInteger`.
El comando `uv init` inicializa un nuevo proyecto de Python utilizando la herramienta **uv**. 

Crea la estructura básica del proyecto, incluyendo un archivo de configuración (`pyproject.toml`) y un entorno virtual listo para usar.
Un token es una unidad básica de texto (como una palabra o parte de ella) que los modelos de inteligencia artificial procesan para entender y generar lenguaje.
Significa que el servidor no guarda información sobre el estado del cliente entre una petición y otra; cada solicitud debe incluir todos los datos necesarios para ser procesada.
Un archivo `.env` sirve para almacenar de forma segura variables de entorno y datos sensibles (como contraseñas o claves de API) fuera del código fuente.
Te llamas Alex y tu color favorito es el verde.
```

### Por qué elegí ventana deslizante

Elegí la ventana deslizante por ser la estrategia más simple de implementar y la de menor latencia y costo en conversaciones cortas. Para un asistente de pocas iteraciones, mantener los últimos $N$ __(representa el número de intercambios o turnos que decides conservar en la variable MAX_TURNS)__ turnos es suficiente para conservar el contexto inmediato sin la sobrecostosa complejidad de generar resúmenes progresivos ni la infraestructura adicional que requieren la memoria selectiva o las bases de datos externas.

### Límite de solicitudes provocado (Paso 9)

Ver evidencia en `entregas/s02/evidencia/rate_limit.png`.

```bash
[429] Límite de RPM alcanzado. Reintentando en 1s...
[429] Límite de RPM alcanzado. Reintentando en 2s...
[429] Límite de RPM alcanzado. Reintentando en 4s...
Request 12: Error del cliente (429): You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 15, model: gemini-3.5-flash-lite
Please retry in 29.361380086s.. No se reintenta.
```