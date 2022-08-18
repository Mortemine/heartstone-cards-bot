import json

with open('cards.json', 'r') as file:
    cards = json.load(file)


def clean_card_info(file_name: str, card_type: str) -> None:
    with open(file_name, 'w+') as new_file:
        new_cards = {}
        for card in cards['cards']:
            card_id = card['id']
            card_rarity = card['rarityId']
            if card_type == 'gold' and len(card['imageGold']) != 0:
                new_cards[card_id] = {'rarityId': card_rarity, 'image': card['imageGold']}
            elif card_type == 'normal':
                new_cards[card_id] = {'rarityId': card_rarity, 'image': card['image']}
            else:
                pass
        json.dump(new_cards, new_file)


clean_card_info('clean_card_info.json', 'normal')
clean_card_info('clean_golden_cards.json', 'gold')
