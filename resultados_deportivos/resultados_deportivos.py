import reflex as rx

resultados = [
    {"evento": "Fútbol - Real Madrid vs Barcelona", "marcador": "2 - 1", "deporte": "Fútbol"},
    {"evento": "Baloncesto - Lakers vs Celtics", "marcador": "98 - 102", "deporte": "Baloncesto"},
    {"evento": "Tenis - Nadal vs Djokovic", "marcador": "6-4, 3-6, 7-5", "deporte": "Tenis"},
]

# Estado para almacenar el deporte seleccionado
selected_deporte = rx.State("")

def filter_results(deporte):
    global selected_deporte
    selected_deporte = deporte

def index():
    filtered_resultados = [
        res for res in resultados if selected_deporte == "" or res["deporte"] == selected_deporte
    ]
    
    return rx.vstack(
        rx.heading("Resultados Deportivos", size="9"),
        rx.hstack(
            rx.button("Todos", on_click=lambda: filter_results("")),
            rx.button("Fútbol", on_click=lambda: filter_results("Fútbol")),
            rx.button("Baloncesto", on_click=lambda: filter_results("Baloncesto")),
            rx.button("Tenis", on_click=lambda: filter_results("Tenis")),
            spacing="1em"
        ),
        *[
            rx.card(
                rx.text(res["evento"], weight="bold"),
                rx.text(res["marcador"]),
                padding="1em",
                margin_bottom="1em",
                border_radius="8px",
                box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
                background_color="#f9f9f9"
            )
            for res in filtered_resultados
        ],
        align="center",
        padding="2em",
        background_color="#eaeaea",
    )

app = rx.App()
app.add_page(index)
app.compile()