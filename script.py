import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def count_kmers(sequence, k):
    
    kmer_counts = {} 
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]  
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1  
        else:
            kmer_counts[kmer] = 1 
    return kmer_counts

def generate_kmer_heatmap(sequence, k):
  
    kmer_counts = count_kmers(sequence, k)
 
    kmer_labels = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    kmer_frequencies = [kmer_counts[kmer] for kmer in kmer_labels]  

    heatmap_data = np.array(kmer_frequencies).reshape(1, -1)

    plt.figure(figsize=(10, 2))
    sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, xticklabels=kmer_labels, yticklabels=["Frequency"])
    plt.title(f"Heatmap of {k}-mer Occurrences")
    plt.xlabel("K-mers along sequence")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)  
    plt.show()


sequence = "AAAACCCTTTTGGGACTG"
k = 2
print("K-mer Frequencies:", count_kmers(sequence, k))  
generate_kmer_heatmap(sequence, k) 