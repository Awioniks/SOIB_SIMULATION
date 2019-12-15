#!/bin/python3

# main func making Commutation Field building

from argparse import ArgumentParser
import sys
import commutation.commutation_field as com
from algorithms.in_out_route import In_Out_Route as routing
import commutation.commutator_globals as glob


def main(file_to_read):
    """
    main func which build commutation field
    """
    consts = glob.Const_For_Commutators()
    consts.aggregate_consts(file_to_read)
    commutation_field = com.Commutation_Field(consts)
    key = "{}_{}"

    for section_nr, connection in consts.CONNECTIONS.items():
        for nr_in_section, addresses in connection["commutator"].items():
            identity = key.format(section_nr, nr_in_section)
            commutation_field.add_commutator(section_nr, nr_in_section)
            commutation_field.set_addresses_of_commutator(identity, addresses)

    routing.set_data(consts, commutation_field)
    #commutation_field.show_com()
    routing.route()


if __name__ == "__main__":
    file_to_read = sys.argv[1]
    main(file_to_read)
