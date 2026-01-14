import ipywidgets as widgets
from IPython.display import display

n = 8


board = [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [" "]*8,
    [" "]*8,
    [" "]*8,
    [" "]*8,
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"]
]

buttons = [[None for _ in range(n)] for _ in range(n)]
selected = None 


default_color = "#f0d9b5"
alt_color = "#b58863"
selected_color = "#00ff00"

def create_button(i, j):
    btn = widgets.Button(
        description=board[i][j],
        layout=widgets.Layout(width='50px', height='50px'),
        style={'button_color': default_color if (i+j)%2==0 else alt_color}
    )

    def on_click(b):
        global selected
      
        if selected:
            si, sj = selected
            if (i,j) != (si,sj):
               
                board[i][j] = board[si][sj]
                board[si][sj] = " "
            
            buttons[si][sj].style.button_color = default_color if (si+sj)%2==0 else alt_color
            selected = None
            update_buttons()
        
        elif board[i][j] != " ":
            selected = (i,j)
            b.style.button_color = selected_color

    btn.on_click(on_click)
    return btn

def update_buttons():
    for i in range(n):
        for j in range(n):
            buttons[i][j].description = board[i][j]
            if (i+j)%2==0:
                buttons[i][j].style.button_color = default_color
            else:
                buttons[i][j].style.button_color = alt_color
    
    if selected:
        si, sj = selected
        buttons[si][sj].style.button_color = selected_color

grid = widgets.GridBox(
    children=[],
    layout=widgets.Layout(
        grid_template_columns=f"repeat({n}, 50px)",
        grid_template_rows=f"repeat({n}, 50px)",
        grid_gap="2px 2px"
    )
)

for i in range(n):
    for j in range(n):
        buttons[i][j] = create_button(i, j)
        grid.children += (buttons[i][j],)

display(grid)
