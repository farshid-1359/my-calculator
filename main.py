import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 350
    page.window_height = 500
    
    # Calculator state
    operators = ["/", "*", "+", "-"]
    last_was_operator = False
    
    # Display field
    display = ft.TextField(
        value="",
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        text_size=24,
    border_color=ft.Colors.OUTLINE,
        height=80,
    )
    
    def on_button_press(e):
        nonlocal last_was_operator
        
        current = display.value
        button_text = e.control.text
        
        if button_text == "C":
            # Clear the display
            display.value = ""
        else:
            if current and (last_was_operator and button_text in operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                display.value = new_text
        
        last_was_operator = button_text in operators
        page.update()
    
    def on_equals(e):
        text = display.value
        if text:
            try:
                solution = str(eval(display.value))
                display.value = solution
            except:
                display.value = "Error"
        page.update()
    
    # Create button rows
    button_rows = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        [".", "0", "C", "+"],
    ]
    
    # Build the calculator layout
    calculator_buttons = []
    
    for row in button_rows:
        button_row = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=label,
                    width=70,
                    height=70,
                    on_click=on_button_press,
                ) for label in row
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        calculator_buttons.append(button_row)
    
    # Equals button
    equals_button = ft.ElevatedButton(
        text="=",
        width=300,
        height=70,
        on_click=on_equals,
    bgcolor=ft.Colors.BLUE,
    color=ft.Colors.WHITE,
    )
    
    # Main layout
    page.add(
        ft.Column(
            controls=[
                display,
                *calculator_buttons,
                equals_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
