import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.window_width = 350
    page.window_height = 500
    
    # Simple state
    current_value = ""
    
    # Display
    display = ft.Text(
        value="0",
        size=30,
        text_align=ft.TextAlign.RIGHT,
        width=300,
        height=60
    )
    
    def button_click(e):
        nonlocal current_value
        button_text = e.control.text
        
        if button_text == "C":
            current_value = ""
            display.value = "0"
        elif button_text == "=":
            if current_value:
                try:
                    # Simple calculation for basic operations only
                    if "+" in current_value:
                        parts = current_value.split("+")
                        result = float(parts[0]) + float(parts[1])
                    elif "-" in current_value:
                        parts = current_value.split("-")
                        result = float(parts[0]) - float(parts[1])
                    elif "*" in current_value:
                        parts = current_value.split("*")
                        result = float(parts[0]) * float(parts[1])
                    elif "/" in current_value:
                        parts = current_value.split("/")
                        result = float(parts[0]) / float(parts[1])
                    else:
                        result = float(current_value)
                    
                    display.value = str(int(result) if result.is_integer() else result)
                    current_value = str(result)
                except:
                    display.value = "Error"
                    current_value = ""
        else:
            current_value += button_text
            display.value = current_value
        
        page.update()
    
    # Buttons
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "C", "+"],
        ["="]
    ]
    
    button_rows = []
    for row in buttons[:-1]:  # All rows except the last
        button_row = ft.Row([
            ft.ElevatedButton(
                text=btn,
                width=70,
                height=70,
                on_click=button_click
            ) for btn in row
        ], alignment=ft.MainAxisAlignment.CENTER)
        button_rows.append(button_row)
    
    # Equals button (full width)
    equals_btn = ft.ElevatedButton(
        text="=",
        width=300,
        height=70,
        on_click=button_click,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE
    )
    
    # Layout
    page.add(
        ft.Column([
            display,
            *button_rows,
            equals_btn
        ], 
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10)
    )

if __name__ == "__main__":
    ft.app(target=main)
