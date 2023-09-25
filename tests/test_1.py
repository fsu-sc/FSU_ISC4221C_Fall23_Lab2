import answers_lab
import pytest

def test_generate_random_protein():
    protein = answers_lab.generate_random_protein(10)
    assert len(protein) == 30
    assert set(protein).issubset(set('ATCG'))