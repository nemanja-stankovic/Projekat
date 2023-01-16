import typing
import json as json


text = """REG_OZNAKA\tBOJA\tTIP_VOZILA
NI-543-MM\tsiva\tautomobil
LE-345-KM\tplava\tkamion
BG-345-TT\tbela\tautomobil
NI-345-XD\tbela\tautomobil
UE-134-NF\tcrna\tautomobil
AL-226-DF\tbela\tkamion"""


def generate_statistics(records: typing.List[str]) -> typing.Dict[str, str]:
    """
    Najpre koristimo list comprehension za kreiranje liste tipova vozila(sa duplikatima).
    Potom koristimo dict comprehension nad skupom tipova vozila (pretvaranjem liste u skup su odbačeni duplikati).
    Za svaki tip vozila računamo udeo tako što podelimo broj pojavljivanja u listi sa ukupnim brojem tipova.
    Množimo sa 100 da bismo dobili procente, zaokružujemo na 2 decimale, pretvaramo u string.
    Na kraju dodajemo simbol '%', kao u zadatku.
    :param records: records that need to be processed
    :return: dict in which every key is one vehicle type, while the value represents a percentage of the vehicle type
    """
    vehicle_type_list = [vehicle_type.split('\t')[2] for vehicle_type in records]
    return {vehicle_type: str(round((vehicle_type_list.count(vehicle_type) / len(vehicle_type_list) * 100), 2)) + '%'
            for vehicle_type in set(vehicle_type_list)}


def generate_city_list(records: typing.List[str]) -> typing.List[str]:
    """
    Najpre koristimo split po crti unutar set comprehension da bismo izdvojili skraćenice za grad.
    Budući da je u pitanju set comprehension, duplikati su eliminisani
    Pretvaramo u listu jer nam lista treba.
    :param records: records that need to be processed
    :return: list of unique city license abbreviations
    """

    return list({record.split('-')[0] for record in records})


def generate_color_by_vehicle_type(records: typing.List[str]) -> typing.Dict[str, typing.Dict[str, int]]:
    """
    U prva dva koraka izdvajamo tipove vozila bez duplikata, kao i boje bez duplikata koristeći set comprehensions.
    U trećem koraku imamo dve ugnježdene dict comprehensions. Unutrašnja formira dict gde su ključevi boje, a vrednosti
    broj vozila te boje (parovi postoje samo ako je taj broj veći od 0)
    Spoljna dict comprehension za ključeve ima tipove vozila, dok za vrednosti ima opisani dict.
    :param records: records to be processed
    :return: dict of dicts containing count of vehicle types per color
    """
    vehicle_types_set = {record.split('\t')[2] for record in records}
    colors_set = {record.split('\t')[1] for record in records}
    return {vehicle_type: {color: text.count(color + '\t' + vehicle_type) for color in colors_set
                           if text.count(color + '\t' + vehicle_type) > 0} for vehicle_type in vehicle_types_set}


def main():
    valid_records = text.split('\n')[1:]
    result = {
        "tip_vozila": generate_statistics(valid_records),
        "gradovi": generate_city_list(valid_records),
        "boja_po_tipu": generate_color_by_vehicle_type(valid_records)
    }
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()