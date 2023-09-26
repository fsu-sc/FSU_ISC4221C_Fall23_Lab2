<h1 style="text-align:center;">ISC4221C Discrete Algorithms for Science Applications (Fall 2023) Lab 2</h1>

# Applications of Search Algorithms

**All your answers should be in a single file named `answers_lab.py`, be careful with the names of your functions. Your report should be a self contained markdown file with a summary of your answers and the code copied inside of it.**
 
A protein is composed of amino acids. There are a total of twenty amino acids which are known. The protein itself is represented by a string of these amino acid "names". The twenty amino acids are Alanine, Arginine, Asparagine, Aspartic Acid, Cysteine, Glutamic Acid, Glutamine, Glycine, Histidine, Isoleucine, Leucine, Lysine, Methionine, Phenylalanine, Proline, Serine, Threonine, Tryptophan, Tyrosine, and Valine.  A DNA molecule is a long chain composed of four different nucleotides: adenine (A), guanine (G), cytosine (C), and thymine (T). A gene is a DNA fragment that codes for a particular protein. Each amino acid is represented by a string of three letters (from A, G, C, and T) called a “codon.” So, for a gene, we might have a string like

<center>ATC-GTA-TTG-CAC-ATT-GCA</center>

Where we have added hyphens to demonstrate the amino acid combinations, because the amino acids are denoted using the four symbols "A", "G", "C" and "T", there are $4^3 = 64$ possible combinations because a letter can be repeated. However, there are only 20 amino acids, so there is some redundancy that just means that different codons (such as GCT, GCC, GCA, GCG) represent the same amino acid (such as alanine). In addition, three of the 64 combinations are used to tag a stop, so there are 61 codons for the 20 amino acids.  Numerous websites such as

[http://www.cbs.dtu.dk/courses/27619/codon.html](http://www.cbs.dtu.dk/courses/27619/codon.html)

You may find a table that associates the DNA codon with the corresponding amino acid. The table from the above link is given below.

| Amino Acid     | SLC  | Codons                       |
| -------------- |-- | --------------------------------|
| Isoleucine     | I | ATT, ATC, ATA                   |
| Leucine        | L | CTT, CTC, CTA, CTG, TTA, TTG    |
| Valine         | V | GTT, GTC, GTA, GTG              |
| Phenylalanine  | F | TTT, TTC                        |
| Methionine     | A | ATG                             |
| Cysteine       | C | TGT, TGC                        |
| Alanine        | A | GCT, GCC, GCA, GCG              |
| Glycine        | G | GGT, GGC, GGA, GGG              |
| Proline        | P | CCT, CCC, CCA, CCG              |
| Threonine      | T | ACT, ACC, ACA, ACG              |
| Serine         | S | TCT, TCC, TCA, TCG, AGT, AGC    |
| Tyrosine       | Y | TAT, TAC                        |
| Tryptophan     | W | TGG                             |
| Glutamine      | Q | CAA, CAG                        |
| Asparagine     | N | AAT, AAC                        |
| Histidine      | H | CAT, CAC                        |
| Glutamic acid  | E | GAA, GAG                        |
| Aspartic acid  | D | GAT, GAC                        |
| Lysine         | K | AAA, AAG                        |
| Arginine       | R | CGT, CGC, CGA, CGG, AGA, AGG    |
| Stop codons    | Stop | TAA, TAG, TGA                |

**Table 1.** 20 Amino acids, their single-letter database codes (SLC) and  their corresponding DNA codons.

###  1. (30 points) Generate  a random protein

Your function should have the structure:
```python
def generate_random_protein(n)
    #code
    return protein # a string of length 3𝑛 for example if n = 2 return 'GATCGA'
```

Note that the only input to the function is **n** which is the number of amino acids to have in your protein.
The return value protein is a string of length **3𝑛**. A suggested structure of the function is
* Initialize an empty protein array as **protein=[]**
* Generate three random integers in the range of 1 to 4.
* Let 1 represent ‘A’, 2 represent ‘G’, ‘3’ represent ‘C’, and ‘4’ represent ‘T’. Pick off your 3-letter
  codon based on the three random integers. If the codon is one of three stop codons TAA, TAG, or TGA, discard it and re-generate a new codon.
* Add your codon to the existing protein to reach the length of **3𝑛**. Add the new codon to the protein as:   `protein.append(new_codon)`

**In your report file, generate a random protein that has 40 amino acids and attach the output of your code.**

### 2. (70 points) Counting the occurrence of a given amino acid 

Implement a function called `frequency_amino_acid()` in which we employ the sequential search to count
the number of occurrences of a given amino acid (codon) in any protein.
The interface of the function should look like:

```python
def frequency_amino_acid(protein, amino_acid):
```

For example, if amino_acid=’Cysteine’, the `frequency_amino_acid()` function will search for
the corresponding codons “TGT” and “TGC” in protein. If we found $M_1$ occurrence of codon TGT and
$M_2$ occurrence of codon TGC, the total occurrences of “Cysteine” is $M_1 + M_2$, and the function should return $M_1 + M_2$. The 20 amino acids and their corresponding codons are given in Table 1. 
