import calendar
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages

# Function to draw calendar with larger cells
def draw_larger_calendar_landscape(year: int, month: int, cell_width=1.5, cell_height=1.8):
    cal = calendar.Calendar()
    month_days = list(cal.itermonthdays2(year, month))
    month_name = calendar.month_name[month]

    fig, ax = plt.subplots(figsize=(cell_width * 7 + 1, cell_height * 6 + 2))
    ax.set_xlim(0, 7 * cell_width)
    ax.set_ylim(0, 7 * cell_height)
    ax.axis('off')

    fig.patch.set_facecolor('#fdf6ec')
    ax.set_facecolor('#fffaf0')

    for row in range(6):
        for col in range(7):
            rect = patches.Rectangle(
                (col * cell_width, row * cell_height),
                cell_width, cell_height,
                linewidth=1,
                edgecolor='gray',
                facecolor='#eed5d5'
            )
            ax.add_patch(rect)

    header_colors = ['#f4a261' if day in ['Sat', 'Sun'] else '#2a9d8f'
                     for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
    for i, (day, color) in enumerate(zip(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], header_colors)):
        ax.text(i * cell_width + cell_width / 2, 6 * cell_height + cell_height * 0.2,
                day, ha='center', va='center', fontsize=14, fontweight='bold', color=color)

    row = 5
    col = 0
    for day, weekday in month_days:
        if day == 0:
            col += 1
            if col > 6:
                col = 0
                row -= 1
            continue

        date = datetime(year, month, day)
        weekday_name = calendar.day_name[date.weekday()]
        if weekday_name in ['Saturday', 'Sunday']:
            checkbox1 = "[ ] 45m"
            checkbox2 = "[ ] 60m"
            checkbox3 = "[ ] 75m"
            workout_type = "Type [       ]"
            text_color = '#d70f8a'
        else:
            checkbox1 = "[ ] 15m"
            checkbox2 = "[ ] 20m"
            checkbox3 = "[ ] 30m"
            workout_type = "Type[       ]"
            text_color = '#0f08c2'

        x = weekday * cell_width
        y = row * cell_height

        ax.text(x + 0.05, y + cell_height - 0.05, str(day), ha='left', va='top', fontsize=10, fontweight='bold', color=text_color)
        ax.text(x + 0.05, y + cell_height - 0.25, checkbox1, ha='left', va='top', fontsize=10, color=text_color)
        ax.text(x + 0.05, y + cell_height - 0.45, checkbox2, ha='left', va='top', fontsize=10, color=text_color)
        ax.text(x + 0.05, y + cell_height - 0.65, checkbox3, ha='left', va='top', fontsize=10, color=text_color)
        ax.text(x + 0.05, y + cell_height - 0.85, workout_type, ha='left', va='top', fontsize=10, color=text_color)

        col += 1
        if col > 6:
            col = 0
            row -= 1

    ax.text(3.5 * cell_width, 6.5 * cell_height + 0.5,
            f"{month_name} {year} - Stay Consistent, Stay Strong",
            ha='center', va='center', fontsize=16, weight='bold', color='#1d3557')
    plt.tight_layout()
    return fig


def generate_calendar_pdf2(year: int, months: list, output_file: str):
    with PdfPages(output_file) as pdf:
        for month in months:
            fig = draw_larger_calendar_landscape(year, month)
            pdf.savefig(fig)
            plt.close(fig)
