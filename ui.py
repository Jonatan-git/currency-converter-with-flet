import flet as ft
from converter import convert_currency

def app_ui(page: ft.Page):
    page.title = "Currency Converter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    base_input = ft.TextField(label="Mata uang asal (contoh: USD)")
    target_input = ft.TextField(label="Mata uang tujuan (contoh: IDR)")
    amount_input = ft.TextField(label="Jumlah uang", input_filter=ft.NumbersOnlyInputFilter())
    result_text = ft.Text(value="", size=18, color="green")

    def convert(e):
        base = base_input.value.upper()
        target = target_input.value.upper()
        try:
            amount = float(amount_input.value)
        except ValueError:
            result_text.value = "⚠️ Jumlah tidak valid."
            page.update()
            return

        result_text.value = convert_currency(base, target, amount)
        page.update()

    convert_btn = ft.ElevatedButton("Konversi", on_click=convert)

    page.add(
        ft.Column(
            [
                ft.Text("💱 Currency Converter", size=24, weight="bold"),
                base_input,
                target_input,
                amount_input,
                convert_btn,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )