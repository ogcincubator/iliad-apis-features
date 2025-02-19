def replace_sdn_prop: if . and test("^SDN:P\\d+::.*") then { "@id": sub("^SDN:(?<p>P[\\d]+)::"; "http://vocab.nerc.ac.uk/collection/\(.p)/") } end ;
.sdn_parameter_urn |= replace_sdn_prop
| .sdn_uom_urn |= replace_sdn_prop