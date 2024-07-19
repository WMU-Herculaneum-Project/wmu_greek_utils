from wmu_greek_utils import agdt
import pytest


test_cases = [
    "a-d---ma-",
    "a-d---mac",
    "a-d---mn-",
    "a-p---ca-",
    "a-p---cd-",
    "a-p---cg-",
    "a-p---fa-",
    "a-p---fac",
    "a-p---fd-",
    "a-p---fdc",
    "a-p---fds",
    "a-p---fg-",
    "a-p---fn-",
    "a-p---fnc",
    "a-p---fns",
    "a-p---fv-",
    "a-p---ma-",
    "a-p---mac",
    "a-p---mas",
    "a-p---md-",
    "a-p---mdc",
    "a-p---mds",
    "a-p---mg-",
    "a-p---mgc",
    "a-p---mgs",
    "a-p---mn-",
    "a-p---mnc",
    "a-p---mns",
    "a-p---mv-",
    "a-p---mvs",
    "a-p---na-",
    "a-p---nas",
    "a-p---nd-",
    "a-p---ndc",
    "a-p---nds",
    "a-p---ng-",
    "a-p---nn-",
    "a-p---nnc",
    "a-p---nns",
    "a-s----d-",
    "a-s---fa-",
    "a-s---fac",
    "a-s---fas",
    "a-s---fd-",
    "a-s---fds",
    "a-s---fg-",
    "a-s---fgc",
    "a-s---fgs",
    "a-s---fn-",
    "a-s---fnc",
    "a-s---fns",
    "a-s---fv-",
    "a-s---ma-",
    "a-s---mac",
    "a-s---mas",
    "a-s---md-",
    "a-s---mdc",
    "a-s---mds",
    "a-s---mg-",
    "a-s---mgs",
    "a-s---mn-",
    "a-s---mnc",
    "a-s---mns",
    "a-s---mv-",
    "a-s---na-",
    "a-s---nac",
    "a-s---nas",
    "a-s---nd-",
    "a-s---ndc",
    "a-s---nds",
    "a-s---ng-",
    "a-s---nn-",
    "a-s---nnc",
    "a-s---nns",
    "a-s---nv-",
    "c--------",
    "d--------",
    "d-------c",
    "d-------s",
    "g--------",
    "i--------",
    "l-d---mn-",
    "l-d---nn-",
    "l-p---fa-",
    "l-p---fd-",
    "l-p---fg-",
    "l-p---fn-",
    "l-p---ma-",
    "l-p---md-",
    "l-p---mg-",
    "l-p---mn-",
    "l-p---na-",
    "l-p---nd-",
    "l-p---ng-",
    "l-p---nn-",
    "l-s---fa-",
    "l-s---fd-",
    "l-s---fg-",
    "l-s---fn-",
    "l-s---ma-",
    "l-s---md-",
    "l-s---mg-",
    "l-s---mn-",
    "l-s---na-",
    "l-s---nd-",
    "l-s---ng-",
    "l-s---nn-",
    "m--------",
    "m-----mn-",
    "m-p---cn-",
    "m-p---fn-",
    "m-p---mn-",
    "m-p---nn-",
    "m-s---fa-",
    "m-s---fd-",
    "m-s---fg-",
    "m-s---fn-",
    "m-s---ma-",
    "m-s---mn-",
    "m-s---na-",
    "n--------",
    "n-----mn-",
    "n-d---cn-",
    "n-d---fa-",
    "n-d---fd-",
    "n-d---ma-",
    "n-d---mn-",
    "n-d---na-",
    "n-d---nn-",
    "n-p---ca-",
    "n-p---cd-",
    "n-p---cg-",
    "n-p---cn-",
    "n-p---fa-",
    "n-p---fd-",
    "n-p---fg-",
    "n-p---fn-",
    "n-p---fv-",
    "n-p---ma-",
    "n-p---md-",
    "n-p---mg-",
    "n-p---mn-",
    "n-p---mv-",
    "n-p---na-",
    "n-p---nd-",
    "n-p---ng-",
    "n-p---nn-",
    "n-s---ca-",
    "n-s---cd-",
    "n-s---cg-",
    "n-s---cn-",
    "n-s---fa-",
    "n-s---fd-",
    "n-s---fg-",
    "n-s---fn-",
    "n-s---fv-",
    "n-s---ma-",
    "n-s---md-",
    "n-s---mg-",
    "n-s---mn-",
    "n-s---mv-",
    "n-s---n--",
    "n-s---na-",
    "n-s---nd-",
    "n-s---ng-",
    "n-s---nn-",
    "n-s---nv-",
    "p-d---cd-",
    "p-d---cg-",
    "p-d---cn-",
    "p-d---fa-",
    "p-d---fn-",
    "p-d---ma-",
    "p-d---mn-",
    "p-p---ca-",
    "p-p---cd-",
    "p-p---cg-",
    "p-p---cn-",
    "p-p---fa-",
    "p-p---fd-",
    "p-p---fg-",
    "p-p---fn-",
    "p-p---ma-",
    "p-p---md-",
    "p-p---mg-",
    "p-p---mn-",
    "p-p---na-",
    "p-p---nd-",
    "p-p---ng-",
    "p-p---nn-",
    "p-s---ca-",
    "p-s---cd-",
    "p-s---cg-",
    "p-s---cn-",
    "p-s---cv-",
    "p-s---fa-",
    "p-s---fd-",
    "p-s---fg-",
    "p-s---fn-",
    "p-s---ma-",
    "p-s---md-",
    "p-s---mg-",
    "p-s---mn-",
    "p-s---na-",
    "p-s---nd-",
    "p-s---ng-",
    "p-s---nn-",
    "r--------",
    "u--------",
    "v--ana---",
    "v--anm---",
    "v--anp---",
    "v--fna---",
    "v--fnm---",
    "v--pna---",
    "v--pnm---",
    "v--rna---",
    "v--rnm---",
    "v-dapamn-",
    "v-dapmma-",
    "v-dapmmn-",
    "v-dppamn-",
    "v-dppmmn-",
    "v-drpamn-",
    "v-papafa-",
    "v-papafn-",
    "v-papama-",
    "v-papamd-",
    "v-papamg-",
    "v-papamn-",
    "v-papmfn-",
    "v-papmma-",
    "v-papmmd-",
    "v-papmmg-",
    "v-papmmn-",
    "v-papmna-",
    "v-papmnd-",
    "v-pappfn-",
    "v-pappma-",
    "v-pappmg-",
    "v-pappmn-",
    "v-pappna-",
    "v-pappnn-",
    "v-pfpama-",
    "v-pfpamn-",
    "v-pfpmfn-",
    "v-pfpmmn-",
    "v-pppafa-",
    "v-pppafd-",
    "v-pppafn-",
    "v-pppama-",
    "v-pppamd-",
    "v-pppamg-",
    "v-pppamn-",
    "v-pppana-",
    "v-pppann-",
    "v-pppmfa-",
    "v-pppmfd-",
    "v-pppmfg-",
    "v-pppmfn-",
    "v-pppmma-",
    "v-pppmmd-",
    "v-pppmmg-",
    "v-pppmmn-",
    "v-pppmna-",
    "v-pppmnd-",
    "v-pppmng-",
    "v-ppppma-",
    "v-prpafn-",
    "v-prpama-",
    "v-prpamg-",
    "v-prpamn-",
    "v-prpana-",
    "v-prpann-",
    "v-prpmfa-",
    "v-prpmfn-",
    "v-prpmma-",
    "v-prpmmn-",
    "v-prpmna-",
    "v-prpmnd-",
    "v-prpmng-",
    "v-prpmnn-",
    "v-prppfn-",
    "v-prppmn-",
    "v-sapafa-",
    "v-sapafn-",
    "v-sapama-",
    "v-sapamd-",
    "v-sapamg-",
    "v-sapamn-",
    "v-sapmfa-",
    "v-sapmfd-",
    "v-sapmfg-",
    "v-sapmfn-",
    "v-sapmma-",
    "v-sapmmg-",
    "v-sapmmn-",
    "v-sapmna-",
    "v-sapmnn-",
    "v-sappfa-",
    "v-sappfg-",
    "v-sappfn-",
    "v-sappma-",
    "v-sappmd-",
    "v-sappmg-",
    "v-sappmn-",
    "v-sappng-",
    "v-sfpafn-",
    "v-sfpama-",
    "v-sfpamg-",
    "v-sfpamn-",
    "v-sfpmma-",
    "v-sfpmmn-",
    "v-sppafa-",
    "v-sppafd-",
    "v-sppafg-",
    "v-sppafn-",
    "v-sppafv-",
    "v-sppama-",
    "v-sppamd-",
    "v-sppamg-",
    "v-sppamn-",
    "v-sppana-",
    "v-sppang-",
    "v-sppmfa-",
    "v-sppmfd-",
    "v-sppmfg-",
    "v-sppmfn-",
    "v-sppmma-",
    "v-sppmmd-",
    "v-sppmmg-",
    "v-sppmmn-",
    "v-sppmna-",
    "v-sppmnd-",
    "v-sppmng-",
    "v-sppmnn-",
    "v-srpafa-",
    "v-srpafn-",
    "v-srpama-",
    "v-srpamd-",
    "v-srpamg-",
    "v-srpamn-",
    "v-srpang-",
    "v-srpann-",
    "v-srpmfa-",
    "v-srpmfn-",
    "v-srpmma-",
    "v-srpmmd-",
    "v-srpmmn-",
    "v-srpmna-",
    "v-srpmnn-",
    "v-srppfa-",
    "v-srppmn-",
    "v1paia---",
    "v1paim---",
    "v1paoa---",
    "v1paom---",
    "v1pasa---",
    "v1pasm---",
    "v1pfia---",
    "v1pfim---",
    "v1piia---",
    "v1piim---",
    "v1ppia---",
    "v1ppim---",
    "v1ppoa---",
    "v1ppom---",
    "v1ppsa---",
    "v1ppsm---",
    "v1pria---",
    "v1prim---",
    "v1saia---",
    "v1saim---",
    "v1saip---",
    "v1saoa---",
    "v1saom---",
    "v1saop---",
    "v1sasa---",
    "v1sasm---",
    "v1sfia---",
    "v1sfim---",
    "v1siia---",
    "v1slia---",
    "v1spia---",
    "v1spim---",
    "v1spoa---",
    "v1spom---",
    "v1spsa---",
    "v1spsm---",
    "v1sria---",
    "v1srim---",
    "v1sroa---",
    "v1stim---",
    "v2dpia---",
    "v2paia---",
    "v2paim---",
    "v2paip---",
    "v2pama---",
    "v2pamm---",
    "v2paoa---",
    "v2paom---",
    "v2pasa---",
    "v2pasm---",
    "v2pfia---",
    "v2pfim---",
    "v2piia---",
    "v2piim---",
    "v2ppia---",
    "v2ppim---",
    "v2ppma---",
    "v2ppmm---",
    "v2ppoa---",
    "v2ppom---",
    "v2ppsa---",
    "v2prim---",
    "v2prma---",
    "v2saia---",
    "v2saim---",
    "v2saip---",
    "v2sama---",
    "v2samm---",
    "v2saoa---",
    "v2saom---",
    "v2sasa---",
    "v2sasm---",
    "v2sfia---",
    "v2sfim---",
    "v2siia---",
    "v2siim---",
    "v2spia---",
    "v2spim---",
    "v2spma---",
    "v2spmm---",
    "v2spmp---",
    "v2spoa---",
    "v2spom---",
    "v2spsa---",
    "v2spsm---",
    "v2sria---",
    "v2srim---",
    "v2srma---",
    "v2srmm---",
    "v3daim---",
    "v3diim---",
    "v3dpim---",
    "v3dria---",
    "v3paia---",
    "v3paim---",
    "v3paip---",
    "v3paoa---",
    "v3paom---",
    "v3paop---",
    "v3pasa---",
    "v3pasm---",
    "v3pfia---",
    "v3pfim---",
    "v3piia---",
    "v3piim---",
    "v3plia---",
    "v3plim---",
    "v3ppia---",
    "v3ppim---",
    "v3ppoa---",
    "v3ppom---",
    "v3ppsa---",
    "v3ppsm---",
    "v3pria---",
    "v3prim---",
    "v3saia---",
    "v3saim---",
    "v3saip---",
    "v3samm---",
    "v3saoa---",
    "v3saom---",
    "v3sasa---",
    "v3sasm---",
    "v3sfia---",
    "v3sfim---",
    "v3siia---",
    "v3siim---",
    "v3siip---",
    "v3slia---",
    "v3slim---",
    "v3slip---",
    "v3spia---",
    "v3spim---",
    "v3spma---",
    "v3spmm---",
    "v3spoa---",
    "v3spom---",
    "v3spsa---",
    "v3spsm---",
    "v3sria---",
    "v3srim---",
    "v3srma---",
    "v3srsa---",
    "z--------",
    "V3SRSA---",
]


@pytest.mark.parametrize("morphology", test_cases)
def test_parse_morphology(morphology):
    assert agdt.parse_morphology(morphology, include_names=False) == [
        agdt.name_mapping[k].get(v, None) for k, v in enumerate(morphology.lower())
    ]


def test_morphology_length():
    with pytest.raises(ValueError):
        agdt.parse_morphology("a-d---ma")
    with pytest.raises(ValueError):
        agdt.parse_morphology("nms")


def test_produce_morphology():
    assert agdt.produce_morphology("future") == (3, "f")
    assert agdt.produce_morphology("subjunctive") == (4, "s")
    assert agdt.produce_morphology("passive") == (5, "p")
    assert agdt.produce_morphology("feminine") == (6, "f")
    assert agdt.produce_morphology("genitive") == (7, "g")
    assert agdt.produce_morphology("comparative") == (8, "c")


def test_morphology_string():
    assert (
        agdt.morphology_string(["noun", "masculine", "singular", "nominative"])
        == "n-s---mn-"
    )


def test_morphology_string_with_short_forms():
    assert agdt.morphology_string(["n", "MASC", "sing", "NOM"]) == "n-s---mn-"


position_cases = [
    [1, "part of speech"],
    [2, "person"],
    [3, "number"],
    [4, "tense"],
    [5, "mood"],
    [6, "voice"],
    [7, "gender"],
    [8, "case"],
    [9, "degree"],
    [1, "pos"],
    [1, "part_of_speech"],
    [2, "per"],
    [2, "pers"],
    [3, "num"],
    [4, "ten"],
    [7, "gen"],
    [9, "deg"],
]


@pytest.mark.parametrize("position,name", position_cases)
def test_position_map(position, name):
    assert agdt.position_to_name(position - 1) == agdt.short_form_to_position_name(name)
    assert agdt.name_to_position(name) == position - 1


def test_assert_position_to_name_not_found():
    assert not agdt.name_to_position("not found")
    assert not agdt.position_to_name(10)
