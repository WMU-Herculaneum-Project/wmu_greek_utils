import pytest
from wmu_greek_utils.normalize import (
    iota_subscript_to_iota_adscript,
    Normalizer,
    NormalizationOptions,
)


def test_iota_subscript_to_iota_adscript():
    text = "ᾴᾳᾲ"
    expected = "άιαιὰι"
    assert iota_subscript_to_iota_adscript(text) == expected


def test_normalizer_lowercase():
    normalizer = Normalizer(config=NormalizationOptions.LOWERCASE)
    text = "ΑΛΕΞΑΝΔΡΟΣ"
    expected = "αλεξανδρος"
    assert normalizer.normalize(text) == expected


def test_normalizer_uppercase():
    normalizer = Normalizer(config=NormalizationOptions.UPPERCASE)
    text = "αλεξανδρος"
    expected = "ΑΛΕΞΑΝΔΡΟΣ"
    assert normalizer.normalize(text) == expected


def test_normalizer_remove_spaces():
    normalizer = Normalizer(config=NormalizationOptions.REMOVE_SPACES)
    text = "Α λ ε ξ α ν δ ρ ο ς"
    expected = "Αλεξανδρος"
    assert normalizer.normalize(text) == expected


def test_normalizer_remove_newlines():
    normalizer = Normalizer(config=NormalizationOptions.REMOVE_NEWLINES)
    text = "Αλεξανδρος\n"
    expected = "Αλεξανδρος"
    assert normalizer.normalize(text) == expected


def test_normalizer_remove_accents():
    normalizer = Normalizer(config=NormalizationOptions.REMOVE_ACCENTS)
    text = "ᾴᾶᾲ"
    expected = "ᾳαᾳ"
    assert normalizer.normalize(text) == expected
    assert normalizer.normalize(text.upper()) == expected.upper()


def test_normalizer_remove_smooth_breathing():
    normalizer = Normalizer(config=NormalizationOptions.REMOVE_BREATHING)
    text = "ἀλφα"
    expected = "αλφα"
    assert normalizer.normalize(text) == expected
    assert normalizer.normalize(text.upper()) == expected.upper()


def test_normalizer_remove_rough_breathing():
    normalizer = Normalizer(config=NormalizationOptions.REMOVE_BREATHING)
    text = "ἱππος"
    expected = "ιππος"
    assert normalizer.normalize(text) == expected
    assert normalizer.normalize(text.upper()) == expected.upper()


def test_normalizer_iota_adscript():
    normalizer = Normalizer(config=NormalizationOptions.IOTA_ADSCRIPT)
    text = "ᾴᾳᾲ"
    expected = "άιαιὰι"
    assert normalizer.normalize(text) == expected


def test_normalizer_normalize_sigma():
    normalizer = Normalizer(config=NormalizationOptions.NORMALIZE_SIGMA)
    text = "σςϲΣϹ"
    expected = "ϲϲϲϹϹ"
    assert normalizer.normalize(text) == expected


def test_normalizer_normalize_theta():
    normalizer = Normalizer(config=NormalizationOptions.NORMALIZE_THETA)
    text = "θϑΘϴ"
    expected = "θθΘΘ"
    assert normalizer.normalize(text) == expected


def test_normalizer_normalize_phi():
    normalizer = Normalizer(config=NormalizationOptions.NORMALIZE_PHI)
    text = "φϕ"
    expected = "φφ"
    assert normalizer.normalize(text) == expected


def test_normalizer_normalize_apostrophe():
    normalizer = Normalizer(config=NormalizationOptions.NORMALIZE_APOSTROPHE)
    text = "Αλέξανδρος\u2019"
    expected = "Αλέξανδρος'"
    assert normalizer.normalize(text) == expected


def test_normalizer_all():
    normalizer = Normalizer(config=NormalizationOptions.ALL)
    text = "Α λ έ ξ α ν δ ρ ο ςͅ\n"  # weird iota subscript
    expected = "ΑΛΕΞΑΝΔΡΟϹΙ"
    assert normalizer.normalize(text) == expected


def test_call():
    normalizer = Normalizer()  # default config is STANDARD
    text = "Ἐν ἀρχῇ ἦν ὁ Λόγος, καὶ ὁ Λόγος ἦν πρὸς τὸν ϑεόν, καὶ ϑεὸς ἦν ὁ Λόγος."
    expected = "ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν, καὶ θεὸς ἦν ὁ λόγος."
    assert normalizer(text) == expected


def test_call_all():
    normalizer = Normalizer(config=NormalizationOptions.ALL)
    text = "Ἐν ἀρχῇ ἦν ὁ Λόγος, καὶ ὁ Λόγος ἦν πρὸς τὸν ϑεόν, καὶ ϑεὸς ἦν ὁ Λόγος."
    expected = "ΕΝΑΡΧΗΙΗΝΟΛΟΓΟϹΚΑΙΟΛΟΓΟϹΗΝΠΡΟϹΤΟΝΘΕΟΝΚΑΙΘΕΟϹΗΝΟΛΟΓΟϹ"
    assert normalizer(text) == expected
