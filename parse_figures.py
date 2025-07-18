#!/usr/bin/env python3
"""
Parse block shapes from figures.csv and create visual representations.
Each figure has an ID and a set of coordinates that define its shape.
"""

import csv
import re
from collections import defaultdict


def parse_figures_csv(filename):
    """
    Parse the figures.csv file and extract figure shapes.
    Returns a dictionary mapping figure IDs to their coordinate arrays.
    """
    figures = {}
    current_figure = None
    current_coords = []
    
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            # Skip empty rows
            if not any(row):
                continue
                
            # Check if this is a new figure definition
            # Row starts with a number (row index) followed by the figure ID
            if len(row) > 2 and row[0].strip().isdigit() and row[1].strip():
                # Save previous figure if exists
                if current_figure and current_coords:
                    figures[current_figure] = current_coords
                
                # Start new figure
                current_figure = row[1].strip()
                current_coords = []
                
                # Extract coordinates from this row
                for i in range(8, len(row)):
                    coord = row[i].strip()
                    if coord and re.match(r'^\d+,\d+$', coord):
                        x, y = map(int, coord.split(','))
                        current_coords.append((x, y))
            
            # Continue collecting coordinates for current figure
            elif current_figure and len(row) > 8:
                for i in range(8, len(row)):
                    coord = row[i].strip()
                    if coord and re.match(r'^\d+,\d+$', coord):
                        x, y = map(int, coord.split(','))
                        current_coords.append((x, y))
    
    # Save last figure
    if current_figure and current_coords:
        figures[current_figure] = current_coords
    
    return figures


def visualize_figure(coords):
    """
    Create a visual representation of a figure from its coordinates.
    Returns a string showing the shape using '#' characters.
    """
    if not coords:
        return "Empty figure"
    
    # Find bounds
    min_x = min(x for x, y in coords)
    max_x = max(x for x, y in coords)
    min_y = min(y for x, y in coords)
    max_y = max(y for x, y in coords)
    
    # Create grid
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Fill in the coordinates
    for x, y in coords:
        grid[y - min_y][x - min_x] = '#'
    
    # Convert to string
    return '\n'.join(''.join(row) for row in grid)


def main():
    # Parse the CSV file
    figures = parse_figures_csv('csv/figures.csv')
    
    # Print summary
    print(f"Total figures parsed: {len(figures)}")
    print("\nFigure Dictionary:")
    print("{")
    
    # Sort figures by their numeric part if possible, otherwise alphabetically
    def sort_key(item):
        key = item[0]
        # Try to extract number from the key
        match = re.search(r'(\d+)', key)
        if match:
            return (0, int(match.group(1)), key)
        return (1, 0, key)
    
    sorted_figures = sorted(figures.items(), key=sort_key)
    
    for figure_id, coords in sorted_figures:
        print(f"    '{figure_id}': {coords},")
    print("}")
    
    # Show some example visualizations
    print("\n\nSample Figure Visualizations:")
    print("=" * 50)
    
    # Show first 10 figures as examples
    for i, (figure_id, coords) in enumerate(sorted_figures[:10]):
        print(f"\nFigure {figure_id} ({len(coords)} blocks):")
        print(visualize_figure(coords))
        print("-" * 20)
    
    # Group figures by number of blocks
    blocks_count = defaultdict(list)
    for figure_id, coords in figures.items():
        blocks_count[len(coords)].append(figure_id)
    
    print("\n\nFigures grouped by number of blocks:")
    for count in sorted(blocks_count.keys()):
        print(f"{count} blocks: {', '.join(sorted(blocks_count[count]))}")


if __name__ == "__main__":
    main()