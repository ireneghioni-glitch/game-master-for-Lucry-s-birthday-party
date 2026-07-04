'''
Lucry's 30 Birthday Party game
==============================

One memeber of the Buddhane friends group, Lucry, turns 30! 🎉

By executing this main.py code it generates an HTML file
tha will allow Lucry to interact with an interface, which will help
her to find our top dumb expressions to search for in a word search 
puzzle on paper.

This main.py contains the main() function which:
    - calls list_words_for_game() function that returns the 
      mapping of images paths to the correspondant solution;
    - saves game data from list_words_for_game() in a json file;
    - calls function html_temp() which returns the HTML code as a string,
      for game master interface handling and answers validation handling;
    - saves the return from html_temp() in an HTML file named 'index.html', 
      executable on browser.
'''


# imports
import json
import os

from utils.game_master_setup import list_words_for_game
from utils.html_template import html_temp

os.makedirs('data', exist_ok=True)


# main builder function (orchestrator)
def main():

    # --- Load images and setup for Game-Master -----------------------------------
    img_loading = list_words_for_game()

    # --- JSON file saving in data directory --------------------------------------
    path_json = os.path.join('data', 'game_data.json')
    with open(path_json, 'w', encoding='utf-8') as f_json:
        json.dump(img_loading, f_json, ensure_ascii=False, indent=4)
    
    print(f"✅ JSON file successfully saved in {path_json}.")
    
    # --- Game-Master interface and validation logic definition -------------------
    # Template HTML / CSS / JS
    html_template = html_temp()

    # --- HTML file generation and saving ---------------------------------------------
    with open("index.html", "w", encoding="utf-8") as f_html:
        f_html.write(html_template)

    print("🔥 'index.html' file successfully generated! Open it on browser or load it online.")  


if __name__ == "__main__":
    main()