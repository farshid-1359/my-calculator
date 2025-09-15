import flet as ft
import operator
import re

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
        border_color=ft.colors.OUTLINE,
        height=80,
    )
    
    def calculate_expression(expression):
        """Safe calculation without eval()"""
        try:
            # Remove spaces
            expression = expression.replace(" ", "")
            
            # Basic validation
            if not expression:
                return 0
                
            # Simple parsing for basic operations
            # This handles +, -, *, / operations
            result = 0
            current_number = ""
            operation = "+"
            
            for char in expression + "+":  # Add + at end to process last number
                if char in "+-*/":
                    if current_number:
                        num = float(current_number)
                        if operation == "+":
                            result += num
                        elif operation == "-":
                            result -= num
                        elif operation == "*":
                            result *= num
                        elif operation == "/":
                            if num != 0:
                                result /= num
                            else:
                                raise ValueError("Division by zero")
                    current_number = ""
                    operation = char
                else:
                    current_number += char
            
            # Return integer if result is whole number
            if result == int(result):
                return int(result)
            return round(result, 8)  # Limit decimal places
            
        except:
            raise ValueError("Invalid expression")
    
    def on_button_press(e):
        nonlocal last_was_operator
        
        current = display.value
        button_text = e.control.text
        
        if button_text == "C":
            display.value = ""
        else:
            if current and (last_was_operator and button_text in operators):
                return
            elif current == "" and button_text in operators:
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
                result = calculate_expression(text)
                display.value = str(result)
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
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
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
