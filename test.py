import random
import time

sites = {
    "netbet": {
        "mainLink": "https://live.netbet.ro/  ",
        "buttons": {
            "account": (1100, 135), 
            "closeAccount": (1240, 250),
            "balancePos": (475, 355)
            },
        "providers": {
            "pragmaticPlay": {
                "buttons": {
                    "bet": (700, 830), 
                    "cameraView": (1265, 215)
                },
                "ocrs": {
                    "firstCheck": (963, 637, 1100, 657),
                    "secondCheck": (635, 603, 700, 626),
                    "thirdCheck": (10, 500, 220, 626)
                },
                "links": {
                    "azureLink" : "https://live.netbet.ro/play/roulette-azure  ",
                    "italyLink" : "https://live.netbet.ro/play/roulette-italy-pragmatic  ",
                    "macaoLink" : "https://live.netbet.ro/play/roulette-macao  ",
                    "germanyLink" : "https://live.netbet.ro/play/roulette-germany-ro  ",
                    "rALink" : "https://live.netbet.ro/play/roulette-a  ",
                    "russianLink" : "https://live.netbet.ro/play/roulette-russia  ",
                    "turkeyLink" : "https://live.netbet.ro/play/roulette-turkey  "
                }
            }
        }
    },
    "betano": {
        "mainLink": "https://ro.betano.com/casino/live/  ",
        "buttons": {
            "account": (1140, 140), 
            "closeAccount": (1140, 140),
            "balancePos": (1117, 252)
            },
        "providers": {
            "pragmaticPlay": {
                    "buttons": {
                        "bet": (666, 876), 
                        "cameraView": (1172, 315)
                    },
                    "ocrs": {
                        "firstCheck": (898, 697, 1026, 717),
                        "secondCheck": (600, 668, 653, 691),
                        "thirdCheck": (30, 536, 189, 690)
                    },
                    "links": {
                    "azureLink": "https://ro.betano.com/casino/live/games/roulette-1-azure/3528/tables/  ",
                    "macaoLink": "https://ro.betano.com/casino/live/games/roulette-3-macao/3531/tables/  ",
                    "germanyLink": "https://ro.betano.com/casino/live/games/roulette-5-german/3529/tables/  ",
                    "turkeyLink": "https://ro.betano.com/casino/live/games/roulette-6-turkish/3533/tables/  ",
                    "romanianLink": "https://ro.betano.com/casino/live/games/roulette-12-romanian/7632/tables/  ",
                    "rouletteTwoLink": "https://ro.betano.com/casino/live/games/roulette-2/3527/tables/  ",
                    "italianLink": "https://ro.betano.com/casino/live/games/roulette-7-italian/3530/tables/  ",
                    "russianLink": "https://ro.betano.com/casino/live/games/roulette-4-russian/3532/tables/  "
                    }
            }
        } # end of general providers
    }, # end of site
    "favbet": {
        "mainLink": "https://www.favbet.ro/ro/personal-office/balance/wallets/  ",
        "buttons": {
            "balancePos": (160, 375)
            },
        "providers": {
            "pragmaticPlay": {
                "buttons": {
                    "bet": (555, 725), 
                    "cameraView": (970, 267)
                },
                "ocrs": {
                    "firstCheck": (747, 577, 849, 597),
                    "secondCheck": (503, 556, 545, 574),
                    "thirdCheck": (64, 450, 166, 575)
                },
                "links": {
                    "azureLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-1---azure/?playMode=real  ",
                    "italyLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-7---italian/?playMode=real  ",
                    "macaoLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-3---macao/?playMode=real  ",
                    "germanyLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-5---german/?playMode=real  ",
                    "rouletteTwoLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-2/?playMode=real  ",
                    "russianLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-4---russian/?playMode=real  ",
                    "turkeyLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-6---turkish/?playMode=real  ",
                    "romanianLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-12---romanian/?playMode=real  ",
                    "indianLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-8---indian/?playMode=real  ",
                    "rubyLink": "https://www.favbet.ro/ro/casino-live/show-game/pragmatic-play/roulette-10---ruby/?playMode=real"
                }
            }
        }
    }
}

last_choice = None
while True:
    # sceglie casualmente un dizionario diverso dal dizionario selezionato al giro precedente
    choice = last_choice
    while choice == last_choice:
        choice = random.choice(list(sites.keys()))
    last_choice = choice
    
    # estrae casualmente un link dal dizionario scelto
    link_dict = sites[choice]["providers"]["pragmaticPlay"]["links"]
    link_key = random.choice(list(link_dict.keys()))
    link = link_dict[link_key]
    
    print(f"Selected link: {link}")
    time.sleep(0.2)
