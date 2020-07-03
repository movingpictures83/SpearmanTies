# SpearmanTies
# Language: Python
# Input: CSV (abundances)
# Output: CSV (correlations)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: scipy==1.4.1

PluMA plugin to compute Spearman correlations (Spearman, 1904) with
a built-in method for handling ties.

The plugin expect input in CSV format where rows represent samples
and columns represent entities, with entry (i, j) holding the abundance
of entity j in sample i.

Output correlations will also be in CSV format, with rows and columns
representing entities and entry (i, j) the correlation between entity i
and entity j.
