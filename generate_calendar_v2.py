# generate_calendar_v2.py
import argparse
from calendar_utils_v2 import generate_calendar_pdf2

def main():
    parser = argparse.ArgumentParser(description="Generate a styled accountability calendar PDF.")
    parser.add_argument('--year', type=int, required=True, help='Year (e.g., 2025)')
    parser.add_argument('--months', type=int, nargs='+', required=True, help='List of months (e.g., 3 4 for March and April)')
    parser.add_argument('--output', type=str, default='accountability_calendar.pdf', help='Output PDF file name')
    args = parser.parse_args()

    generate_calendar_pdf2(args.year, args.months, args.output)

if __name__ == '__main__':
    main()
