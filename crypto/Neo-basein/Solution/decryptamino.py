def amino_to_binary(amino_sequence):
    inverse_mapping = {
        "Serine": "000",
        "Proline": "001",
        "Leucine": "010",
        "Valine": "011",
        "Threonine": "100",
        "Alanine": "101",
        "Glycine": "110",
        "Arginine": "111"
    }

    binary_sequence = ""

    for amino_acid in amino_sequence:
        if amino_acid in inverse_mapping:
            binary_sequence += inverse_mapping[amino_acid]+" "
        else:
            raise ValueError(f"Invalid amino acid: {amino_acid}")

    return binary_sequence

amino_sequence="Valine Leucine Leucine Glycine Arginine Proline Threonine Arginine Valine Proline Leucine Glycine Arginine Proline Alanine Proline Valine Alanine Leucine Glycine Glycine Alanine Glycine Valine Valine Glycine Glycine Alanine Proline Serine Glycine Serine Valine Alanine Leucine Valine Valine Alanine Valine Arginine Leucine Proline Serine Glycine Threonine Alanine Glycine Leucine Leucine Arginine Glycine Threonine Glycine Threonine Glycine Valine Leucine Proline Serine Threonine Proline Alanine Alanine Proline Leucine Valine Threonine Alanine Arginine Alanine Serine Arginine Leucine Proline Glycine Alanine Arginine Alanine Serine Threonine Proline Threonine Serine Glycine Proline Alanine Arginine Alanine"
binary_sequence = amino_to_binary(amino_sequence.split())
print(binary_sequence)
