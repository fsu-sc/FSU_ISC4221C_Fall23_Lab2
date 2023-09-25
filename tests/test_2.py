import answers_lab
import pytest

def test_frequency_amino_acid():
    protein = 'AGATTCGAAGGTCAGCATTACTTATCTTCATACCTAAATAGGTTCAGCTTCCGTACAACTGAAGTGGCCCGCGACCTCATGAATGCCATATCGCATTACGCCCGCATGGTCCCAATTCTCTCAGAGATTTCTAAAGGCCCCTACCTGGAT'
    print(len(protein))
    assert answers_lab.frequency_amino_acid(protein, 'Isoleucine') == 3
    assert answers_lab.frequency_amino_acid(protein, 'Leucine') == 5
    assert answers_lab.frequency_amino_acid(protein, 'Valine') == 2
    assert answers_lab.frequency_amino_acid(protein, 'Phenylalanine') == 3
    assert answers_lab.frequency_amino_acid(protein, 'Methionine') == 2
    assert answers_lab.frequency_amino_acid(protein, 'Cysteine') == 0
    assert answers_lab.frequency_amino_acid(protein, 'Alanine') == 3
    assert answers_lab.frequency_amino_acid(protein, 'Glycine') == 2
    assert answers_lab.frequency_amino_acid(protein, 'Proline') == 2
    assert answers_lab.frequency_amino_acid(protein, 'Threonine') == 2
    assert answers_lab.frequency_amino_acid(protein, 'Serine') == 6
    assert answers_lab.frequency_amino_acid(protein, 'Tyrosine') == 4
    assert answers_lab.frequency_amino_acid(protein, 'Tryptophan') == 0
    assert answers_lab.frequency_amino_acid(protein, 'Glutamine') == 1
    assert answers_lab.frequency_amino_acid(protein, 'Asparagine') == 2
    assert answers_lab.frequency_amino_acid(protein, 'Histidine') == 2
    assert answers_lab.frequency_amino_acid(protein, 'Glutamic acid') == 3
    assert answers_lab.frequency_amino_acid(protein, 'Aspartic acid') == 2
    assert answers_lab.frequency_amino_acid(protein, 'Lysine') == 1
    assert answers_lab.frequency_amino_acid(protein, 'Arginine') == 5
    assert answers_lab.frequency_amino_acid(protein, 'Stop codons') == 0

    # print(f"{answers_lab.frequency_amino_acid(protein, 'Isoleucine') } Isoleucine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Leucine')     } Leucine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Valine')      } Valine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Phenylalanine')} Phenylalanine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Methionine')  } Methionine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Cysteine')    } Cysteine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Alanine')     } Alanine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Glycine')     } Glycine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Proline')     } Proline")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Threonine')   } Threonine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Serine')      } Serine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Tyrosine')    } Tyrosine") 
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Tryptophan')  } Tryptophan")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Glutamine')   } Glutamine") 
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Asparagine')  } Asparagine") 
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Histidine')   } Histidine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Glutamic acid')} Glutamic acid")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Aspartic acid')} Aspartic acid")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Lysine')      } Lysine")
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Arginine')    } Arginine") 
    # print(f"{answers_lab.frequency_amino_acid(protein, 'Stop codons') } Stop codons") 


test_frequency_amino_acid()