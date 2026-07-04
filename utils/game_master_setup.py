# building builder using a dictionary for the game master interface 


# function for loading images
def load_image():

    # images paths
    CASTO_IMG_PATH = "images/for_game_master/CASTO.jpeg"
    CHARLINO_IMG_PATH = "images/for_game_master/CHARLINO.jpeg"
    DAIJOBU_IMG_PATH = "images/for_game_master/DAIJOBU.jpeg"
    FILI_IMG_PATH = "images/for_game_master/FILI.jpeg"
    I30SIFANNOSENTIRE_IMG_PATH = "images/for_game_master/I30SIFANNOSENTIRE.jpeg"
    IMMANUEL_IMG_PATH = "images/for_game_master/IMMANUEL.jpeg"
    NONHAPIUSENSO_IMG_PATH = "images/for_game_master/NONHAPIUSENSO.jpeg"
    STAREQUI_IMG_PATH = "images/for_game_master/STAREQUI.jpeg"
    PERMEEUGUALE_IMG_PATH = "images/for_game_master/PERMEEUGUALE.jpeg"
    PORCODDUE_IMG_PATH = "images/for_game_master/PORCODDUE.jpeg"
    UNEURO_IMG_PATH = "images/for_game_master/UNEURO.jpeg"
    VERSAILTE_IMG_PATH = "images/for_game_master/VERSAILTE.jpeg"

    # putting them in a list
    imgs_paths_list = [NONHAPIUSENSO_IMG_PATH, FILI_IMG_PATH, STAREQUI_IMG_PATH, 
                       UNEURO_IMG_PATH, VERSAILTE_IMG_PATH, I30SIFANNOSENTIRE_IMG_PATH, 
                       CHARLINO_IMG_PATH, IMMANUEL_IMG_PATH, CASTO_IMG_PATH, 
                       PERMEEUGUALE_IMG_PATH, PORCODDUE_IMG_PATH, DAIJOBU_IMG_PATH]

    return imgs_paths_list



def list_words_for_game():

    # list of dictionaries (one dict for word to be found)
    list_of_words = [
        {
            'id': 1,
            'image': load_image()[0],
            'solution': 'NONHAPIUSENSO'
        },
        {
            'id': 2,
            'image': load_image()[1],
            'solution': 'FILI'
        },
        {
            'id': 3,
            'image': load_image()[2],
            'solution': 'STAREQUI'
        },
        {
            'id': 4,
            'image': load_image()[3],
            'solution': 'UNEURO'
        },
        {
            'id': 5,
            'image': load_image()[4],
            'solution': 'VERSAILTE'
        },
        {
            'id': 6,
            'image': load_image()[5],
            'solution': 'I30SIFANNOSENTIRE'
        },
        {
            'id': 7,
            'image': load_image()[6],
            'solution': 'CHARLINO'
        },
        {
            'id': 8,
            'image': load_image()[7],
            'solution': 'IMMANUEL'
        },
        {
            'id': 9,
            'image': load_image()[8],
            'solution': 'CASTO'
        },
        {
            'id': 10,
            'image': load_image()[9],
            'solution': 'PERMEEUGUALE'
        },
        {
            'id': 11,
            'image': load_image()[10],
            'solution': 'PORCODDUE'
        },
        {
            'id': 12,
            'image': load_image()[11],
            'solution': 'DAIJOBU'
        }
    ]

    return list_of_words
